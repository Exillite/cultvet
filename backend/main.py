from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="CultVet",
    description="API for application with entarective excursions.",
    version="0.1",
    contact={
        "name": "Author: Alexander Rodionov",
        "email": "sa27shal@gmail.com"
    },
    openapi_url="/api/v0.1/openapi.json",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v0.1", description="Root endpoint", tags=['BASE'])
async def test():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
