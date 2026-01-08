# ABC Telecom Customer Call Analysis - Crew AI

A comprehensive Crew AI application for analyzing and classifying ABC Telecom customer support calls into different categories.

## Project Overview

This project uses **Crew AI** to automate the analysis and classification of customer service calls for ABC Telecom. The system categorizes calls into 8 different types:

- **Billing**: Invoice, payment, and pricing inquiries
- **Technical Support**: Network issues, connectivity problems, service troubleshooting  
- **Account Management**: Account changes, plan modifications, account information
- **Customer Service**: General inquiries, complaints, escalations
- **Retention**: Cancellation prevention, upgrade offers, loyalty programs
- **Sales**: New service sales, plan upgrades, promotional offers
- **Refund**: Refund requests, credits, compensation
- **Fraud**: Fraud detection, security concerns, identity verification

## Features

### Crew AI Agents
1. **Call Analyzer Agent** - Analyzes transcripts to understand customer needs, sentiment, and issues
2. **Call Classifier Agent** - Categorizes calls into appropriate departments
3. **Quality Assurance Agent** - Reviews classifications for accuracy and compliance
4. **Action Plan Coordinator** - Creates comprehensive action plans and recommendations

### Classification Tools
- Sentiment analysis
- Duration estimation
- Topic extraction
- Urgency assessment
- Customer information extraction
- Service identification
- Issue detection
- Sentiment indicator analysis

### Processing Modes
- **Full Analysis**: Complete workflow with QA review and action plans
- **Quick Classification**: Fast analysis and categorization for high-volume processing

## Project Structure

```
.
├── main.py                          # Main application entry point
├── test_classification.py           # Quick test without full Crew AI
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore file
│
├── src/
│   ├── agents.py                   # Crew AI agents definitions
│   ├── tasks.py                    # Crew AI tasks definitions
│   └── crew.py                     # Crew configuration
│
├── tools/
│   └── classification_tools.py     # Classification functions and tools
│
└── data/
    └── sample_transcripts.py       # Sample customer call transcripts
```

## Installation

### Prerequisites
- Python 3.9 or higher
- OpenAI API key for Claude/GPT models

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd "c:\Users\LENOVO\Documents\Google ADK\Crew AI- Customer call agent"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   copy .env.example .env
   # Edit .env and add your OpenAI API key
   ```

## Usage

### Quick Classification Test (Recommended First)
Test the classification system without requiring Crew AI/API:

```bash
python test_classification.py
```

This will classify 5 sample customer calls and show:
- Sentiment analysis
- Call duration estimate
- Extracted information
- Category classification with confidence scores
- Full classification reports

### Full Crew AI Analysis
Run the complete crew-based analysis:

```bash
python main.py
```

This will:
1. Analyze customer calls
2. Classify them into categories
3. Perform QA review
4. Generate action plans
5. Create comprehensive reports

### Using in Your Own Code

```python
from tools.classification_tools import classify_call_category, generate_classification_report

# Your customer call transcript
transcript = """
Customer: Hi, I have issues with my internet...
Agent: I'll help you troubleshoot...
"""

# Quick classification
classification = classify_call_category(transcript)
print(f"Category: {classification['primary_category']}")
print(f"Confidence: {classification['confidence_score']}%")

# Full report
report = generate_classification_report(transcript)
print(report)
```

## Call Categories & Examples

### 1. Billing
- Questions about invoices and charges
- Payment difficulties
- Pricing inquiries
- Dispute resolution

### 2. Technical Support
- Network connectivity issues
- WiFi/internet problems
- Service disruptions
- Troubleshooting requests

### 3. Account Management
- Address or contact information updates
- Plan modifications
- Account status inquiries
- Service changes

### 4. Customer Service
- General complaints
- Service quality issues
- General inquiries
- Escalation requests

### 5. Retention
- Cancellation requests
- Competitor comparisons
- Special offers to retain customers
- Upgrade negotiations

### 6. Sales
- Plan upgrades
- New service purchases
- Promotional offers
- Service additions

### 7. Refund
- Refund requests
- Credit applications
- Compensation requests
- Billing error corrections

### 8. Fraud
- Suspicious account activity
- Security concerns
- Unauthorized charges
- Identity verification

## Sample Calls Included

The project includes 8 diverse sample transcripts covering all categories:
1. Technical Support - Network Issue
2. Retention - Cancellation Request
3. Billing - Overcharge Issue
4. Sales - Upgrade Request
5. Account Management - Address Update
6. Refund - Unauthorized Charges
7. Fraud Detection - Suspicious Activity
8. Customer Service - General Complaint

## Classification Output

Each classification includes:
- **Primary Category**: The main issue category
- **Category Description**: Detailed description of the category
- **Confidence Score**: Confidence percentage (0-100%)
- **Department Recommendation**: Where the call should be routed
- **Sentiment**: Overall tone (Positive, Negative, Neutral)
- **Urgency Level**: Priority level (Low, Medium, High)
- **Key Information**: Extracted services, issues, and requests

## Configuration

### Environment Variables (.env)
```
OPENAI_API_KEY=your_api_key_here
```

### Customization

To customize categories, modify [tools/classification_tools.py](tools/classification_tools.py):

```python
CALL_CATEGORIES = {
    "your_category": "Category description",
    ...
}
```

Update keywords for classification in the `classify_call_category()` function.

## Performance Considerations

- **Quick Test**: ~1-2 seconds per call (no API)
- **Full Crew Analysis**: ~15-30 seconds per call (requires OpenAI API)
- **Batch Processing**: Can process multiple calls sequentially

## Troubleshooting

### Missing API Key
If you see: "OPENAI_API_KEY environment variable not set"
1. Copy `.env.example` to `.env`
2. Add your OpenAI API key
3. Run again

### Dependency Issues
```bash
pip install --upgrade -r requirements.txt
```

### Import Errors
Ensure you're running from the project root directory and have activated the virtual environment.

## Future Enhancements

- Integration with live call recording APIs
- Speech-to-text transcript generation
- Real-time call routing
- Machine learning model fine-tuning
- Multi-language support
- Integration with Verizon CRM systems
- Emotion detection enhancements
- Custom callback routing logic

## API Requirements

- **OpenAI API**: Required for full Crew AI analysis
- **Crew AI Framework**: Orchestrates agents and tasks
- **Python 3.9+**: Runtime environment

## License

This project is provided as-is for educational and business use.

## Support

For issues or questions, refer to:
- [Crew AI Documentation](https://docs.crewai.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- Project code comments and examples

## Version History

- **v1.0** (January 2026): Initial release with 8 call categories, 4 agents, classification tools
