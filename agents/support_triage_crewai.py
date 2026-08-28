"""Support ticket triage crew."""
from crewai import Agent, Crew, Process, Task

classifier = Agent(
    role="Ticket Classifier",
    goal="Assign each inbound support ticket a category and severity",
    backstory="Ten years on a tier-2 support desk.",
    llm="gpt-4o",
    verbose=True,
)

responder = Agent(
    role="Response Drafter",
    goal="Draft a first response for the customer",
    backstory="Writes clearly and never over-promises.",
    llm="claude-sonnet-4-5-20250929",
)

triage = Task(
    description="Classify ticket {ticket_id} and draft a reply.",
    expected_output="A JSON object with category, severity, and draft_reply.",
    agent=classifier,
)

crew = Crew(
    agents=[classifier, responder],
    tasks=[triage],
    process=Process.sequential,
)

if __name__ == "__main__":
    print(crew.kickoff(inputs={"ticket_id": "CS-1001"}))
