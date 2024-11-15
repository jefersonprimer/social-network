from fastapi import FastAPI
from src.datalayer.dbconfig import configure_db

def create_app():
    app = FastAPI()
    configure_db(app)

    return app

app = create_app()

@app.get('/')
async def home():
    return {'status': '200'}