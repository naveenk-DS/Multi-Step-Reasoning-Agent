# Multi-Step Reasoning Agent with Self-Checking
This project implements a structured reasoning agent that solves word problems using a
Planner → Executor → Verifier loop. The agent performs multi-step reasoning, validates its
own answers, and exposes only a short, user-safe explanation in structured JSON format.
## How to Run Locally


### 1. Setup Environment:
```python -m venv venv```
```venv\Scripts\activate (Windows)```
```pip install -r requirements.txt```

### 2. Run CLI:
```python cli.py```

### 3. Run Web UI (Streamlit):
```python -m streamlit run app.py```
```Open browser at: http://localhost:8501```

### 4.LLM Configuration
```Edit agent/config.py and set LLM_PROVIDER to mock or openai.```
```For OpenAI, set environment variable OPENAI_API_KEY.```

### 5.Where Prompts Live
```agent/prompts/```
- planner_prompt.txt
- executor_prompt.txt
- verifier_prompt.txt
  
### 6.Assumptions
- Input questions are structured word problems
- Mock LLM is deterministic for offline testing
- OpenAI backend provides real reasoning
- Verifier ensures internal consistency
  
### 7.Prompt Design
Planner: Decomposes problem without solving.
Executor: Follows plan exactly and computes result.
Verifier: Re-checks correctness independently.

### 8.What Didn’t Work Well
- Free-form outputs broke JSON parsing
- Planner solving problems caused duplication
- Mock LLM has limited generalization
  
### 9.What I Would Improve
- Python-based arithmetic tools
- Stronger symbolic verification
- Caching and UI history support
  
### 10.Example Output
```Answer: 12```
```Status: success```
```Reasoning: Tom has 12 chocolates remaining.```

## This project demonstrates multi-step reasoning, self-verification, and production-ready deployment.
