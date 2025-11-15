from chromadb import Client
from chromadb.config import Settings
from app.config import CHROMA_DB_DIR

def get_chroma():
    client = Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=CHROMA_DB_DIR
    ))
    return client
