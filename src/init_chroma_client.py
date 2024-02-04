# use dotenv to load environemnt 
import os
import sys
import uuid
import logging

from dotenv import load_dotenv
load_dotenv()

from config import COLLECTION_NAME, DATABASE_LOCAL_PATH

####################################
## Local Sqlite3 replacement for Chroma (if running locally on Intel Mac) ##
print('CURRENT_HOST: ', os.environ.get('CURRENT_HOST'))
import pysqlite3
sys.modules['sqlite3'] = pysqlite3
sys.modules['sqlite3'].sqlite_version_info = (3,35,0)
print(sys.modules['sqlite3'])

####################################
import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings
####################################

def setup_local_chroma_client(): 
    CHROMA_CLIENT = chromadb.PersistentClient(DATABASE_LOCAL_PATH, Settings(allow_reset="True"))
    print('chroma heartbeat: ', CHROMA_CLIENT.heartbeat()) # returns a nanosecond heartbeat
    print('chroma host: ', DATABASE_LOCAL_PATH)
    return CHROMA_CLIENT

###############################################

def get_chroma_client():
    return setup_local_chroma_client()

def get_embed_function(): 
    QA_EMBED_FUN = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="multi-qa-MiniLM-L6-cos-v1")
    return QA_EMBED_FUN

CHROMA_CLIENT = get_chroma_client()
QA_EMBED_FUN = get_embed_function()