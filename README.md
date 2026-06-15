<div align="center">

# 💻 Remote Process Invocation

### Salesforce → FastAPI → Claude

A request–reply integration pattern where Salesforce makes an Apex callout to a Python FastAPI endpoint, which calls the Claude API and returns the response back to Salesforce — synchronously, in a single round trip.

[![Salesforce](https://img.shields.io/badge/Salesforce-Apex-00A1E0?logo=salesforce&logoColor=white)](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Anthropic](https://img.shields.io/badge/Claude-API-D97757?logo=anthropic&logoColor=white)](https://docs.claude.com/)

<sub>Inspired by the <a href="https://trailhead.salesforce.com/content/learn/modules/app-integration-patterns/app-integration-patterns-3?trail_id=explore-integration-patterns-and-practices">Remote Process Invocation – Request and Reply</a> pattern from Salesforce Trailhead.</sub>

</div>

---

## 🎥 Demo

<div align="center">
  <a href="https://www.youtube.com/watch?v=5KJ6fgjzhAw">
    <img src="https://img.youtube.com/vi/5KJ6fgjzhAw/maxresdefault.jpg" alt="Watch the demo on YouTube" width="600">
  </a>
  <br>
  <em>Click the thumbnail for the full walkthrough.</em>
</div>

---

## 🧭 How it works

```
Salesforce (Apex)  ──HTTP POST──▶  FastAPI endpoint  ──▶  Claude API
       ▲                                                        │
       └────────────── JSON response ◀──────────────────────────┘
```

1. Apex sends an HTTP callout through a Named Credential.
2. FastAPI receives the payload and forwards it to Claude.
3. Claude's response flows back to Salesforce in the same transaction.

---

## ✅ Prerequisites

| Requirement | Notes |
| --- | --- |
| **Salesforce org** | With permission to create Apex classes and Named Credentials |
| **Python 3.9+** | Any recent version works |
| **Anthropic API key** | Grab one at [console.anthropic.com](https://console.anthropic.com/) |
| **Python packages** | `fastapi`, `uvicorn`, `anthropic`, `pydantic` |
| **ngrok** | To expose your local server to Salesforce |

---

## 🚀 Getting started

### 1. Start the FastAPI server

```bash
pip install fastapi uvicorn anthropic pydantic
export ANTHROPIC_API_KEY="your-key-here"
uvicorn main:app --reload --port 8000
```

The endpoint will be live at `POST /endpoint-state`.

### 2. Expose it to the internet

Salesforce needs a public URL to reach your local server:

```bash
ngrok http 8000
```

Copy the `https://` forwarding URL ngrok prints out.

### 3. Configure Salesforce

In **Setup**, create a **Named Credential** called `Python_endpoint_named_credential` and paste the ngrok (or deployed) URL as its endpoint.

### 4. Fire the callout

From **Developer Console → Execute Anonymous**, run:

```apex
new Remote_Process_Invocation('/endpoint-state', 'YourAccountName');
```

### 5. Inspect the response

Claude's reply is written to the Salesforce **debug logs** — open the most recent log to see the result.

---

<div align="center">
  <sub>Built with Apex, FastAPI, and Claude.</sub>
</div>
