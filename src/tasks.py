"""Crew AI Tasks for customer call classification."""

from crewai import Task
from .agents import (
    create_call_analyzer_agent,
    create_call_classifier_agent,
    create_quality_assurance_agent,
    create_action_plan_agent
)


def create_analysis_task() -> Task:
    """Create task for analyzing customer calls."""
    return Task(
        description="""Analyze the following customer call transcript:
        {call_transcript}
        
        Extract and report on:
        1. Overall sentiment and emotional state
        2. Key topics and issues mentioned
        3. Services discussed (mobile, internet, TV, etc.)
        4. Specific problems or requests
        5. Urgency indicators
        6. Any red flags or special circumstances""",
        expected_output="""A comprehensive analysis including:
        - Customer sentiment assessment
        - Key topics identified
        - Services involved
        - Critical issues
        - Urgency level
        - Notable observations""",
        agent=create_call_analyzer_agent()
    )


def create_classification_task() -> Task:
    """Create task for classifying calls into categories."""
    return Task(
        description="""Based on the customer call analysis, classify the call into one of these categories:
        - Billing (invoices, payments, pricing)
        - Technical Support (network, connectivity issues)
        - Account Management (plan changes, account info)
        - Customer Service (general inquiries, complaints)
        - Retention (cancellation prevention, retention offers)
        - Sales (upgrades, new services)
        - Refund (refunds, credits, compensation)
        - Fraud (fraud detection, security)
        
        Call transcript: {call_transcript}
        
        Provide:
        1. Primary category classification
        2. Confidence score
        3. Reasoning for the classification
        4. Secondary categories if applicable
        5. Recommended department routing""",
        expected_output="""Classification results including:
        - Primary category with description
        - Confidence percentage
        - Clear reasoning
        - Alternative categories considered
        - Department recommendation""",
        agent=create_call_classifier_agent()
    )


def create_qa_review_task() -> Task:
    """Create task for quality assurance review."""
    return Task(
        description="""Review the call analysis and classification for quality and compliance.
        
        Evaluate:
        1. Accuracy of the classification
        2. Compliance with Verizon standards
        3. Customer satisfaction indicators
        4. Risk factors or escalation needs
        5. Data quality and completeness
        
        Call details:
        - Transcript: {call_transcript}
        - Analysis: {analysis_result}
        - Classification: {classification_result}""",
        expected_output="""QA Review Report with:
        - Accuracy assessment
        - Compliance status
        - Risk level
        - Required escalations
        - Recommendations for improvement""",
        agent=create_quality_assurance_agent()
    )


def create_action_plan_task() -> Task:
    """Create task for developing action plans."""
    return Task(
        description="""Create a comprehensive action plan for handling this customer call.
        
        Based on the analysis and classification:
        1. Identify immediate actions needed
        2. Specify which department should handle this
        3. Recommend follow-up actions
        4. Set timeline for resolution
        5. Identify any escalation needs
        6. Suggest retention strategies if applicable
        
        Call context:
        - Classification: {classification_result}
        - Analysis: {analysis_result}
        - QA Review: {qa_result}""",
        expected_output="""Action Plan including:
        - Immediate actions (within 24 hours)
        - Primary responsible department
        - Follow-up schedule
        - Resolution timeline
        - Escalation procedures if needed
        - Customer retention strategy
        - Success metrics""",
        agent=create_action_plan_agent()
    )
