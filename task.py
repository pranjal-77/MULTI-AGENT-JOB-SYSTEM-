from venv import create

from crewai import Task 

def create_task(agent,job_description):
    """
    Create a task to analyze a job description
    Args:
        agent: The Job Analyst agent
        job_description: The full job posting text
    
    Returns:
        Task object
    """
    return Task(
        description = f""" Analyze this job description in detail and provide a comprehensive breakdown.
        JOB DESCRIPTION:{job_description}
 
Provide a thorough analysis covering:
 
1. TECHNICAL SKILLS REQUIRED
   - List all technical skills mentioned
   - Categorize each as: MUST-HAVE or NICE-TO-HAVE
   - Note any proficiency levels specified
 
2. SOFT SKILLS & QUALITIES
   - Communication requirements
   - Leadership/teamwork expectations
   - Problem-solving abilities needed
   - Other personal qualities sought
 
3. EXPERIENCE REQUIREMENTS
   - Years of experience needed
   - Specific industry experience required
   - Types of projects or work expected
   - Any alternative experience accepted
 
4. KEY RESPONSIBILITIES
   - Day-to-day tasks
   - Primary deliverables
   - Team collaboration aspects
   - Success metrics if mentioned
 
5. EDUCATION & CERTIFICATIONS
   - Required degrees
   - Preferred certifications
   - Alternative qualifications
   - Continuous learning expectations
 
6. CULTURAL FIT & RED FLAGS
   - Company culture indicators
   - Growth opportunities
   - Any concerning requirements
   - Work-life balance signals
   - Competitive aspects
 
 Be thorough but concise. Focus on actionable insights that help candidates
 decide if they're a good fit and how to position themselves.""",
       agent=agent,
       expected_output= """A detailed, well-organized analysis with clear sections
        for each category above. Each section should be 2-5 sentences of focused insights."""
    )


def create_resume_task(agent, job_description, user_background):
    """
    Create a task to tailor a resume to a specific job
    
    Args:
        agent: The Resume Writer agent
        job_description: Target job posting
        user_background: Candidate's experience and skills
    
    Returns:
        Task object
    """
    
    return Task(
        description=f"""Create a tailored resume section that highlights relevant
experience for this specific job opportunity.
 
TARGET JOB:
{job_description}
 
CANDIDATE BACKGROUND:
{user_background}
 
Your task:
1. Identify the 3-5 most relevant experiences from the candidate's background
2. Craft compelling bullet points using the STAR method (Situation, Task, Action, Result)
3. Incorporate keywords from the job description naturally
4. Quantify achievements with specific metrics and numbers
5. Use strong action verbs (led, developed, increased, optimized, designed, etc.)
6. Ensure ATS compatibility (clear formatting, relevant keywords)
7. Match the tone and level to the position (junior/mid/senior)
 
FORMATTING REQUIREMENTS:
• Professional tone appropriate to the role level
• Bullet points starting with action verbs
• Specific, quantified achievements (not just responsibilities)
• 3-5 bullets per role/project
• Keywords from job description woven in naturally
• Focus on IMPACT and RESULTS, not just tasks
 
EXAMPLE FORMAT:
PROFESSIONAL EXPERIENCE
 
[Role Title] | [Company/Project]
• [Action verb] [what you did] resulting in [quantified impact/result]
• [Action verb] [technical achievement] using [technologies from job posting]
• [Action verb] [leadership/collaboration aspect] to [business outcome]
 
Make every word count. Show don't tell.""",
        
        agent=agent,
        
        expected_output="""A polished professional experience section with 3-5
        achievement-focused bullet points that directly address the job requirements.
        Include specific metrics, technical keywords, and clear results."""
    )
 

def cover_letter(agent,job_description,comapany_name,user_background):
    """
    Create a task to write a professional cover letter 
     Args: 
      agent: The Resume Writer agent
      job_description: the job posting  
      comapny_name: the name of the company
      user_background: Candidate experince
      
      Returns: 
      Task Object
      """
    
    return Task(
        description=f"""Write a compelling,personalised cover letter for this position
    Company: {comapany_name}
    Job Description: {job_description}
    Candidate Background: {user_background} 

     STRUCTURE YOUR COVER LETTER:
 
    1. OPENING PARAGRAPH (Hook - 2-3 sentences)
   • Start with a strong hook that grabs attention
   • Show genuine enthusiasm for the role and company
   • Reference something specific about the company (recent news, values, mission)
   • Make it personal, not generic
 
2. BODY PARAGRAPHS (Connection - 2 paragraphs)
   Paragraph 1:
   • Connect your most relevant experience to their needs
   • Highlight 1-2 key achievements with metrics
   • Show you understand their challenges
   
   Paragraph 2:
   • Demonstrate cultural fit
   • Show passion for the industry/domain
   • Explain why THIS company specifically
   • Include another relevant achievement or skill
 
3. CLOSING PARAGRAPH (Call to Action - 2 sentences)
   • Express enthusiasm for discussing further
   • Professional call to action
   • Thank them for consideration
 
GUIDELINES:
• Length: 250-300 words (not too long!)
• Tone: Professional but warm and authentic
• Be SPECIFIC, not generic
• Show personality while remaining professional
• Avoid clichés like "passionate team player"
• Make it about THEM and how you can help, not just about you
• Proper business letter format
 
This should feel like it was written by a human who genuinely wants this job,
not a template. Every sentence should add value.""",
        agent=agent,
        expected_output="""A polished professional experience section with 3-5
        achievement-focused bullet points that directly address the job requirements.
        Include specific metrics, technical keywords, and clear results. """
    )
      

def create_linkedin_message(agent,company_name,job_title,hiring_manager_name,user_background):
    """
    Create a task to write a personalized LinkedIn message
    
    Args:
        agent:The Messaging Specialist agent
        job_title: Position being applied for
        company_name: Target company
        hiring_manager_name: Name of hiring manager
        user_background: Candidate's background
    Returns:
        Task Object
    """
    
    return Task(
        description=f"""Create two professional LinkedIn messages for networking
related to this job opportunity.
CONTEXT:
Position: {job_title}
Company: {company_name}
Contact: {hiring_manager_name}
Your Background: {user_background}
 
CREATE TWO SEPARATE MESSAGES:
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE 1: CONNECTION REQUEST (MAXIMUM 300 characters!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 
LinkedIn limits connection requests to 300 characters. Every character counts!
 
Requirements:
• Reference something specific (mutual connection, company news, their work)
• Mention the role you're interested in
• Be warm but professional
• Give them a reason to connect
• Make it feel personal, not like a mass message
• NO generic "I'd like to add you to my network"
 
Bad example: "Hi, I'd like to connect with you. I'm interested in the Python role."
Good example: "Hi [Name]! Saw your post on [Company's] AI initiative. I'm applying
for the Python Developer role and would love to learn more about the team's vision."
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE 2: FOLLOW-UP (After connection accepted - 150-200 words)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 
This is sent AFTER they accept your connection request.
 
Structure:
• Thank them for connecting (1 sentence)
• Express genuine interest in the role/company (2 sentences)
• Share 1-2 relevant achievements briefly (2-3 sentences)
• Ask an insightful question about the role or team (1 sentence)
• Gentle call to action (1 sentence)
• Optional: Offer value (share an article, insight, etc.)
 
Tone Guidelines:
• Conversational but professional
• Genuinely curious, not transactional
• Respectful of their time
• Show you've done research
• Focus on mutual value, not just what you want
 
CRITICAL PRINCIPLES:
• Be genuine, not salesy
• Do your homework (reference company projects, news, values)
• Make it about the work and the mission, not just "getting a job"
• Show enthusiasm without desperation
• Build a relationship, don't just ask for things
 
Remember: The goal is to start a genuine professional conversation, not to
immediately ask for a job. People can spot inauthentic networking from miles away.""",
   agent=agent,
   expected_output="""Two clearly labeled messages:
 
CONNECTION REQUEST: [Exactly at or under 300 characters, personalized and specific]
 
FOLLOW-UP MESSAGE: [150-200 words, professional but warm, focused on building
a genuine connection while expressing interest in the opportunity]"""
    )


def create_complete_application_tasks(
    agents_dict,
    job_info,
    user_background
):
    """
    Create all tasks for a complete job application
    
    Args:
        agents_dict: Dictionary with 'analyst', 'resume', 'messaging' keys
        job_info: Dict with 'description', 'company', 'title', 'hiring_manager'
        user_background: Candidate's background
    
    Returns:
        List of Task objects in execution order
    """
    
    tasks = [
        # Task 1: Analyze the job
        create_task(
            agents_dict['analyst'],
            job_info['description']
        ),
        
        # Task 2: Tailor resume
        create_resume_task(
            agents_dict['resume'],
            job_info['description'],
            user_background
        ),
        
        # Task 3: Write cover letter
        cover_letter(
            agents_dict['resume'],
            job_info['description'],
            job_info['company'],
            user_background
        ),
        
        # Task 4: Create LinkedIn messages
        create_linkedin_message(
            agents_dict['messaging'],
            job_info['title'],
            job_info['company'],
            job_info.get('hiring_manager', 'Hiring Manager'),
            user_background
        )
    ]
    
    return tasks
 
 
# ============================================================================
# TEST TASKS
# ============================================================================
 
if __name__ == "__main__":
    """
    Test task creation
    Run: python tasks.py
    """
    
    print("\n" + "="*80)
    print("🧪 TESTING TASK DEFINITIONS")
    print("="*80)
    
    print("\n✅ Available task creators:")
    print("   1. create_job_analysis_task()")
    print("   2. create_resume_task()")
    print("   3. create_cover_letter_task()")
    print("   4. create_linkedin_outreach_task()")
    print("   5. create_complete_application_tasks()")
    
    print("\n💡 These tasks will be assigned to agents in crew.py")
    print("\n" + "="*80 + "\n")