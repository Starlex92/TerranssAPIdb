from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from server.models.product_review import ProductReview

async def init_db():
     client = AsyncIOMotorClient('mongodb://fastapidb:jxoYvEc8y85qlJuMCrGWC6Huy6fXepDL66zBLaMQF9DRgTjZWx02B6Sr3Kr0687f3ut9aKQ0HKoQACDbUMTutw==@fastapidb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@fastapidb@')
     await init_beanie(database=client.cosmosmongodb, document_models=[ProductReview])