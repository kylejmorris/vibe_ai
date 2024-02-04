from init_chroma_client import CHROMA_CLIENT, QA_EMBED_FUN, Settings, chromadb
from config import COLLECTION_NAME

####################################
### HELPERS 
def create_collection(client, collection_name): 
    collection = CHROMA_CLIENT.create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}, # l2 is the default
        embedding_function=QA_EMBED_FUN, 
        
    )
    print ("client heartbeat: " , client.heartbeat())
    return collection

def reset_client(client): 
    r = client.reset() # Empties and completely resets the database. ⚠️ This is destructive and not reversible.
    return r

####################################
#### CREATE / RESET. 
#### Caution: this erases your entire database

DB_ACTION = input("Enter CREATE or RESET. Optionally add a NAME if CREATING collections.  ")
action, *name_parts = DB_ACTION.split()
if action == "CREATE":
    if not name_parts:
        print(create_collection(CHROMA_CLIENT, COLLECTION_NAME))
        pass
    else:
        print(create_collection(CHROMA_CLIENT, name_parts[0]))
elif action == "RESET":
    print(reset_client(CHROMA_CLIENT))
