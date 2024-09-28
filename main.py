import dotenv

dotenv.load_dotenv()

from fastapi import FastAPI
from langserve import add_routes

from ai import chat_chain, classifier_chain
from routes.faiss_router import router as faiss_router

app = FastAPI()
app.include_router(faiss_router, prefix="/faiss")

add_routes(
    app,
    chat_chain,
    path="/chat",
)

add_routes(app, classifier_chain, path="/classifier")
