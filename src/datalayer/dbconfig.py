from fastapi import FastAPI 
from tortoise.contrib.fastapi import register_tortoise

async def configure_db(app: FastAPI):
    register_tortoise(
        app=app,
        config={
            'connections': {
                #'default': 'postgres://postgres:qwerty@localhost:5432/events'
                'default': 'sqlite://db.sqlite3'
            },
            'apps': {
                'models': {
                    'models': [
                        'src.datalayer.models.user'
                    ],
                    'default_connection': 'default',
                }
            }

        }
    )