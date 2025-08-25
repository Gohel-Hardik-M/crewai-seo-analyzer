from flask import Flask, render_template, request, make_response
from crewai import Agent, Task, Crew, Process
import os
import litellm

app = Flask(__name__)


# Environment Setup

os.environ["OPENROUTER_API_KEY"] = "YOUR_OPENROUTER_API_KEY"
os.environ["LITELLM_PROVIDER"] = "openrouter"  
MODEL_NAME = "openrouter/mistralai/mistral-7b-instruct"


# Route Setup

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            report = generate_seo_report(url)
            return render_template('report.html', url=url, report=report)
        except Exception as e:
            return render_template('report.html', url=url, report=f"Error: {str(e)}")
    return render_template('index.html')




# SEO Report via CrewAI
def generate_seo_report(target_url):
    # Agents
    research_agent = Agent(
        role="SEO Researcher",
        goal="Scrape website content and extract useful SEO-related data",
        backstory="You are an SEO analyst who collects data about websites for optimization.",
        llm=MODEL_NAME,
        verbose=True,
    )

    analysis_agent = Agent(
        role="SEO Analyst",
        goal="Analyze website text for SEO quality and ranking potential",
        backstory="You are an expert in SEO analysis and can provide keyword and structure suggestions.",
        llm=MODEL_NAME,
        verbose=True,
    )

    report_agent = Agent(
        role="SEO Report Generator",
        goal="Summarize findings into an SEO report with recommendations",
        backstory="You create easy-to-read SEO reports for website owners.",
        llm=MODEL_NAME,
        verbose=True,
    )

    # Tasks
    task1 = Task(
        description=f"Scrape and summarize text from the target URL: {target_url}",
        expected_output="A clean summary of webpage text content.",
        agent=research_agent,
    )

    task2 = Task(
        description="Analyze the text for SEO performance. Look at keywords, headings, meta descriptions, internal links.",
        expected_output="SEO analysis covering strengths, weaknesses, and possible improvements.",
        agent=analysis_agent,
    )

    task3 = Task(
        description="Create a structured SEO report with recommendations.",
        expected_output="Final report in bullet points with clear, actionable SEO tips.",
        agent=report_agent,
    )

    # Crew
    crew = Crew(
        agents=[research_agent, analysis_agent, report_agent],
        tasks=[task1, task2, task3],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return result


if __name__ == '__main__':
    app.run(debug=True)

