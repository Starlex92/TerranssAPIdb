from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from server.models.product_review import ProductReview

async def init_db():
     client = AsyncIOMotorClient('mongodb://fastapidb:44M46W831ougjIIOeUBQuUKXolHS16FXDes3S6jwzmSNZD6Vkp63OOANUCfIkBzsaJSpwYT7OJ80ACDbr0Ffqw==@fastapidb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@fastapidb@')
     await init_beanie(database=client.cosmosmongodb, document_models=[ProductReview])