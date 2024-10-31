from fastapi import FastAPI
import uvicorn
api = FastAPI()


@api.get("/")
async def home():
    return {"message": "Hello World"}

if __name__ == "__main___":
    uvicorn.run("api:api", host="0.0.0.0", port=5000, reload=True)