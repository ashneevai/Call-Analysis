# ABC Telecom Call Analysis — Architecture

This document provides high-level architecture and data flow for the ABC Telecom Call Analysis system. Diagrams use Mermaid and render on GitHub.

## System Context
```mermaid
flowchart TD
  User(End User) -->|Submits transcript / views results| UI[Streamlit Web UI\n(app.py)]

  subgraph Engine[Classification Engine\n(tools/classification_tools.py)]
    A[analyze_call_transcript]
    C[classify_call_category]
    E[extract_customer_info]
    R[generate_classification_report]
  end

  subgraph CrewAI[Optional: Crew AI Orchestration\n(src/agents.py, src/tasks.py, src/crew.py)]
    AG[agents.py]
    TK[tasks.py]
    CW[crew.py]
  end

  OA[(OpenAI API)]
  DATA[(Sample Data\n data/sample_transcripts.py)]

  UI -->|Calls| Engine
  UI -->|Loads samples| DATA
  UI -. optional .-> CrewAI
  CrewAI -. requires .-> OA

  Engine -->|Returns metrics + report| UI
  CrewAI -. returns reasoning .-> UI
```

## Component Overview
```mermaid
flowchart LR
  subgraph Web[Web UI]
    APP[app.py\nStreamlit tabs\n- Classify\n- Analysis\n- Batch\n- Samples]
  end

  subgraph Core[Core Engine]
    TOOLS[tools/classification_tools.py\n- analyze_call_transcript\n- classify_call_category\n- extract_customer_info\n- generate_classification_report]
  end

  subgraph Agents[Optional Agents]
    AGENTS[src/agents.py]
    TASKS[src/tasks.py]
    CREW[src/crew.py]
  end

  subgraph Data[Data]
    SAMPLES[data/sample_transcripts.py]
  end

  APP --> TOOLS
  APP --> SAMPLES
  APP -. optional .-> AGENTS
  AGENTS --> TASKS --> CREW
```

## Sequence — Single Call Classification (Direct Path)
```mermaid
sequenceDiagram
  participant U as User
  participant S as Streamlit UI (app.py)
  participant E as Engine (classification_tools.py)

  U->>S: Paste transcript and click Classify
  S->>E: analyze_call_transcript(transcript)
  E-->>S: analysis (sentiment, urgency, topics)
  S->>E: classify_call_category(transcript, analysis)
  E-->>S: primary_category, confidence, scores
  S->>E: extract_customer_info(transcript)
  E-->>S: services, issues, requests
  S->>E: generate_classification_report(...)
  E-->>S: formatted report
  S-->>U: Metrics, charts, downloadable report
```

## Sequence — Optional Crew AI Path
```mermaid
sequenceDiagram
  participant U as User
  participant S as Streamlit UI (app.py)
  participant C as Crew (src/crew.py)
  participant O as OpenAI API

  U->>S: Submit transcript (AI mode)
  S->>C: create_quick_classification_crew(...).kickoff()
  C->>O: LLM prompts (analysis, classification)
  O-->>C: Structured outputs
  C-->>S: Results (category, confidence, reasoning)
  S-->>U: Display results and exports
```

## Deployment
- Local execution via Streamlit: app runs on localhost:8501
- Source hosted on GitHub: pushes from local repo
- No database; session state in-memory for UI
- Optional: Add CI/CD, Docker, or cloud hosting later

## Key Files
- Web UI: app.py
- Core engine: tools/classification_tools.py
- Optional agents: src/agents.py, src/tasks.py, src/crew.py
- Samples: data/sample_transcripts.py
- Docs: README.md, START_HERE.md, UI_GUIDE.md
