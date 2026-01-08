"""Crew AI Agents for customer call analysis."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crewai import Agent
from tools.classification_tools import (
    analyze_call_transcript,
    classify_call_category,
    extract_customer_info,
    generate_classification_report
)


def create_call_analyzer_agent() -> Agent:
    """Create an agent that analyzes customer call transcripts."""
    return Agent(
        role="Customer Call Analyst",
        goal="Analyze customer call transcripts to understand customer needs, issues, and sentiment",
        backstory="""You are an experienced ABC Telecom customer service analyst with 10+ years 
        of experience. You excel at understanding customer concerns, extracting key information, 
        and assessing the overall sentiment and urgency of customer calls. You have deep knowledge 
        of Verizon services including mobile, internet, TV, and business solutions.""",
        verbose=True,
        allow_delegation=False
    )


def create_call_classifier_agent() -> Agent:
    """Create an agent that classifies calls into categories."""
    return Agent(
        role="Call Category Classifier",
        goal="Classify customer calls into appropriate service categories for proper routing and handling",
        backstory="""You are an expert at categorizing customer service calls for a major telecom provider. 
        With a deep understanding of customer service operations, you can quickly identify the primary issue 
        in a call and classify it correctly. You know all the different departments and their specialties: 
        billing, technical support, account management, customer service, retention, sales, refunds, 
        and fraud prevention.""",
        verbose=True,
        allow_delegation=False
    )


def create_quality_assurance_agent() -> Agent:
    """Create an agent for quality assurance and compliance review."""
    return Agent(
        role="Quality Assurance & Compliance Officer",
        goal="Review classified calls for accuracy, compliance, and customer satisfaction indicators",
        backstory="""You are a senior QA manager at Verizon with responsibility for ensuring all customer 
        interactions meet quality standards and compliance requirements. You review call classifications, 
        ensure proper handling procedures were followed, and identify opportunities for improvement. 
        You understand regulatory requirements and customer satisfaction metrics.""",
        tools=[],
        verbose=True,
        allow_delegation=False
    )


def create_action_plan_agent() -> Agent:
    """Create an agent that recommends next steps and actions."""
    return Agent(
        role="Customer Action Plan Coordinator",
        goal="Create comprehensive action plans and recommendations based on call analysis and classification",
        backstory="""You are an experienced customer success coordinator at Verizon who specializes in 
        creating actionable plans for different types of customer interactions. You understand follow-up 
        procedures, escalation paths, and how to ensure customer satisfaction. You know which departments 
        need to be involved and what timelines are appropriate for different issue types.""",
        tools=[],
        verbose=True,
        allow_delegation=False
    )
