from pathlib import Path
from fastapi import FastAPI
from firebase_admin import credentials, initialize_app

from .routes import router

# Initialize Firebase Admin SDK
cred = credentials.Certificate(Path("serviceAccountKey.json"))


def start_app():
    try:
        initialize_app(cred)
        app = FastAPI(
            title="Sneakx",
            description="A backend service for sneakx - a mobile app for commencing sneakers of all kind",
            version="0.1.0",
        )
        app.include_router(router)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

    return app


app = start_app()
