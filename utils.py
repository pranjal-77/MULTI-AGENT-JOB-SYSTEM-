import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_india_jobs(keyword='software engineer', location='', num_results=10):
    """
    Fetch job listings from Adzuna API for INDIA
    
    Args:
        keyword: Job search term (e.g., 'python developer', 'data scientist')
        location: Indian city (e.g., 'Mumbai', 'Bangalore', 'Delhi')
        num_results: Number of results to return (max 50)
    
    Returns:
        List of job dictionaries
    """
    
    print(f"\n🇮🇳 Searching Indian jobs for: '{keyword}'")
    if location:
        print(f"   📍 Location: {location}")
    
    # Step 1: Get API credentials
    app_id = "220b0141"
    app_key ="7fd502c8c33abc87bf8c52a6a9d84768"
    
    if not app_id or not app_key:
        print("\n❌ ERROR: Adzuna credentials not found in .env file!")
        print("\n🔧 Add these to your .env file:")
        print("   ADZUNA_APP_ID=your_app_id")
        print("   ADZUNA_APP_KEY=your_app_key")
        print("\n📝 Get credentials from: https://developer.adzuna.com/")
        return []
    
    country = 'in'  
    page = 1
    url = f'https://api.adzuna.com/v1/api/jobs/{country}/search/{page}'
    
    # Step 3: Adzuna uses QUERY PARAMETERS for authentication (not headers!)
    params = {
        'app_id': app_id,           # Authentication
        'app_key': app_key,         # Authentication
        'results_per_page': min(num_results, 50),  # Max 50
        'what': keyword,             # Job title/keywords
        'content-type': 'application/json'
    }
    
    # Add location if provided
    if location:
        params['where'] = location
    
    # Step 4: Make the request
    try:
        print("   📡 Sending request to Adzuna API...")
        response = requests.get(url, params=params, timeout=10)
        
        # Check for errors
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            
            if not results:
                print("   ⚠️  No jobs found")
                return []
            
            print(f"   ✅ Found {len(results)} jobs!")
            
            # Step 5: Process the results (Adzuna format is different!)
            job_list = []
            for job in results:
                # Get salary information
                salary_min = job.get('salary_min')
                salary_max = job.get('salary_max')
                
                if salary_min and salary_max:
                    salary = f"₹{salary_min:,.0f} - ₹{salary_max:,.0f} per year"
                elif salary_min:
                    salary = f"₹{salary_min:,.0f}+ per year"
                else:
                    salary = "Not specified"
                
                # Build job dictionary
                job_data = {
                    'title': job.get('title', 'N/A'),
                    'company': job.get('company', {}).get('display_name', 'N/A'),
                    'location': job.get('location', {}).get('display_name', 'N/A'),
                    'description': job.get('description', 'No description'),
                    'url': job.get('redirect_url', ''),
                    'salary': salary,
                    'contract_type': job.get('contract_type', 'N/A'),
                    'posted_date': job.get('created', 'N/A'),
                    'category': job.get('category', {}).get('label', 'N/A')
                }
                
                job_list.append(job_data)
            
            return job_list
            
        elif response.status_code == 401:
            print("\n❌ ERROR 401: Invalid credentials")
            print("   Check your ADZUNA_APP_ID and ADZUNA_APP_KEY")
            return []
            
        elif response.status_code == 429:
            print("\n❌ ERROR 429: Rate limit exceeded")
            print("   Free tier: 500 calls/month")
            return []
            
        else:
            print(f"\n ERROR {response.status_code}: {response.reason}")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Network error: {e}")
        return []
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return []


def display_job(job, index=None):
    """Pretty print a job listing"""
    
    separator = "=" * 80
    
    if index is not None:
        print(f"\n{separator}")
        print(f"🇮🇳 JOB #{index + 1}")
        print(separator)
    
    print(f"📋 Title:        {job['title']}")
    print(f"🏢 Company:      {job['company']}")
    print(f"📍 Location:     {job['location']}")
    print(f"💰 Salary:       {job['salary']}")
    print(f"📝 Type:         {job['contract_type']}")
    print(f"🏷️  Category:     {job['category']}")
    print(f"📅 Posted:       {job['posted_date']}")
    print(f"🔗 URL:          {job['url']}")
    print(f"\n📄 Description:")
    desc = job['description'][:300] if len(job['description']) > 300 else job['description']
    print(f"   {desc}...")
    
    if index is not None:
        print(separator)


# Test the API
if __name__ == "__main__":
    print("\n" + "="*80)
    print("🇮🇳 INDIAN JOB SEARCH - ADZUNA API")
    print("="*80)
    
    # Test 1: General search
    jobs = fetch_india_jobs('python developer', num_results=3)
    
    if jobs:
        print(f"\n✅ SUCCESS! Found {len(jobs)} jobs\n")
        for i, job in enumerate(jobs):
            display_job(job, i)
    else:
        print("\n💡 If you don't have Adzuna credentials yet:")
        print("   1. Sign up at: https://developer.adzuna.com/signup")
        print("   2. Get your App ID and App Key")
        print("   3. Add to .env file:")
        print("      ADZUNA_APP_ID=your_id")
        print("      ADZUNA_APP_KEY=your_key")
        print("\n   OR use mock_indian_jobs.py for testing!")
    
    print("\n" + "="*80)
    
    # Test 2: City-specific search
    print("\n🔍 Searching for jobs in Bangalore...")
    blr_jobs = fetch_india_jobs('software engineer', 'Bangalore', num_results=2)
    
    if blr_jobs:
        print(f"\n✅ Found {len(blr_jobs)} jobs in Bangalore:")
        for job in blr_jobs:
            print(f"   • {job['title']} - {job['company']}")
    
    print("\n" + "="*80 + "\n")