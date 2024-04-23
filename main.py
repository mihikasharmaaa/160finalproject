from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()

client = OpenAI(api_key="ghu_WV2pVtYEMj0xPuG8ftVypa7UgPsyiK15rxTV",
                base_url="http://localhost:8080/v1")


class NutritionRecRequest(BaseModel):
    prompt: str


@app.post("/api/nutrition/recommendation")
async def create_nutrition_recommendation(req: NutritionRecRequest):
    resp = client.chat.completions.create(
        model="gpt-4",
        stream=False,
        top_p=1.0,
        max_tokens=100,
        temperature=0.5,
        messages=[
            {"role": "system", "content": "You are a cat nutritionist, skilled in recommending healthy and balanced diets for pets."},
            {"role": "user", "content": req.prompt}
        ]
    )
    return resp.choices[0].message.content.strip()
