"""Tools for customer call classification and analysis."""

from typing import Dict, List
import json

# Define call categories for ABC Telecom
CALL_CATEGORIES = {
    "billing": "Billing, payments, invoices, and pricing inquiries",
    "technical_support": "Network issues, connectivity problems, service troubleshooting",
    "account_management": "Account changes, plan modifications, account information",
    "customer_service": "General inquiries, complaints, escalations",
    "retention": "Cancellation prevention, upgrade offers, loyalty programs",
    "sales": "New service sales, plan upgrades, promotional offers",
    "refund": "Refund requests, credits, compensation",
    "fraud": "Fraud detection, security concerns, identity verification"
}


def analyze_call_transcript(transcript: str) -> Dict:
    """
    Analyze a customer call transcript to extract key information.
    
    Args:
        transcript: The customer call transcript text
        
    Returns:
        Dictionary containing analysis results
    """
    analysis = {
        "sentiment": detect_sentiment(transcript),
        "duration_estimate": estimate_duration(transcript),
        "key_topics": extract_topics(transcript),
        "urgency_level": assess_urgency(transcript)
    }
    return analysis


def classify_call_category(transcript: str, analysis: Dict = None) -> Dict:
    """
    Classify a customer call into one of the predefined categories.
    
    Args:
        transcript: The customer call transcript
        analysis: Optional analysis results
        
    Returns:
        Classification result with category and confidence
    """
    keywords = {
        "billing": ["bill", "payment", "invoice", "charge", "cost", "price", "amount", "balance"],
        "technical_support": ["connection", "network", "wifi", "signal", "not working", "issue", "problem", "error"],
        "account_management": ["account", "plan", "change", "update", "modify", "information"],
        "customer_service": ["complaint", "issue", "help", "support", "problem", "service"],
        "retention": ["cancel", "leave", "switch", "competitor", "deal", "offer"],
        "sales": ["upgrade", "new", "package", "plan", "buy", "purchase", "offer"],
        "refund": ["refund", "credit", "compensation", "return", "money back"],
        "fraud": ["fraud", "security", "unauthorized", "suspicious", "identity", "verification"]
    }
    
    transcript_lower = transcript.lower()
    category_scores = {}
    
    for category, keywords_list in keywords.items():
        score = sum(1 for keyword in keywords_list if keyword in transcript_lower)
        category_scores[category] = score
    
    # Get category with highest score
    primary_category = max(category_scores, key=category_scores.get)
    confidence = min(category_scores[primary_category] / max(1, sum(category_scores.values())) * 100, 100)
    
    return {
        "primary_category": primary_category,
        "category_description": CALL_CATEGORIES[primary_category],
        "confidence_score": round(confidence, 2),
        "all_scores": category_scores,
        "recommendation": f"This call should be routed to the {primary_category.replace('_', ' ').title()} department"
    }


def extract_customer_info(transcript: str) -> Dict:
    """
    Extract customer information from the transcript.
    
    Args:
        transcript: The customer call transcript
        
    Returns:
        Extracted customer information
    """
    info = {
        "mentioned_services": extract_services(transcript),
        "issues_reported": extract_issues(transcript),
        "requests": extract_requests(transcript),
        "sentiment_markers": extract_sentiment_indicators(transcript)
    }
    return info


def generate_classification_report(transcript: str) -> str:
    """
    Generate a comprehensive classification report for a customer call.
    
    Args:
        transcript: The customer call transcript
        
    Returns:
        Formatted report string
    """
    analysis = analyze_call_transcript(transcript)
    classification = classify_call_category(transcript, analysis)
    customer_info = extract_customer_info(transcript)
    
    report = f"""
CUSTOMER CALL CLASSIFICATION REPORT
====================================

CLASSIFICATION RESULT:
- Primary Category: {classification['primary_category'].upper()}
- Category Description: {classification['category_description']}
- Confidence Score: {classification['confidence_score']}%
- Department Recommendation: {classification['recommendation']}

ANALYSIS SUMMARY:
- Sentiment: {analysis['sentiment']}
- Urgency Level: {analysis['urgency_level']}
- Estimated Call Duration: {analysis['duration_estimate']}

KEY INFORMATION:
- Mentioned Services: {', '.join(customer_info['mentioned_services']) if customer_info['mentioned_services'] else 'None identified'}
- Issues Reported: {', '.join(customer_info['issues_reported']) if customer_info['issues_reported'] else 'None reported'}
- Customer Requests: {', '.join(customer_info['requests']) if customer_info['requests'] else 'No specific requests'}

SENTIMENT INDICATORS:
{chr(10).join([f'  - {indicator}' for indicator in customer_info['sentiment_markers']]) if customer_info['sentiment_markers'] else '  - Neutral tone detected'}

ACTION ITEMS:
- Priority Level: {classification['confidence_score']}%
- Next Steps: Route to {classification['primary_category'].replace('_', ' ').title()} department for further handling
"""
    return report


def detect_sentiment(transcript: str) -> str:
    """Detect sentiment from transcript."""
    transcript_lower = transcript.lower()
    negative_words = ["angry", "frustrated", "unhappy", "disappointed", "problem", "issue", "not working"]
    positive_words = ["happy", "satisfied", "grateful", "thanks", "appreciate", "working fine"]
    
    negative_count = sum(1 for word in negative_words if word in transcript_lower)
    positive_count = sum(1 for word in positive_words if word in transcript_lower)
    
    if negative_count > positive_count:
        return "Negative"
    elif positive_count > negative_count:
        return "Positive"
    else:
        return "Neutral"


def estimate_duration(transcript: str) -> str:
    """Estimate call duration based on transcript length."""
    word_count = len(transcript.split())
    if word_count < 100:
        return "Short (< 5 minutes)"
    elif word_count < 300:
        return "Medium (5-15 minutes)"
    else:
        return "Long (> 15 minutes)"


def extract_topics(transcript: str) -> List[str]:
    """Extract main topics from transcript."""
    topics = []
    topic_keywords = {
        "billing": ["bill", "payment", "invoice", "charge"],
        "network": ["network", "wifi", "signal", "connection"],
        "plan": ["plan", "package", "service"],
        "outage": ["down", "outage", "not working"]
    }
    
    transcript_lower = transcript.lower()
    for topic, keywords in topic_keywords.items():
        if any(keyword in transcript_lower for keyword in keywords):
            topics.append(topic)
    
    return topics if topics else ["general"]


def assess_urgency(transcript: str) -> str:
    """Assess urgency level of the call."""
    transcript_lower = transcript.lower()
    urgent_keywords = ["urgent", "immediately", "asap", "emergency", "critical", "down"]
    
    if any(keyword in transcript_lower for keyword in urgent_keywords):
        return "High"
    elif any(word in transcript_lower for word in ["problem", "issue"]):
        return "Medium"
    else:
        return "Low"


def extract_services(transcript: str) -> List[str]:
    """Extract mentioned services."""
    services = []
    service_keywords = {
        "mobile": ["mobile", "phone", "cellular", "wireless"],
        "internet": ["internet", "broadband", "wifi", "data"],
        "tv": ["tv", "television", "cable", "streaming"],
        "home": ["home", "residential", "fios"],
        "business": ["business", "corporate", "enterprise"]
    }
    
    transcript_lower = transcript.lower()
    for service, keywords in service_keywords.items():
        if any(keyword in transcript_lower for keyword in keywords):
            services.append(service)
    
    return services


def extract_issues(transcript: str) -> List[str]:
    """Extract reported issues."""
    issues = []
    issue_keywords = {
        "connectivity": ["no signal", "no connection", "can't connect", "wifi down"],
        "billing": ["wrong charge", "overcharge", "unexpected bill"],
        "speed": ["slow", "buffering", "lag"],
        "outage": ["service down", "outage", "not working"]
    }
    
    transcript_lower = transcript.lower()
    for issue, keywords in issue_keywords.items():
        if any(keyword in transcript_lower for keyword in keywords):
            issues.append(issue)
    
    return issues


def extract_requests(transcript: str) -> List[str]:
    """Extract customer requests."""
    requests = []
    request_keywords = {
        "discount": ["discount", "reduce", "lower price"],
        "upgrade": ["upgrade", "faster", "more data"],
        "cancel": ["cancel", "stop service", "leave"],
        "credit": ["credit", "refund", "compensation"],
        "technician": ["technician", "repair", "fix it"]
    }
    
    transcript_lower = transcript.lower()
    for request, keywords in request_keywords.items():
        if any(keyword in transcript_lower for keyword in keywords):
            requests.append(request)
    
    return requests


def extract_sentiment_indicators(transcript: str) -> List[str]:
    """Extract sentiment indicators from transcript."""
    indicators = []
    
    if any(word in transcript.lower() for word in ["angry", "frustrated", "upset"]):
        indicators.append("Customer showing frustration")
    if any(word in transcript.lower() for word in ["thank", "appreciate", "thanks"]):
        indicators.append("Customer expressing gratitude")
    if any(word in transcript.lower() for word in ["urgent", "immediately", "asap"]):
        indicators.append("Time-sensitive issue")
    if any(word in transcript.lower() for word in ["first time", "repeat", "again"]):
        indicators.append("Potential repeat issue")
    
    return indicators
