from chromadb import Client, Settings

def get_chroma():
    client = Client(
        Settings(
            chroma_api_impl="chromadb.api.rust.RustBindingsAPI",
            persist_directory="./chroma"
        )
    )

    # Create collection if it doesn't exist
    try:
        collection = client.get_collection("rag_insight")
    except Exception:  # NotFoundError
        collection = client.create_collection("rag_insight")

    return client
