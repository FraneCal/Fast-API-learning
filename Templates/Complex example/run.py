import uvicorn
from app.db import models, database

# Create tables
models.Base.metadata.create_all(bind=database.engine)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
