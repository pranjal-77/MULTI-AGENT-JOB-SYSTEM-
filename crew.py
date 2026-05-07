"""
Crew Orchestration - Brings Agents and Tasks Together
This file coordinates the multi-agent workflow
"""

from crewai import Crew, Process
from agents import job_analyst, resume_writer, messaging_specialist
from task import (
    create_task,
    create_resume_task,
    cover_letter,
    create_linkedin_message,
)

def run_job_application_crew(
    job_description,
    company_name,
    job_title,
    user_background,
    hiring_manager="Hiring Manager"
):
    """
    Run the complete job application AI crew
    
    This orchestrates all 3 agents to:
    1. Analyze the job description
    2. Tailor your resume
    3. Write a cover letter  
    4. Draft LinkedIn outreach messages
    
    Args:
        job_description (str): Full text of the job posting
        company_name (str): Name of the company
        job_title (str): Title of the position
        user_background (str): Your experience, skills, and background
        hiring_manager (str): Name of hiring manager (if known)
    
    Returns:
        dict: Results from all tasks
    """
    
    print("\n" + "="*80)
    print("🚀 STARTING JOB APPLICATION AI CREW")
    print("="*80)
    print(f"\n📋 Position: {job_title}")
    print(f"🏢 Company: {company_name}")
    print(f"👤 Hiring Manager: {hiring_manager}")
    print("\n" + "="*80 + "\n")
    
    # Create all tasks
    print("📝 Creating tasks for agents...")
    
    task1_analysis = create_task(
        job_analyst,
        job_description
    )
    
    task2_resume = create_resume_task(
        resume_writer,
        job_description,
        user_background
    )
    
    task3_cover_letter = cover_letter(
        resume_writer,
        job_description,
        company_name,
        user_background
    )
    
    task4_linkedin = create_linkedin_message(
        messaging_specialist,
        company_name,
        job_title,
        hiring_manager,
        user_background
    )
    
    print("✅ Tasks created!\n")
    
    # Assemble the crew
    print("👥 Assembling the crew...")
    
    crew = Crew(
        agents=[job_analyst, resume_writer, messaging_specialist],
        tasks=[task1_analysis, task2_resume, task3_cover_letter, task4_linkedin],
        process=Process.sequential,  # Tasks run one after another
        verbose=True  # Show detailed progress
    )
    
    print("✅ Crew assembled!\n")
    
    # Execute the workflow
    print("🎬 Starting crew execution...")
    print("   (This may take 1-2 minutes - agents are thinking!)\n")
    print("="*80 + "\n")
    
    result = crew.kickoff()
    
    print("\n" + "="*80)
    print("✅ CREW EXECUTION COMPLETE!")
    print("="*80 + "\n")
    
    # Extract results from tasks
    results = {
        "job_analysis": task1_analysis.output.raw_output if hasattr(task1_analysis.output, 'raw_output') else str(task1_analysis.output),
        "tailored_resume": task2_resume.output.raw_output if hasattr(task2_resume.output, 'raw_output') else str(task2_resume.output),
        "cover_letter": task3_cover_letter.output.raw_output if hasattr(task3_cover_letter.output, 'raw_output') else str(task3_cover_letter.output),
        "linkedin_messages": task4_linkedin.output.raw_output if hasattr(task4_linkedin.output, 'raw_output') else str(task4_linkedin.output),
        "full_output": result
    }
    
    return results


def display_results(results):
    """
    Pretty print the crew results
    
    Args:
        results (dict): Output from run_job_application_crew()
    """
    
    print("\n" + "="*80)
    print("📊 RESULTS FROM AI AGENTS")
    print("="*80)
    
    # Job Analysis
    print("\n" + "─"*80)
    print("🔍 JOB ANALYSIS (from Job Analyst)")
    print("─"*80)
    print(results['job_analysis'])
    
    # Tailored Resume
    print("\n" + "─"*80)
    print("📄 TAILORED RESUME (from Resume Writer)")
    print("─"*80)
    print(results['tailored_resume'])
    
    # Cover Letter
    print("\n" + "─"*80)
    print("✉️ COVER LETTER (from Resume Writer)")
    print("─"*80)
    print(results['cover_letter'])
    
    # LinkedIn Messages
    print("\n" + "─"*80)
    print("💼 LINKEDIN MESSAGES (from Messaging Specialist)")
    print("─"*80)
    print(results['linkedin_messages'])
    
    print("\n" + "="*80 + "\n")


def save_results(results, filename_prefix="application"):
    """
    Save results to text files
    
    Args:
        results (dict): Output from run_job_application_crew()
        filename_prefix (str): Prefix for output files
    """
    
    import os
    from datetime import datetime
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save each component
    files_created = []
    
    # Job Analysis
    filename = f"output/{filename_prefix}_{timestamp}_analysis.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("JOB ANALYSIS\n")
        f.write("="*80 + "\n\n")
        f.write(results['job_analysis'])
    files_created.append(filename)
    
    # Resume
    filename = f"output/{filename_prefix}_{timestamp}_resume.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("TAILORED RESUME\n")
        f.write("="*80 + "\n\n")
        f.write(results['tailored_resume'])
    files_created.append(filename)
    
    # Cover Letter
    filename = f"output/{filename_prefix}_{timestamp}_cover_letter.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("COVER LETTER\n")
        f.write("="*80 + "\n\n")
        f.write(results['cover_letter'])
    files_created.append(filename)
    
    # LinkedIn Messages
    filename = f"output/{filename_prefix}_{timestamp}_linkedin.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("LINKEDIN OUTREACH MESSAGES\n")
        f.write("="*80 + "\n\n")
        f.write(results['linkedin_messages'])
    files_created.append(filename)
    
    print(f"\n💾 Saved {len(files_created)} files to ./output/")
    for file in files_created:
        print(f"   ✅ {file}")
    
    return files_created


# ============================================================================
# TEST THE CREW
# ============================================================================

if __name__ == "__main__":
    """
    Test the crew with sample data
    Run: python crew.py
    """
    
    # Sample job description
    sample_job = """
    Senior Python Developer
    Infosys Limited - Bangalore, India
    
    We are seeking an experienced Python Developer to join our digital transformation team.
    
    Key Responsibilities:
    • Design and develop scalable web applications using Python and Django
    • Build RESTful APIs and microservices architecture
    • Work with PostgreSQL databases and optimize query performance
    • Implement CI/CD pipelines and containerization using Docker
    • Collaborate with cross-functional teams in an Agile environment
    • Mentor junior developers and conduct code reviews
    
    Required Skills:
    • 4-6 years of professional Python development experience
    • Strong expertise in Django or Flask frameworks
    • Experience with RESTful API design and development
    • Proficiency in PostgreSQL or MySQL
    • Knowledge of Docker and containerization
    • Understanding of AWS cloud services (EC2, S3, Lambda)
    • Excellent problem-solving and debugging skills
    
    Preferred Skills:
    • Experience with React.js or Angular
    • Knowledge of GraphQL
    • Familiarity with Redis caching
    • Experience with microservices architecture
    
    Education:
    • Bachelor's degree in Computer Science or related field
    
    What We Offer:
    • Competitive salary package (₹12-18 LPA)
    • Health insurance for family
    • Learning and development opportunities
    • Flexible working arrangements
    • Career growth in a Fortune 500 company
    """
    
    # Sample user background
    sample_background = """
   5 years Python development with Django/Flask. Built RESTful APIs for e-commerce.
   Tech stack: Python, Django, PostgreSQL, Redis, Docker, AWS.
   Experience with CI/CD (Jenkins, GitLab) and leading junior developers.
   Bachelor's in Computer Science.
    """
    
    print("\n🧪 TESTING CREW WITH SAMPLE JOB APPLICATION\n")
    
    try:
        # Run the crew
        results = run_job_application_crew(
            job_description=sample_job,
            company_name="Infosys Limited",
            job_title="Senior Python Developer",
            user_background=sample_background,
            hiring_manager="Rajesh Kumar"
        )
        
        # Display results
        display_results(results)
        
        # Save to files
        save_results(results, "infosys_python")
        
        print("\n✅ TEST COMPLETE!")
        print("   Check the ./output/ folder for saved files")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\n💡 Make sure you have:")
        print("   1. GOOGLE_API_KEY in your .env file")
        print("   2. Installed: pip install crewai langchain-google-genai")
        print("   3. agents_complete.py and tasks_complete.py in same folder")