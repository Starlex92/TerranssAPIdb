from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from server.models.product_review import ProductReview

async def init_db():
     client = AsyncIOMotorClient('mongodb://fastapidb:QfWdAihu8b6BUcVYKGBuaOstrQJWUHGEIe8gXLCDQhEfEh4lByVh7XdbR88qQtpooUdro0Yr8lcyACDbYJxoaw==@fastapidb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@fastapidb@')
     await init_beanie(database=client.cosmosmongodb, document_models=[ProductReview])