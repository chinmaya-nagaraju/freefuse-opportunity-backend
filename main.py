from fastapi import FastAPI, Request
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/ask-gpt")
async def ask_gpt(request: Request):
    body = await request.json()
    user_message = body["userMessage"]

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are the FreeFuse Opportunity Classifier. Use the uploaded taxonomy to match inputs to categories."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    answer = response.choices[0].message["content"]
    return {"answer": answer}
