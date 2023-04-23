@echo off
call venv\Scripts\activate.bat
cd flaskr
set FLASK_APP=__init__.py
set FLASK_DEBUG=true
flask run