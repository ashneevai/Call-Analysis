# Verizon Call Classifier - Web UI Guide

## 🚀 Quick Start

### Option 1: Using the Batch Script (Easiest)
Double-click the `run_ui.bat` file to start the web interface automatically.

### Option 2: Manual Start (PowerShell)
```powershell
# Navigate to project directory
cd 'c:\Users\LENOVO\Documents\Google ADK\Crew AI- Customer call agent'

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start the web app
streamlit run app.py
```

### Option 3: Manual Start (Command Prompt)
```cmd
cd c:\Users\LENOVO\Documents\Google ADK\Crew AI- Customer call agent
venv\Scripts\activate.bat
streamlit run app.py
```

## 🌐 Accessing the Web Interface

Once started, the application will be available at:
- **Local URL:** http://localhost:8501
- **Network URL:** http://192.168.1.5:8501 (for other devices on your network)

The server should start automatically in your browser. If not, manually visit the URL above.

## 📱 Interface Features

### 📥 Tab 1: Classify Single Call
- **Paste Transcript:** Enter a customer call transcript
- **Classification:** Get instant category classification with confidence score
- **Analysis:** View sentiment, urgency, and key information extracted
- **Visualization:** See confidence scores for all categories
- **Export:** Download results as TXT, CSV, or JSON

**Supported Categories:**
1. Billing - Invoices, payments, pricing
2. Technical Support - Network, connectivity issues
3. Account Management - Plan changes, account info
4. Customer Service - General inquiries, complaints
5. Retention - Cancellation prevention
6. Sales - Upgrades, new services
7. Refund - Refunds, credits, compensation
8. Fraud - Security concerns

### 📊 Tab 2: Analysis Dashboard
- **Call History:** View all previously classified calls
- **Statistics:** Summary metrics and trends
- **Category Distribution:** Pie chart showing call distribution
- **Call Summary Table:** Quick overview of all processed calls

### ⚡ Tab 3: Batch Processing
- **Multiple Calls:** Paste multiple transcripts separated by `---`
- **Batch Processing:** Process all at once
- **Summary Reports:** Visualizations and statistics
- **Batch Export:** Download all results as CSV

### 📚 Tab 4: Sample Calls
- **Pre-built Examples:** 5 different sample call transcripts
- **Quick Testing:** Test classification instantly
- **Learn Patterns:** See how different call types are classified

### ⚙️ Sidebar Settings
- **Classification Method:** Choose between keyword-based (fast) or AI-powered (slow)
- **About:** Information about the system
- **Call History:** Toggle history display

## 💡 Usage Examples

### Example 1: Single Call Classification
1. Click "Classify Call" tab
2. Paste this transcript:
   ```
   Customer: Hi, my internet is down!
   Agent: I'm sorry to hear that.
   Customer: This is urgent, I work from home.
   Agent: Let me escalate to technical support.
   ```
3. Click "Classify Call" button
4. View results in real-time

### Example 2: Batch Processing
1. Click "Batch Process" tab
2. Paste multiple transcripts separated by `---`:
   ```
   [Call 1 transcript]
   ---
   [Call 2 transcript]
   ---
   [Call 3 transcript]
   ```
3. Click "Process Batch"
4. View statistics and download CSV

### Example 3: Using Sample Calls
1. Click "Sample Calls" tab
2. Click "Classify this sample" for any sample
3. View instant classification results

## 📊 Understanding the Results

### Classification Metrics
- **Category:** The primary issue category
- **Confidence Score:** How confident the system is (0-100%)
- **Sentiment:** Customer emotion (Positive/Negative/Neutral)
- **Urgency:** Priority level (Low/Medium/High)

### Category Scores
- Bar chart shows confidence for all 8 categories
- Blue bar indicates the selected category
- Gray bars show alternatives

### Customer Information
- **Services:** Mobile, Internet, TV, Home, Business
- **Issues:** Reported problems
- **Requests:** What customer wants (discount, upgrade, cancel, etc.)
- **Sentiment Markers:** Indicators like frustration, gratitude, urgency

## 🎯 Routing Recommendations

Based on classification, the system recommends:
- **Billing** → Finance/Billing Department
- **Technical Support** → Technical Support Team
- **Account Management** → Account Services
- **Customer Service** → General Support
- **Retention** → Retention Specialists
- **Sales** → Sales Team
- **Refund** → Credits & Refunds Department
- **Fraud** → Security & Fraud Team

## 💾 Export Options

Each classified call can be exported as:
- **TXT:** Human-readable report
- **CSV:** For spreadsheet analysis
- **JSON:** For integration with other systems

## 🔧 Troubleshooting

### Issue: "Port 8501 already in use"
```powershell
# Kill existing process
lsof -i :8501
# Or manually specify a different port
streamlit run app.py --server.port 8502
```

### Issue: Module not found errors
```powershell
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Slow classification
- Use "Keyword-Based" method in sidebar
- Batch process instead of single calls

## 🔐 Security Notes

- **No data is stored** persistently on disk
- **Call history** is only kept during the session
- **Local only** - runs on your machine
- No API calls required for basic classification

## ⚡ Performance

- **Keyword-Based:** ~100ms per call
- **AI-Powered:** ~5-30 seconds per call (requires API)
- **Batch Processing:** Scales linearly with number of calls

## 🎨 Customization

To customize the UI, edit `app.py`:
- Colors and themes in the markdown styling section
- Add new sample calls in the Sample Calls tab
- Modify categories in `tools/classification_tools.py`
- Change the layout using Streamlit functions

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the README.md in the project root
3. Check the VENV_SETUP.md for environment issues

## 🚀 Next Steps

1. **Start the UI** using one of the methods above
2. **Test with samples** in the "Sample Calls" tab
3. **Classify real calls** using the "Classify Call" tab
4. **Batch process** multiple calls in "Batch Process" tab
5. **Review analytics** in the "Analysis" dashboard
6. **Export results** for further analysis

---

**Version:** 1.0  
**Last Updated:** January 8, 2026  
**Status:** ✅ Ready for Production
