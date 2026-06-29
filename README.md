# Choreography Practice Companion Application

> An AI agent that transforms showcase videos into personalized practice companions, helping competitive ballroom dancers learn, refine, and master their routines.

Built for the **Google for Startups: AI Agents Challenge 2026 — Track 1**.

### Track 1: Build (Net-New Agents)

Start with a blank canvas and a complex business problem. In this track, you will leverage the Agent Development Kit (ADK)—or your preferred open-source framework like LangChain or CrewAI—to architect a net-new autonomous agent. Your goal is to move from static code to declarative intent. Show us how your agent uses the Model Context Protocol (MCP) to securely connect to external tools, gather context, and execute tasks autonomously. <br />

<br />

## What it does 

Personalized Choreography Practice Companion is an autonomous agent built with the **Google Agent Development Kit (ADK)** and powered by **Gemini 2.5 Flash**. A competitive dancer hands the agent a showcase video and a dance style.
The agent then:

1. Analyzes the music's tempo and beat structure
2. Proposes a phrase-by-phrase practice breakdown aligned to the music
3. Returns a personalized drill plan with timestamps and counts

## Aspiration / Future State

The vision is for the agent to autonomously analyze a choreography video, generate per-phrase MP4 clips, and deploy a personalized "Showcase Practice" web application that dancers can use to drill and master their routines.

The resulting experience would be similar to the Showcase Genie application that I built using Perplexity Computer.

Showcase Genie:
https://showcase-genie.vercel.app/


## Architecture

- **Framework:** Google Agent Development Kit (ADK) for Python
- **Model:** Gemini 2.5 Flash (via Google AI Studio)
- **Pattern:** Single LLM agent + custom function tools
- **Runtime:** Local (`adk web`) and Cloud Run

```
choreography_coach (root_agent)
        │
        ├── analyze_audio_tempo   ← detects BPM + time signature
        └── propose_phrase_breakdown ← proposes practice phrases
```

## Project structure

```
my_agent/
├── .env                # API keys (gitignored)
├── __init__.py         # package init
├── agent.py            # root_agent definition + instruction prompt
└── custom_functions.py # tool implementations
```

## Run locally

```bash
pip install google-adk
cd my_agent
# Add your GOOGLE_API_KEY to .env (get one at aistudio.google.com/apikey)
python3 -m google.adk.cli web --allow_origins "regex:https://.*\.cloudshell\.dev"
```

Then open the web preview and chat with the agent.

## Test the agent

👉 https://choreography-coach-320638869939.us-central1.run.app/dev-ui/?app=choreography_coach <br />
<br />

<img width="1299" height="790" alt="image" src="https://github.com/user-attachments/assets/6ab5dede-2287-4802-89f6-c36b6780d3e1" />
Step 1: The home page loads in the Agent Development Kit interface. The user (a competitive ballroom dancer) is greeted with the "Choreography Coach Agent," an AI-powered assistant designed to help dancers practice choreographies more effectively by transforming a choreography video into a personalized practice companion. <br /> 

<br />

<img width="1435" height="530" alt="Step 2" src="https://github.com/user-attachments/assets/eb05cdcd-9d3a-4d4b-8c8d-608e5e128358" />
Step 2: The dancer enters the initial prompt: "Can you help me practice my Waltz routine?"
The agent responds by requesting three pieces of information:

1. The file path to the showcase video
2. The dance style (e.g., Waltz in 3/4 time)
3. The approximate length of the routine in seconds

<br />

<img width="1426" height="527" alt="analyze_audio_tempo" src="https://github.com/user-attachments/assets/909e0b70-5908-4f7d-845e-9154a97ba280" />
Notice: ADK function tool, analyze_audio_tempo is called <br /> 

<br />

<img width="1430" height="528" alt="propose_phrase_breakdown" src="https://github.com/user-attachments/assets/5c246f9d-f0f7-4bc1-80be-b9832e4969d0" />
Notice: ADK function tool, propose_phrase_breakdown is called <br />

<br />

<img width="1425" height="791" alt="image" src="https://github.com/user-attachments/assets/f3ecd682-722a-40c5-94e6-ef17c672da20" />
Step 3: The dancer enters a prompt with the requested information: "I want to practice my showcase. It's a 90-second Waltz in 3/4 time. The video is located at C:\Users\Julia\Videos\V_Rhythm.mp4."
The agent then works through the request transparently, showing each step:

- It confirms that it is analyzing the tempo and time signature of the video.
- It detects 90 BPM and confirms the 3/4 time signature.
- It announces the next step: breaking the 90-second routine into manageable practice phrases of four measures each.
- Finally, it delivers a personalized Waltz Practice Plan with 12 numbered phrases, each with exact timestamps (e.g., Phrase 01: 0:00–0:08, 12 counts), ending with Phrase 12 at 1:30. <br />

<br />

## About

Built for Google for Startups - AI Agents Challenge.

Built by Julia Suzuki, founder of **Truly Human AI**, an AI-first product company building personalized training companions for competitive ballroom dancers.

<img width="877" height="496" alt="image" src="https://github.com/user-attachments/assets/906ad27e-5c5c-4e4c-ad26-28cdf92de07c" />




