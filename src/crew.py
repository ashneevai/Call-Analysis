"""Crew AI Crew configuration for customer call analysis."""

from crewai import Crew, Process
from .agents import (
    create_call_analyzer_agent,
    create_call_classifier_agent,
    create_quality_assurance_agent,
    create_action_plan_agent
)
from .tasks import (
    create_analysis_task,
    create_classification_task,
    create_qa_review_task,
    create_action_plan_task
)


def create_customer_call_crew() -> Crew:
    """Create and configure the customer call analysis crew."""
    
    # Create agents
    analyzer_agent = create_call_analyzer_agent()
    classifier_agent = create_call_classifier_agent()
    qa_agent = create_quality_assurance_agent()
    action_agent = create_action_plan_agent()
    
    # Create tasks
    analysis_task = create_analysis_task()
    classification_task = create_classification_task()
    qa_task = create_qa_review_task()
    action_task = create_action_plan_task()
    
    # Create crew
    crew = Crew(
        agents=[analyzer_agent, classifier_agent, qa_agent, action_agent],
        tasks=[analysis_task, classification_task, qa_task, action_task],
        process=Process.sequential,
        verbose=True
    )
    
    return crew


def create_quick_classification_crew() -> Crew:
    """Create a lightweight crew for quick classification without full QA."""
    
    # Create agents
    analyzer_agent = create_call_analyzer_agent()
    classifier_agent = create_call_classifier_agent()
    
    # Create tasks
    analysis_task = create_analysis_task()
    classification_task = create_classification_task()
    
    # Create crew
    crew = Crew(
        agents=[analyzer_agent, classifier_agent],
        tasks=[analysis_task, classification_task],
        process=Process.sequential,
        verbose=True
    )
    
    return crew
