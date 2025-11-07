@echo off
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
call venv\Scripts\activate
python -m uvicorn main:app --reload
pause