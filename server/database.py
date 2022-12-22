from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from server.models.product_review import ProductReview

async def init_db():
     client = AsyncIOMotorClient('mongodb://fastapidb:A1SYbIH88yxlxk4FxwWG9yiaksEyxrb0gZ5zQqPabTXlvAnRVndY6U2LBlU0XK2FcgJy8o6TzA8bACDb34kNwQ==@fastapidb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@fastapidb@')
     await init_beanie(database=client.cosmosmongodb, document_models=[ProductReview])