@echo off
REM Start the Streamlit Web UI for Verizon Call Classifier

echo.
echo ======================================
echo Starting Verizon Call Classifier UI
echo ======================================
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start Streamlit
echo Starting Streamlit server...
streamlit run app.py

pause
