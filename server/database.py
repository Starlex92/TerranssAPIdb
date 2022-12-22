from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from server.models.product_review import ProductReview

async def init_db():
     client = AsyncIOMotorClient('mongodb://fastapidb:gtchzYV1S9qdTF5fczkFGey4ZN0J0taeymK9UDUrBxjjHYbVvxxARci8Zp5j66gEyPakMd5vuJO8ACDbINHjbw==@fastapidb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@fastapidb@')
     await init_beanie(database=client.cosmosmongodb, document_models=[ProductReview])