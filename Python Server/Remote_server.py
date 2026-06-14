import os
from fastapi import FastAPI
from pydantic import BaseModel, field_validator
import anthropic 

client = anthropic.Anthropic()

app = FastAPI()

class OrderRequest(BaseModel):
    message_id: str        
    account_id: str

    @field_validator('message_id', mode='before')
    @classmethod
    def coerce_to_string(cls, v):
        if isinstance(v, (int, float)):
            return str(v)
        return v  # Ensures it passes back the string if it was already a string

seen = {}                  

@app.post("/endpoint-state") #- this is the endpoint
def endpoint_state(req: OrderRequest):
    if req.message_id in seen:        
        return seen[req.message_id] # making sure we're not processing the same reuest twice
        
    prepare_response = client.messages.create( # we're sending the request to claude to process
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Received a new API request: {req.message_id} and account_id: {req.account_id}. please return a short, funny and cheerful response"
            }
        ]
    )
    result = prepare_response.content[0].text.strip()
    seen[req.message_id] = result
    return result # finally, results sent back to sf .....Let's go Babyyyy!!!