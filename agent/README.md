# Agent Module

The `agent` package contains the core orchestration logic of ResearchMind-AI.

## Responsibilities

- Command routing
- Conversation memory
- Tool execution
- Research workflow orchestration
- AI interaction

## Files

### research_agent.py

The main controller responsible for handling user requests, invoking the appropriate services, managing conversation history, and coordinating the overall workflow.

### router.py

Parses user commands and maps them to the appropriate action.

Examples:

- search
- summarize
- compare
- review
- cite

### memory.py

Maintains conversation context during the current session.

### tools.py

Acts as a wrapper around all service modules and provides a unified interface to the Research Agent.

## Workflow

```
User
 │
 ▼
ResearchAgent
 │
 ├── Router
 ├── Memory
 └── Tools
      │
      ▼
 Services
```
