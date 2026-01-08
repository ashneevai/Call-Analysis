#!/bin/bash
# Start the Streamlit Web UI for Verizon Call Classifier

echo ""
echo "======================================"
echo "Starting Verizon Call Classifier UI"
echo "======================================"
echo ""

# Activate virtual environment
source venv/bin/activate

# Start Streamlit
echo "Starting Streamlit server..."
streamlit run app.py
