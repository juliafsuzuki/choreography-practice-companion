# Choreography Coach Agent

> An AI agent that helps competitive ballroom dancers turn a showcase video into a personalized practice companion.

Built for the **Google for Startups: AI Agents Challenge 2026 — Track 1**.

## What it does

Choreography Coach is an autonomous agent built with the **Google Agent Development Kit (ADK)** and powered by **Gemini 2.5 Flash**. A competitive dancer hands the agent a showcase video and a dance style.
The agent then:

1. Analyzes the music's tempo and beat structure
2. Proposes a phrase-by-phrase practice breakdown aligned to the music
3. Returns a personalized drill plan with timestamps and counts

The end-state vision: the agent autonomously cuts per-phrase MP4 clips and deploys a "Showcase Practice" web app the dancer can drill against.

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

<img width="1299" height="790" alt="image" src="https://github.com/user-attachments/assets/6ab5dede-2287-4802-89f6-c36b6780d3e1" />
Step 1: The home page loads in the Agent Development Kit interface. The user (a competitive ballroom dancer) is greeted with the "Choreography Coach Agent," an AI-powered assistant designed to help dancers practice choreographies more effectively by transforming a choreography video into a personalized practice companion. 


<img width="1436" height="524" alt="image" src="https://github.com/user-attachments/assets/75c7faed-fd7f-4b44-9815-cf73b4b83dbb" />
Step 2: The dancer enters the initial prompt: "Can you help me practice my Waltz routine?"
The agent responds by requesting three pieces of information:

1. The file path to the showcase video
2. The dance style (e.g., Waltz in 3/4 time)
3. The approximate length of the routine in seconds


<img width="1425" height="791" alt="image" src="https://github.com/user-attachments/assets/f3ecd682-722a-40c5-94e6-ef17c672da20" />
Step 3: The dancer enters a prompt with the requested information: "I want to practice my showcase. It's a 90-second Waltz in 3/4 time. The video is located at C:\Users\Julia\Videos\V_Rhythm.mp4."
The agent then works through the request transparently, showing each step:

- It confirms that it is analyzing the tempo and time signature of the video.
- It detects 90 BPM and confirms the 3/4 time signature.
- It announces the next step: breaking the 90-second routine into manageable practice phrases of four measures each.
- Finally, it delivers a personalized Waltz Practice Plan with 12 numbered phrases, each with exact timestamps (e.g., Phrase 01: 0:00–0:08, 12 counts), ending with Phrase 12 at 1:30. <br />


## About

Built for Google for Startups - AI Agents Challenge.

Built by Julia Suzuki, founder of **Truly Human AI**, an AI-first product company building personalized training companions for competitive ballroom dancers.

<img width="877" height="496" alt="image" src="https://github.com/user-attachments/assets/906ad27e-5c5c-4e4c-ad26-28cdf92de07c" />




