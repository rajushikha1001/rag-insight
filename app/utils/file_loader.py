import os

def load_documents(directory):
    docs = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if filename.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs
