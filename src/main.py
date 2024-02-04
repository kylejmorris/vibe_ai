# main.py
import os
import config
import chromadb 
# from services import *

# client = chromadb.HTTPClient(config.DATABASE_URL)

# client = chromadb.PersistentClient(config.DATABASE_PATH)

##### SETUP #####

from db_add_data import add_document_to_collection

# get the text from kyle_linkedin.txt 
person_name="Kyle Morris"
text_source="LINKEDIN"
with open("people_data/kyle_linkedin.txt", "r") as file: 
    test_text = file.read()
    print(test_text)
add_document_to_collection(test_text, person_name, text_source)

# # get the text from kyle_linkedin.txt 
# person_name="Steve Frey"
# text_source="LINKEDIN"
# with open("people_data/sf_linkedin.txt", "r") as file: 
#     test_text = file.read()
#     print(test_text)
# add_document_to_collection(test_text, person_name, text_source)
