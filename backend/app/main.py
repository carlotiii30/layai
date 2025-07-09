from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api import routes
from app.core.config import add_cors

app = FastAPI(
    title="Layai API",
    description="AI-Powered Editorial Layout Assistant",
    version="0.1.0",
)

add_cors(app)

app.include_router(routes.router)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
