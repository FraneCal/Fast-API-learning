from fastapi import FastAPI
from app.core.config import setup_cors
from app.routers import items

def create_app() -> FastAPI:
    app = FastAPI(
        title="My FastAPI Project",
        version="0.1.0"
    )

    # Setup CORS
    setup_cors(app)

    # Health check route
    @app.get("/", tags=["Health"])
    def root():
        return {"message": "FastAPI project is running 🚀"}

    # Include routers
    app.include_router(items.router)

    return app

app = create_app()
