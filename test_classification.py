"""Quick test script for call classification without full Crew AI."""

from tools.classification_tools import (
    classify_call_category,
    analyze_call_transcript,
    extract_customer_info,
    generate_classification_report
)


def test_classification():
    """Test the classification tools."""
    
    # Sample customer call transcripts
    test_calls = [
        {
            "name": "Technical Support Call",
            "transcript": """
            Customer: Hi, I've been having issues with my internet connection for the past week. 
            It keeps dropping and my speed is very slow.
            Agent: I'm sorry to hear that. Let me help you troubleshoot.
            Customer: It's affecting my work. I need this fixed urgently!
            Agent: Let me escalate this to our technical team.
            """
        },
        {
            "name": "Billing Inquiry",
            "transcript": """
            Customer: Hi, I have a question about my bill. I was charged $150 but I expected $100.
            Agent: Let me review your account.
            Customer: This is the second time there's been an error.
            Agent: I sincerely apologize. Let me correct this for you immediately.
            """
        },
        {
            "name": "Retention/Cancellation",
            "transcript": """
            Customer: I want to cancel my service. I'm switching to another provider.
            Agent: I'm sorry to hear you want to leave.
            Customer: Your prices are too high compared to competitors.
            Agent: Let me see what special offers I can provide to keep you as a valued customer.
            """
        },
        {
            "name": "Account Management",
            "transcript": """
            Customer: I need to update my account information. I moved to a new address.
            Agent: Of course! I'll help you with that.
            Customer: Also, can I upgrade my plan?
            Agent: Absolutely, let me show you our available options.
            """
        },
        {
            "name": "Sales/Upgrade",
            "transcript": """
            Customer: I'd like to get faster internet for my home office.
            Agent: Great! Our fiber optic service would be perfect for you.
            Customer: What speeds can you offer?
            Agent: We can provide speeds up to 940 Mbps!
            Customer: Sounds good, let's upgrade!
            """
        }
    ]
    
    print("="*80)
    print("ABC TELECOM CUSTOMER CALL CLASSIFICATION TEST")
    print("="*80)
    
    for i, test_call in enumerate(test_calls, 1):
        print(f"\n\nTest {i}: {test_call['name']}")
        print("-" * 80)
        
        transcript = test_call['transcript']
        
        # Analyze the transcript
        print("\n1. ANALYZING CALL...")
        analysis = analyze_call_transcript(transcript)
        print(f"   Sentiment: {analysis['sentiment']}")
        print(f"   Duration: {analysis['duration_estimate']}")
        print(f"   Topics: {', '.join(analysis['key_topics'])}")
        print(f"   Urgency: {analysis['urgency_level']}")
        
        # Extract customer info
        print("\n2. EXTRACTING CUSTOMER INFO...")
        customer_info = extract_customer_info(transcript)
        print(f"   Services: {', '.join(customer_info['mentioned_services']) if customer_info['mentioned_services'] else 'None'}")
        print(f"   Issues: {', '.join(customer_info['issues_reported']) if customer_info['issues_reported'] else 'None'}")
        print(f"   Requests: {', '.join(customer_info['requests']) if customer_info['requests'] else 'None'}")
        
        # Classify the call
        print("\n3. CLASSIFYING CALL...")
        classification = classify_call_category(transcript, analysis)
        print(f"   Primary Category: {classification['primary_category'].upper()}")
        print(f"   Description: {classification['category_description']}")
        print(f"   Confidence: {classification['confidence_score']}%")
        print(f"   Recommendation: {classification['recommendation']}")
        
        # Category scores
        print(f"\n   Category Scores:")
        for category, score in sorted(classification['all_scores'].items(), key=lambda x: x[1], reverse=True):
            print(f"     - {category}: {score}")
        
        # Generate full report
        print("\n4. FULL CLASSIFICATION REPORT...")
        report = generate_classification_report(transcript)
        print(report)
        
        print("\n" + "="*80)


if __name__ == "__main__":
    test_classification()
    print("\n✅ Classification testing complete!")
