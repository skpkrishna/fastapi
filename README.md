# fastapi
1. create a virtual environment using python3 -m venv env
2. Clone the repository
3. Activate the Virtual environment source env/bin/activate
4. Install all the python dependencies using pip3 install -r requirements.txt
5. Run the command "uvicorn main:app --reload"
6. API Documentation 

  POST /compute
  request payload :
  {
    "batch_id": "id0102",
    "payload": [[1,2], [3,4]]
  }

  success response: {
    "batch_id": "id0102",
    "response": [3, 7],
    "status": "success",
    "started_at": "2024-06-06 13:08:39",
    "completed_at": "2024-06-06 13:08:50"
  }

  failure response: {
    "batch_id": "id0102",
    "response": [],
    "status": "failed",
    "started_at": "2024-06-06 13:08:39",
    "completed_at": ""
  }

  GET /compute 

  [
    {
      "batch_id": "id0102",
      "response": [3, 7],
      "status": "success",
      "started_at": "2024-06-06 13:08:39",
      "completed_at": "2024-06-06 13:08:50"
    },
    {
      "batch_id": "id0103",
      "response": [3, 7],
      "status": "success",
      "started_at": "2024-06-06 13:08:39",
      "completed_at": "2024-06-06 13:08:50"
    }
  ]
  
  GET /compute/{id}
  /compute/id0102
  {
    "batch_id": "id0102",
    "response": [3, 7],
    "status": "success",
    "started_at": "2024-06-06 13:08:39",
    "completed_at": "2024-06-06 13:08:50"
  }
  
7. To run tests "pytest"
