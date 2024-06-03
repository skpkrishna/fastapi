# fastapi
1. create a virtual environment using python3 -m venv env
2. Clone the repository
3. Activate the Virtual environment source env/bin/activate
4. Install all the python dependencies using pip3 install -r requirements.txt
5. Run the command "uvicorn main:app --reload"
6. POST /compute
   will create an entry
  GET /compute 
  will retrieve all the entries
  GET /compute/{batch_id}
  will retrieve a specific entry
7. To run tests "pytest"
