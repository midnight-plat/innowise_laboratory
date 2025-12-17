from fastapi import FastAPI

# Creating FastAPI
app = FastAPI()

# Making endpoint (Health Check)
@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}