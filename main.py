"""Main application for Verizon Customer Call Analysis using Crew AI."""

import os
from dotenv import load_dotenv
from src.crew import create_customer_call_crew, create_quick_classification_crew
from tools.classification_tools import generate_classification_report

# Load environment variables
load_dotenv()


def classify_single_call(transcript: str, quick_mode: bool = False) -> dict:
    """
    Classify a single customer call transcript.
    
    Args:
        transcript: Customer call transcript text
        quick_mode: If True, use faster classification without full QA
        
    Returns:
        Dictionary with classification results
    """
    print("\n" + "="*70)
    print("VERIZON CUSTOMER CALL ANALYSIS & CLASSIFICATION")
    print("="*70)
    
    if quick_mode:
        print("\nMode: Quick Classification (Analysis + Classification)")
        crew = create_quick_classification_crew()
    else:
        print("\nMode: Full Analysis (Analysis + Classification + QA + Action Plan)")
        crew = create_customer_call_crew()
    
    print("\nProcessing call transcript...")
    print("-" * 70)
    
    inputs = {
        "call_transcript": transcript,
        "analysis_result": "",
        "classification_result": "",
        "qa_result": ""
    }
    
    try:
        # Run the crew
        result = crew.kickoff(inputs=inputs)
        
        # Generate detailed report
        report = generate_classification_report(transcript)
        
        print("\n" + report)
        
        return {
            "status": "success",
            "result": str(result),
            "report": report
        }
    except Exception as e:
        print(f"\nError during processing: {str(e)}")
        return {
            "status": "error",
            "error": str(e)
        }


def batch_classify_calls(transcripts: list, quick_mode: bool = False) -> list:
    """
    Classify multiple customer calls in batch.
    
    Args:
        transcripts: List of transcript strings
        quick_mode: If True, use faster classification
        
    Returns:
        List of classification results
    """
    results = []
    
    for i, transcript in enumerate(transcripts, 1):
        print(f"\n\n{'='*70}")
        print(f"Processing Call {i} of {len(transcripts)}")
        print(f"{'='*70}")
        
        result = classify_single_call(transcript, quick_mode)
        results.append({
            "call_number": i,
            "result": result
        })
    
    return results


def main():
    """Main entry point for the application."""
    
    # Sample customer call transcripts for Verizon
    sample_calls = [
        """
        Customer: Hi, I've been having issues with my internet connection for the past week. 
        It keeps dropping and my speed is very slow.
        Agent: I'm sorry to hear that. Let me help you troubleshoot. Are you using WiFi or a wired connection?
        Customer: I'm using WiFi on my phone. It was working fine before.
        Agent: Can you restart your router and try again?
        Customer: Already did that twice. It's not helping.
        Agent: I understand your frustration. Let me escalate this to our technical support team.
        """,
        
        """
        Customer: Hi, I want to cancel my service. I found a better deal with another provider.
        Agent: I'm sorry to hear you want to leave us! May I ask what's the main reason?
        Customer: Your prices are too high. Competitor is offering 30% discount.
        Agent: Let me see what I can do. We have loyalty programs and special offers for valued customers.
        Customer: Well, if you can match the price, I might reconsider.
        Agent: Let me check what we can offer for you.
        """,
        
        """
        Customer: I have a question about my bill. I was charged twice this month!
        Agent: I apologize for the confusion. Let me look into your account.
        Customer: This is the second time this happened. I'm not happy.
        Agent: I understand. Let me investigate and ensure this is corrected immediately.
        Customer: You need to refund me the extra charge.
        Agent: Absolutely, I'll process that refund for you right away.
        """,
        
        """
        Customer: I'd like to upgrade my mobile plan. I need more data for work.
        Agent: Great! Let me check what plans would work best for you.
        Customer: I'm currently on the basic plan with 5GB. I need at least 20GB.
        Agent: Perfect, we have plans that would be ideal for your needs.
        Customer: What's the pricing?
        Agent: Our premium plans start at $79.99 per month for unlimited data.
        """,
        
        """
        Customer: I need to update my account information. I moved to a new address.
        Agent: Of course! I can help you with that. What's your new address?
        Customer: It's 123 Main Street, New York, NY 10001.
        Agent: Thank you. I've updated your information in the system.
        Customer: Also, can I change my plan while we're at it?
        Agent: Absolutely, what changes would you like?
        """
    ]
    
    print("Starting ABC Telecom Customer Call Classification System")
    print("=" * 70)
    
    # Classify all sample calls
    results = batch_classify_calls(sample_calls, quick_mode=True)
    
    # Print summary
    print("\n\n" + "="*70)
    print("BATCH PROCESSING SUMMARY")
    print("="*70)
    print(f"Total calls processed: {len(results)}")
    for result in results:
        status = result['result'].get('status', 'unknown')
        print(f"Call {result['call_number']}: {status.upper()}")


if __name__ == "__main__":
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  WARNING: OPENAI_API_KEY environment variable not set!")
        print("Please add your OpenAI API key to the .env file")
        print("Copy .env.example to .env and add your API key")
        print("\nYou can still test the classification tools without running the full crew.")
    
    # Run main application
    main()
