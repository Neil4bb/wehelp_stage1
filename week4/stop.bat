@echo off
chcp 65001 >nul
echo ====================================
echo 🧹 正在結束 FastAPI 伺服器與環境...
echo ====================================

:: 嘗試中止所有 uvicorn 進程
echo 停止伺服器中...
taskkill /F /IM "python.exe" /T >nul 2>&1

:: 停用虛擬環境
echo 停用虛擬環境...
call venv\Scripts\deactivate.bat >nul 2>&1

:: 清理畫面
cls
echo ✅ 伺服器與虛擬環境已結束。
echo ====================================
echo 💡 下次開發請執行 run.bat
pause