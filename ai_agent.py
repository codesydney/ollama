from crewai import Agent, Task, Crew
import os

# Create a simple agent with direct model reference
math_agent = Agent(
    role="Math Expert",
    goal="Solve mathematical problems and explain the solutions clearly",
    backstory="""You are an experienced mathematics teacher who excels at 
    breaking down complex problems into simple steps. You enjoy helping
    students understand mathematical concepts.""",
    allow_delegation=False,
    verbose=True,
    llm="ollama/gemma2:2b"  # Directly specify the model
)

# Create a task for the agent
math_task = Task(
    description="What is 152 * 71 and can you explain how you solved it?",
    agent=math_agent,
    expected_output="The answer with a clear explanation of the multiplication process."
)

# Create a crew with the agent and task
crew = Crew(
    agents=[math_agent],
    tasks=[math_task],
    verbose=True
)

# Run the crew and get the result
result = crew.kickoff()
print("\nResult:")
print(result)