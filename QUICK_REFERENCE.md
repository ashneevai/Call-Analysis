# 🎯 Quick Reference Card - Verizon Call Classifier UI

## 🚀 START HERE

**Start the UI:**
```powershell
# Option 1: Double-click → run_ui.bat
# Option 2: Run this command
streamlit run app.py
```

**Access:** http://localhost:8501

---

## 📱 4 Main Tabs

### 1. 📥 Classify Single Call
**What:** Classify one customer call at a time
**How:**
1. Paste transcript in text box
2. Click "🔍 Classify Call" button
3. View results instantly
4. Download as TXT/CSV/JSON

**Time:** ~100ms | **Cost:** Free

---

### 2. 📊 Analysis Dashboard
**What:** View all processed calls & analytics
**How:**
1. Classify some calls first
2. Go to Analysis tab
3. See statistics and charts
4. Review call history table

**Shows:** Total calls, avg confidence, trends, distribution

---

### 3. ⚡ Batch Processing
**What:** Process multiple calls at once
**How:**
1. Paste multiple transcripts
2. Separate each with `---`
3. Click "⚡ Process Batch"
4. Download results as CSV

**Time:** ~100ms per call

---

### 4. 📚 Sample Calls
**What:** Test with pre-built examples
**How:**
1. Expand any sample
2. Click "Classify this sample"
3. See instant results
4. Learn from examples

**5 Samples Included:** Tech Support, Billing, Retention, Account, Sales

---

## 🎯 Call Categories (8 Types)

| Category | Key Words |
|----------|-----------|
| **💳 Billing** | bill, charge, invoice, payment, price |
| **🔧 Tech Support** | connection, network, wifi, not working |
| **👤 Account** | update, change, plan, account, address |
| **📞 Customer Service** | complaint, issue, help, support |
| **🎯 Retention** | cancel, leave, competitor, deal |
| **📈 Sales** | upgrade, buy, new plan, package |
| **💰 Refund** | refund, credit, compensation, return |
| **🔐 Fraud** | fraud, unauthorized, suspicious, security |

---

## 💡 Example Transcripts

### Technical Support
```
Customer: My internet is down!
Agent: Let me help troubleshoot this.
Customer: It's been out for 2 hours.
Agent: I'll escalate to technical support.
```
→ Classification: **TECHNICAL_SUPPORT** ✅

### Billing Issue
```
Customer: I was charged twice!
Agent: Let me check your account.
Customer: I need a refund immediately.
Agent: I'll process that right away.
```
→ Classification: **BILLING** ✅

### Retention
```
Customer: I want to cancel.
Agent: May I ask why?
Customer: Your prices are too high.
Agent: Let me see what we can offer.
```
→ Classification: **RETENTION** ✅

---

## 📊 Results Explained

### Metrics Shown
- **Primary Category** - Main issue type
- **Confidence** - 0-100% (how sure the system is)
- **Sentiment** - Positive/Negative/Neutral
- **Urgency** - Low/Medium/High
- **Duration** - Short/Medium/Long
- **Services** - Mobile, Internet, TV, etc.
- **Issues** - Detected problems
- **Requests** - What customer wants

### Charts
- **Bar Chart** - Category confidence scores
- **Pie Chart** - Distribution of calls/sentiment
- **Table** - Call history details

---

## 💾 Export Formats

### Download Options
1. **📄 TXT** - Human-readable report
2. **📊 CSV** - Spreadsheet format
3. **📋 JSON** - Data integration format

### How to Download
- Click download button after classification
- Choose format (TXT/CSV/JSON)
- Save to your computer

---

## ⚙️ Settings (Sidebar)

### Classification Method
- **Keyword-Based** (Fast) - Instant, ~100ms
- **AI-Powered** (Slow) - Intelligent, 5-30s (needs API)

### Information
- System description
- About the categories
- What the system does

### Call History
- Toggle to show/hide history
- Persistent during session

---

## 🎓 Tips & Tricks

### ✅ Do's
- ✅ Use complete transcripts with both customer & agent
- ✅ Include timestamps for better accuracy
- ✅ Process multiple calls in batch mode
- ✅ Export results for records
- ✅ Review sample calls to learn patterns

### ❌ Don'ts
- ❌ Use only customer text (include agent responses)
- ❌ Paste very short fragments
- ❌ Skip the sample calls on first use
- ❌ Expect 100% accuracy (confidence varies)
- ❌ Close browser without saving important results

---

## 🔧 Troubleshooting

### Problem: "Connection refused"
**Solution:** Make sure Streamlit is running
```powershell
streamlit run app.py
```

### Problem: "Port already in use"
**Solution:** Use different port
```powershell
streamlit run app.py --server.port 8502
```

### Problem: Missing modules
**Solution:** Reinstall dependencies
```powershell
pip install -r requirements.txt
```

### Problem: Very slow processing
**Solution:** Switch to keyword-based method in sidebar

---

## 📈 Performance

| Task | Time | Notes |
|------|------|-------|
| Load Page | 500ms | First time only |
| Classify Call | 100ms | Keyword-based |
| Batch (10 calls) | 1 second | Sequential |
| Generate Chart | 50ms | Real-time |
| Export | Instant | Download starts |

---

## 🎯 Common Scenarios

### Scenario 1: Single Call
```
1. Paste transcript
2. Click "Classify Call"
3. Review results
4. Download report
```

### Scenario 2: Batch of 5 Calls
```
1. Get 5 transcripts
2. Put "---" between each
3. Go to Batch tab
4. Click "Process Batch"
5. Download CSV
```

### Scenario 3: Learning the System
```
1. Go to Sample Calls tab
2. Try each sample one by one
3. See classification results
4. Understand patterns
5. Ready for real calls
```

---

## 💡 Pro Tips

- 🎯 **Batch processing** is faster for multiple calls
- 📊 **Analysis tab** shows trends over time
- 📄 **Export** results regularly for backup
- 🔄 **Refresh** page to clear session history
- 💡 **Try samples** first before real transcripts

---

## 🚀 Getting Help

1. **Read:** Check `UI_GUIDE.md` for details
2. **Browse:** Look at sample calls
3. **Try:** Experiment with different inputs
4. **Export:** Save results for review
5. **Repeat:** Classify more calls

---

## ✨ Features at a Glance

| Feature | Where | How |
|---------|-------|-----|
| Classify | Tab 1 | Paste & click |
| View History | Tab 2 | See dashboard |
| Batch Process | Tab 3 | Separate with --- |
| Test Samples | Tab 4 | Click sample |
| Export Results | All Tabs | Download button |
| Settings | Sidebar | Choose method |

---

## 🎉 Summary

```
📞 Verizon Call Classifier UI
├─ 📥 Classify single calls
├─ 📊 View analytics
├─ ⚡ Batch process
├─ 📚 Sample calls
├─ 💾 Export results
└─ ✅ No setup needed!

URL: http://localhost:8501
Status: ✅ LIVE
Time: ~100ms per call
Cost: FREE
```

---

**🎯 Start Now:** Open http://localhost:8501 in your browser!

**Version:** 1.0 | **Date:** January 8, 2026 | **Status:** ✅ Ready
