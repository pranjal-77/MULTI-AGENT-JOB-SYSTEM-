"""
Safe crew runner with automatic retry on rate limits
"""

from crew import run_job_application_crew, display_results, save_results
import time

def run_with_retry(max_retries=3):
    """Run crew with automatic retry on rate limit"""
    
    # Sample data
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
    
    sample_background = """
    5 years Python development with Django/Flask.
    Built RESTful APIs for e-commerce platforms.
    Tech stack: Python, Django, PostgreSQL, Redis, Docker, AWS.
    Experience with CI/CD (Jenkins, GitLab).
    Led team of 3 junior developers.
    Bachelor's in Computer Science.
    """
    
    for attempt in range(max_retries):
        try:
            print(f"\n🚀 Attempt {attempt + 1}/{max_retries}")
            
            results = run_job_application_crew(
                job_description=sample_job,
                company_name="Infosys Limited",
                job_title="Senior Python Developer",
                user_background=sample_background,
                hiring_manager="Rajesh Kumar"
            )
            
            # Success!
            display_results(results)
            save_results(results, "infosys_python")
            
            print("\n✅ SUCCESS!")
            return results
            
        except Exception as e:
            error_msg = str(e)
            
            # Check if it's a rate limit error
            if "Rate limit" in error_msg or "RateLimitError" in error_msg:
                wait_time = 30 + (attempt * 10)  # Wait longer each retry
                print(f"\n Rate limit hit. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                
                if attempt < max_retries - 1:
                    print(f"🔄 Retrying... ({max_retries - attempt - 1} attempts left)")
                else:
                    print("\n Max retries reached. Please try again later.")
                    raise
            else:
                # Different error - don't retry
                print(f"\n Error: {e}")
                raise

if __name__ == "__main__":
    run_with_retry()