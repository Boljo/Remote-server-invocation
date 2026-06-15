<div align="center">

# 💻 Remote Process Invocation - Inspired by https://trailhead.salesforce.com/content/learn/modules/app-integration-patterns/app-integration-patterns-3?trail_id=explore-integration-patterns-and-practices

### Salesforce → FastAPI → Claude

A request-reply integration where Salesforce makes an Apex callout to a Python FastAPI endpoint, which calls the Claude API and returns the response back to Salesforce.

[![Salesforce](https://img.shields.io/badge/Salesforce-Apex-00A1E0?logo=salesforce&logoColor=white)](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Anthropic](https://img.shields.io/badge/Claude-API-D97757?logo=anthropic&logoColor=white)](https://docs.claude.com/)

</div>

---

## 🎥 Demo — Remote FastAPI Server Invocation 😎

<div align="center">
  <a href="https://www.youtube.com/watch?v=5KJ6fgjzhAw">
    <img src="https://img.youtube.com/vi/5KJ6fgjzhAw/maxresdefault.jpg" alt="Watch the demo" width="600">
  </a>
  <br>
  <em>Click the thumbnail to watch the full walkthrough on YouTube.</em>
</div>

---

## ✅ Prerequisites

| Requirement | Notes |
| --- | --- |
| **Salesforce org** | With permission to create Apex classes and Named Credentials |
| **Python 3.9+** | — |
| **Anthropic API key** | Get one at [console.anthropic.com](https://console.anthropic.com/) |
| **Python packages** | `fastapi`, `uvicorn`, `anthropic`, `pydantic` |
| **ngrok** | To expose your local server to Salesforce |

---

## 🚀 How to Use

### 1. Start the Python endpoint

```bash
pip install fastapi uvicorn anthropic pydantic
export ANTHROPIC_API_KEY="your-key-here"
uvicorn main:app --reload --port 8000
```

The endpoint will be available at `POST /endpoint-state`.

### 2. Expose it publicly

So Salesforce can reach your local server:

```bash
ngrok http 8000
```

Copy the `https://` URL ngrok gives you.

### 3. Configure Salesforce

Create a **Named Credential** called `Python_endpoint_named_credential` with the ngrok (or deployed) URL as its endpoint.

### 4. Run the callout

Invoke the Apex class — for example, from **Developer Console → Execute Anonymous**:

```apex
new Remote_Process_Invocation('/endpoint-state', 'YourAccountName');
```

### 5. Check the result

The response from Claude is printed to the Salesforce debug logs.

---

<div align="center">
  <sub>Built with Apex, FastAPI, and Claude.</sub>
</div>
