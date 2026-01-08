"""Sample call transcripts for testing and demonstration."""

import json


SAMPLE_TRANSCRIPTS = [
    {
        "id": 1,
        "name": "Technical Support - Network Issue",
        "category": "technical_support",
        "transcript": """
        Customer: Hi, I've been having issues with my internet connection for the past week. 
        It keeps dropping and my speed is very slow.
        Agent: I'm sorry to hear that. Let me help you troubleshoot. Are you using WiFi or a wired connection?
        Customer: I'm using WiFi on my phone and laptop. It was working fine before.
        Agent: Can you restart your router and try again?
        Customer: Already did that twice. It's not helping. This is really frustrating!
        Agent: I understand your frustration. Let me escalate this to our technical support team.
        Customer: How long will this take? I need internet for my work.
        Agent: We'll have someone contact you within 24 hours to resolve this.
        """
    },
    {
        "id": 2,
        "name": "Retention - Cancellation Request",
        "category": "retention",
        "transcript": """
        Customer: Hi, I want to cancel my service. I found a better deal with another provider.
        Agent: I'm sorry to hear you want to leave us! May I ask what's the main reason?
        Customer: Your prices are too high. The competitor is offering 30% discount on their plans.
        Agent: I understand price is important. Let me check what special offers I can provide for you.
        Customer: Well, if you can match the price or offer something comparable, I might reconsider.
        Agent: Let me look into our loyalty programs. Can you give me a moment?
        Customer: Sure, but I need to make a decision today.
        Agent: I found a 6-month promotional rate that could save you significantly.
        """
    },
    {
        "id": 3,
        "name": "Billing - Overcharge Issue",
        "category": "billing",
        "transcript": """
        Customer: I have a question about my bill. I was charged twice this month!
        Agent: I sincerely apologize for the confusion. Let me look into your account right away.
        Customer: This is the second time this happened in three months. I'm very unhappy.
        Agent: I completely understand your frustration. Let me investigate this immediately.
        Customer: I need a refund for the extra charge plus some compensation.
        Agent: You're absolutely right. I'll process the refund immediately and add a $50 credit to your account.
        Customer: Thank you. I appreciate you handling this quickly.
        Agent: Is there anything else I can help you with?
        """
    },
    {
        "id": 4,
        "name": "Sales - Upgrade Request",
        "category": "sales",
        "transcript": """
        Customer: I'd like to upgrade my mobile plan. I need more data for my work from home.
        Agent: Great! That's a smart choice. Let me check what plans would work best for you.
        Customer: I'm currently on the basic plan with 5GB. I need at least 20GB monthly.
        Agent: Perfect, we have several premium plans that would be ideal for your needs.
        Customer: What's the pricing difference?
        Agent: Our premium plans start at $79.99 per month for unlimited data.
        Customer: That's too expensive. What else do you have?
        Agent: We have a mid-tier plan at $59.99 with 50GB, which might fit your needs.
        Customer: That sounds better. Let's go with that.
        """
    },
    {
        "id": 5,
        "name": "Account Management - Address Update",
        "category": "account_management",
        "transcript": """
        Customer: I need to update my account information. I've moved to a new address.
        Agent: Of course! I'll be happy to help you with that. What's your new address?
        Customer: It's 123 Main Street, New York, NY 10001, Apartment 5B.
        Agent: Thank you! I've updated your information in the system.
        Customer: Also, while we're at it, I'd like to change my billing date to the 15th of the month.
        Agent: No problem. I can take care of that for you.
        Customer: Great! Is there anything else I should know?
        Agent: Your service will continue uninterrupted at the new address.
        """
    },
    {
        "id": 6,
        "name": "Refund - Unauthorized Charges",
        "category": "refund",
        "transcript": """
        Customer: I want to dispute a charge on my account. I was charged for roaming data but I wasn't traveling.
        Agent: I apologize for that. Let me review your account to investigate.
        Customer: I travel rarely, so this charge doesn't make sense.
        Agent: You're right. I can see the charge was made. Let me process a refund for you.
        Customer: How long will it take to get my money back?
        Agent: The refund will appear in your account within 5-7 business days.
        Customer: Thank you for taking care of this quickly.
        """
    },
    {
        "id": 7,
        "name": "Fraud Detection - Suspicious Activity",
        "category": "fraud",
        "transcript": """
        Customer: I'm calling because I see a new device on my account that I didn't authorize.
        Agent: Thank you for alerting us. This is very important. Can you describe the device?
        Customer: There's an iPad that was added yesterday. I definitely didn't do that.
        Agent: I'm taking this seriously. Let me disable that device immediately and secure your account.
        Customer: Is my account safe? Could they have accessed my personal information?
        Agent: We'll review the access logs. Please change your password immediately.
        Customer: Should I be concerned about identity theft?
        Agent: Let me transfer you to our fraud prevention team for a full security review.
        """
    },
    {
        "id": 8,
        "name": "Customer Service - General Complaint",
        "category": "customer_service",
        "transcript": """
        Customer: I need to speak to a supervisor. I'm very disappointed with my service quality.
        Agent: I'm sorry to hear you're unhappy. What specific issues have you experienced?
        Customer: The service has been inconsistent, and I had to call three times last week to resolve issues.
        Agent: I sincerely apologize for the inconvenience. Let me escalate this to a supervisor.
        Customer: I want something done about this. I've been a customer for 5 years.
        Agent: Your loyalty means a lot to us. Let me get a supervisor on the line right now.
        """
    }
]


def get_sample_transcripts():
    """Return all sample transcripts."""
    return SAMPLE_TRANSCRIPTS


def get_transcript_by_id(transcript_id: int):
    """Get a specific transcript by ID."""
    for transcript in SAMPLE_TRANSCRIPTS:
        if transcript['id'] == transcript_id:
            return transcript
    return None


def get_transcripts_by_category(category: str):
    """Get all transcripts in a specific category."""
    return [t for t in SAMPLE_TRANSCRIPTS if t['category'] == category]


def save_transcripts_to_file(filepath: str):
    """Save sample transcripts to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(SAMPLE_TRANSCRIPTS, f, indent=2)


if __name__ == "__main__":
    print("Sample Transcripts Available:")
    print("=" * 80)
    for transcript in SAMPLE_TRANSCRIPTS:
        print(f"\nID: {transcript['id']}")
        print(f"Name: {transcript['name']}")
        print(f"Category: {transcript['category']}")
        print(f"Preview: {transcript['transcript'][:100]}...")
