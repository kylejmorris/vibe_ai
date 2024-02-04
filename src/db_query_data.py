from init_chroma_client import CHROMA_CLIENT, QA_EMBED_FUN 
from config import COLLECTION_NAME

############ Query document ############
def query_db(query_text, num_results=2): 
    print("query text ",query_text)

    try: 
        collection = CHROMA_CLIENT.get_collection(name=COLLECTION_NAME, embedding_function=QA_EMBED_FUN) 

        results = collection.query(
            query_texts=[query_text],
            n_results=num_results
        )
        return results 
    except Exception as e: 
        print (f"error querying collection. \n with {COLLECTION_NAME}, {query_text} \n", e)
        return None

from pprint import pprint
results = query_db("stablecoin.")
pprint (results) 
print(len(results['documents']))
for r in results['documents'][0]: 
    pprint(r) 
    print("\n\n")