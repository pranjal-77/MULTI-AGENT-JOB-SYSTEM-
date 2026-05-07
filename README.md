# 🤖 Multi-Agent Job Search System

An AI-powered multi-agent system that automates and supercharges the job search process — from analyzing job descriptions to writing tailored resumes, cover letters, and LinkedIn outreach messages.

---

## 🚀 What It Does

This system uses **3 specialized AI agents** working together via **CrewAI** to handle every stage of the job application process:

| Agent | Role | What It Does |
|-------|------|--------------|
| 🔍 **Job Analyst** | Senior Job Market Analyst | Analyzes job descriptions, extracts must-have vs nice-to-have skills, identifies what employers really want |
| ✍️ **Resume Writer** | Certified Professional Resume Writer (CPRW) | Creates ATS-friendly resumes and cover letters tailored to the job |
| 💬 **LinkedIn Specialist** | Professional Outreach Specialist | Drafts personalized LinkedIn connection requests and follow-up messages |

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **AI Framework** | CrewAI 0.74.1 |
| **LLM** | Groq (Llama 3.3 70B Versatile) |
| **LLM Orchestration** | LangChain 0.1.20 |
| **Frontend** | Streamlit 1.40.0 |
| **Data Handling** | Pandas 2.2.0 |
| **API Clients** | Anthropic, Google Generative AI |
| **Config** | Python-dotenv, PyYAML |
| **Validation** | Pydantic 2.6.4 |
| **Language** | Python 3.10+ |

---

## 📁 Project Structure

```
MULTI-AGENT-JOB-SYSTEM/
├── agents.py          # Agent definitions (Job Analyst, Resume Writer, LinkedIn Specialist)
├── crew.py            # CrewAI crew configuration and orchestration
├── task.py            # Task definitions for each agent
├── run_crew.py        # Entry point to run the multi-agent system
├── test_crew.py       # Tests for the crew
├── utils.py           # Utility functions
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
└── frontend/          # Streamlit frontend UI
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/pranjal-77/MULTI-AGENT-JOB-SYSTEM-.git
cd MULTI-AGENT-JOB-SYSTEM-
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
Get your free Groq API key at [console.groq.com](https://console.groq.com)

---

## ▶️ Running the System

### Run the multi-agent crew
```bash
python run_crew.py
```

### Run the Streamlit frontend
```bash
streamlit run frontend/app.py
```

### Test agents individually
```bash
python agents.py
python test_crew.py
```

---

## 🧠 How It Works

1. You provide a **job description** and your **background/resume**
2. The **Job Analyst** breaks down the job requirements and identifies key skills
3. The **Resume Writer** crafts a tailored resume and cover letter based on the analysis
4. The **LinkedIn Specialist** writes a personalized outreach message to the hiring manager or recruiter
5. All outputs are saved and displayed via the Streamlit UI

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key for LLM inference |

> ⚠️ Never commit your `.env` file. It's already in `.gitignore`.

---

## 📦 Dependencies

```
streamlit==1.40.0
crewai==0.74.1
langchain==0.1.20
python-dotenv==1.0.1
requests==2.32.3
pandas==2.2.0
pydantic==2.6.4
anthropic==0.28.0
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 👤 Author

**Pranjal** — [@pranjal-77](https://github.com/pranjal-77)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
