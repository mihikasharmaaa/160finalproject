from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI()


class NutritionRecRequest(BaseModel):
    prompt: str


@app.post("/api/nutrition/recommendation")
async def create_nutrition_recommendation(req: NutritionRecRequest):
    async with httpx.AsyncClient() as client:
        params = {
            "key": "rg_v1_xglbbxx7o082u7qgn1ug10yl10putbntwmuq_ngk", "prompt": req.prompt}
        resp = await client.get("https://noggin.rea.gent/shallow-chipmunk-1074", params=params)
    return resp.text
