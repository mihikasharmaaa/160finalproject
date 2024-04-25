from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class NutritionRecRequest(BaseModel):
    prompt: str

@app.post("/api/nutrition/recommendation")
async def create_nutrition_recommendation(req: NutritionRecRequest):
    async with httpx.AsyncClient() as client:
        params = {
            "key": "rg_v1_xglbbxx7o082u7qgn1ug10yl10putbntwmuq_ngk", "prompt": req.prompt}
        resp = await client.get("https://noggin.rea.gent/shallow-chipmunk-1074", params=params)
    return resp.text
