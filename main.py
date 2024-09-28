import dotenv
dotenv.load_dotenv()

from fastapi import FastAPI
from langserve import add_routes
from routes.faiss_router import router as faiss_router


from ai import chain
from ai.classifier import classifier_chain

app = FastAPI()
app.include_router(faiss_router, prefix="/faiss")

add_routes(
    app,
    chain,
    path="/chat",
)

add_routes(
    app,
    classifier_chain,
    path="/classifier"
)