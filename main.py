from fastapi import FastAPI
from langserve import add_routes
from routes.faiss_router import router as faiss_router


from ai import chain

app = FastAPI()
app.include_router(faiss_router, prefix="/faiss")
add_routes(
    app,
    chain,
    path="/chat"
)