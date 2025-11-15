from chromadb.client import Chroma
from chromadb.config import Settings

def get_chroma():
    # Create Chroma client with new API
    client = Chroma(
        persist_directory="./chroma",
        settings=Settings(
            chroma_api_impl="chromadb.api.rust.RustBindingsAPI"
        )
    )
    return client
