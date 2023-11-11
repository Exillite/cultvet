from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from modules.Files.routes import router as FilesRouter
from modules.User.routes import router as UsersRouter
from modules.Ecscursion.routes import router as ExcursionsRouter
from modules.PassEcscursion.routes import router as PassExcursionsRouter

from db import connect_to_mongo, close_mongo_connection


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


app.include_router(FilesRouter)
app.include_router(UsersRouter)
app.include_router(ExcursionsRouter)
app.include_router(PassExcursionsRouter)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    print("Connect to mongo.")


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


@app.get("/api/v0.1", description="Root endpoint", tags=['BASE'])
async def test():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
