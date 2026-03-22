# Aareon AI Agent System
This is a sample POC project for an intelligent property management platform powered by OpenAI GPT, featuring specialized AI agents for real estate operations.
## Features
### 6 Specialized AI Agents
- Document Processor - Extract data from maintenance requests, leases, invoices
- Customer Support - Handle tenant inquiries 24/7
- Process Automation - Optimize maintenance scheduling, rent collection
- Tenant Screening - Calculate risk scores and recommendations
- Financial Analyst - Analyze occupancy rates, ROI, cash flow
- Maintenance Predictor - Predict issues and generate schedules
### Key Capabilities
- RAG System - Intelligent document retrieval
- Advanced Metrics - ROUGE, BLEU, response time analysis
- Evaluation Framework - Track accuracy and performance
- Interactive UI - Gradio web interface with 7 tabs
## Quick Start
# Clone repository
git clone https://github.com/yourusername/aareon-ai-agent-system.git
cd aareon-ai-agent-system

# Install dependencies
pip install -r requirements.txt

# Set up OpenAI API key
cp .env.example .env
# Add your OpenAI API key to .env

# Run the web interface
python gradio_app.py

Access at: [http://localhost:7860](http://localhost:7860)

## Sample Data Included

* Property records (8 properties)
* Tenant information
* Maintenance requests
* Customer inquiries

## Tech Stack

* Python 3.11+
* OpenAI GPT - LLM integration
* Gradio - Web interface
* Pandas - Data processing
* LangChain - Agent framework

## Project Structure

aareon-ai-agent-system/
├── src/ai_agents/      # 6 specialized agents
├── src/core/           # LLM client, vector store
├── src/evaluation/     # Metrics and testing
├── data/raw/           # Sample CSV data
├── config/             # Settings and prompts
└── gradio_app.py       # Web interface

## Use Cases

* Process maintenance requests automatically
* Answer tenant questions instantly
* Screen potential tenants
* Analyze property financials
* Predict maintenance needs
* Automate workflows

## Evaluation Metrics

* Exact and partial match accuracy
* Response time analytics (avg, p95, p99)
* Token usage and cost tracking
* Quality scores (readability, professionalism)

## Contributing

Contributions welcome. Please read contributing guidelines.

## License

MIT License

## Acknowledgments

* OpenAI for GPT models
* Aareon for the vision
Status: Production Ready | Version: 2.0 | Agents: 6
## Short Version
# Aareon AI Agent System
AI powered property management platform with 6 specialized agents.
## Features

- Document Processor - Extract data from leases, invoices, maintenance requests
- Customer Support - Handle tenant inquiries 24/7
- Process Automation - Optimize workflows
- Tenant Screening - Risk scoring and recommendations
- Financial Analyst - ROI, occupancy, cash flow analysis
- Maintenance Predictor - Predict and schedule repairs

## Quick Start
pip install -r requirements.txt
cp .env.example .env
python gradio_app.py
Open [http://localhost:7860](http://localhost:7860)
## Sample Data
Property records, tenant info, maintenance requests, customer inquiries
## Tech Stack
Python, OpenAI GPT, Gradio, Pandas, LangChain
## Evaluation Metrics
* ROUGE and BLEU scores
* Response time analytics
* Token usage and cost tracking
* Quality scoring
## License
MIT
Status: Production Ready

```
```
