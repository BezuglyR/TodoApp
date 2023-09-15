# TodoApp - todo application

Application to manage users todos

### Python version

TodoApp use **python 3.7** version for project

### Install and run

1. clone project from github to local folder

2. download and install [python 3.7.10](https://www.python.org/ftp/python/3.7.10/python-3.7.10-amd64.exe)

3. change directory to local folder with cloned project

4. create virtual invironment `python -m venv venv` or `python3 -m venv venv` for windows

5. install dependencies `pip install -r requirements.txt`

6. create environment variables for pasgresql server, see config.py

7. start project web server `uvicorn main:app --reload`

8. visit http://127.0.0.1:8000

### Deployed test app

Test app was deployed on Render for test view [TodoApp](https://todoapp-iyp9.onrender.com)

   
