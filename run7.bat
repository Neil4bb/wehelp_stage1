@echo off
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

call venv\Scripts\activate
cd week7
python -m uvicorn main:app --reload

pause