import json
import logging

class JsonFormatter(logging.Formatter):
    def __init__(self, fmt_dict: dict = None, time_format: str = "%Y-%m-%dT%H:%M:%S", msec_format: str = "%s.%03dZ"):
        self.fmt_dict = fmt_dict if fmt_dict is not None else {"message": "message"}
        self.default_time_format = time_format
        self.default_msec_format = msec_format
        self.datefmt = None

    def usesTime(self) -> bool:
        return "asctime" in self.fmt_dict.values()

    def formatMessage(self, record) -> dict:
        return {fmt_key: record.__dict__[fmt_val] for fmt_key, fmt_val in self.fmt_dict.items()}

    def format(self, record) -> str:
        record.message = record.getMessage()
        
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        message_dict = self.formatMessage(record)

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)

        if record.exc_text:
            message_dict["exc_info"] = record.exc_text

        if record.stack_info:
            message_dict["stack_info"] = self.formatStack(record.stack_info)

        if "req" in record.__dict__:
            message_dict["request"] = record.__dict__["req"]
        if "res" in record.__dict__:
            message_dict["response"] = record.__dict__["res"]
        if record.levelno == logging.ERROR and record.exc_info:
            message_dict["error"] = self.formatException(record.exc_info)

        return json.dumps(message_dict, default=str)

logger = logging.root

json_formatter = JsonFormatter({"level": "levelname", 
                                "message": "message", 
                                "loggerName": "name", 
                                "processName": "processName",
                                "processID": "process", 
                                "threadName": "threadName", 
                                "threadID": "thread",
                                "timestamp": "asctime"})


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(json_formatter)
log_dir = './logs/'
import os
if not os.path.isdir(log_dir):
   os.makedirs(log_dir)
json_handler = logging.FileHandler('./logs/app.log')
json_handler.setFormatter(json_formatter)

logger.handlers = [stream_handler, json_handler]
logger.setLevel(logging.DEBUG)
logging.getLogger("uvicorn.access").disabled = True

