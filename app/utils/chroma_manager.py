# app/utils/chroma_manager.py
from chromadb import Client, Settings  # <- correct import

def get_chroma():
    client = Client(
        Settings(
            chroma_api_impl="chromadb.api.rust.RustBindingsAPI",
            persist_directory="./chroma"
        )
    )
    return client
