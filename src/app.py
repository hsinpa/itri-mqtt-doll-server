from fastapi import FastAPI

from src.router.yuri_temp_router import router as yuri_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(openapi_url="/docs/openapi.json", docs_url="/docs")
app.include_router(yuri_router)

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://counseling-psycho.vercel.app",
    "https://counseling-psycho-chatbot.vercel.app",
    "https://itri-mqtt-doll-git-dev-hsinpas-projects.vercel.app",
    "https://itri-mqtt-doll.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"version": "0.0.2"}