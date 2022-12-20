from beanie import init_beanie, Document
#from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

from server.models.product_review import ProductReview

async def init_db():
    client = AsyncIOMotorClient("mongodb://fastapidb:tsIsh9SvEnjBDcyqtuOZLSPPf59CumRdYRv2OH14ceb9eILqOvzJaiIhUe93eC4gBqFaSlzy6t0GACDbvW2dBQ==@fastapidb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@fastapidb@")        
    await init_beanie(database=client.cosmosmongodb, document_models=[ProductReview])