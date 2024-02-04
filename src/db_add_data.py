import uuid 
from init_chroma_client import CHROMA_CLIENT, QA_EMBED_FUN 
from config import COLLECTION_NAME, DATABASE_LOCAL_PATH


############ Helpers ############
def add_text_to_collection(chroma_client, collection_name, documents, metadatas, ids,  embed_func): 
    collection = chroma_client.get_collection(name=collection_name, embedding_function=embed_func)
    result = collection.add(
        documents=documents,
        # embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    return result

############ Add to db ############
### Format data from URL list 

def chunk_long_document(text)->list[str]: 
    # UPDATE:  define a chunking function how you want here 
    # hacky split every 4 sentences 
    sentences = text.split('.')
    chunk_size = 3 # sentences 
    chunks = ['.'.join(sentences[i:i+chunk_size]) + '.' for i in range(0, len(sentences), chunk_size)]
    return chunks
    # return [text] 

def add_document_to_collection(text, person_name="Kyle Morris", text_source="LINKEDIN"):
    """Main function to take someone's long e.g. linkedin data and add it to the collection"""

    text_chunks = chunk_long_document(text)
    append_results = [] 
    for chunk in text_chunks: 
        result = add_text_to_collection(
            CHROMA_CLIENT, 
            collection_name=COLLECTION_NAME, 
            documents=[chunk], 
            metadatas=[
                {"person_name": person_name, 
                 "text_source": text_source}
                 ], 
            ids=[str(uuid.uuid4())], 
            embed_func=QA_EMBED_FUN
        )
        print(result)
        append_results.append(result)
    return append_results

