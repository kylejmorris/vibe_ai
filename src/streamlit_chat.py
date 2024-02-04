import os 
import sys
import streamlit as st
import requests
import json
#from openai import OpenAI
import openai
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.path.abspath('../'))

from openai_functions import create_chat_completion, create_streaming_chat_completion
from db_query_data import query_db


############### Vars ############ 
RETRIEVAL_RELEVANCE_THRESHOLD=0.3
NUM_RETRIEVAL_RESULTS = 3

############ Local server ############
CONNECTION_URL = "localhost"
CONNECTION_PORT = 5000

############ Streamlit Setup ############
# layout widemode
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("<h1 style='text-align: center;'>🌎 Vibe AI 🌎</h1>", unsafe_allow_html=True)


############ Body, Sidebar Columns ############
st.markdown("---")  # Horizontal line for separation
body,sidebar = st.columns(2)  # Create two columns
body.markdown("### Chat")
sidebar.markdown("### Results")

############ Initialize chat message history ############

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": " "},
        {"role": "assistant", "content": "👥 🔎 Who do you want to find?"}
    ]
if "response" not in st.session_state:
    st.session_state["response"] = None

messages = st.session_state.messages
messages = [msg for msg in messages if msg["role"] != "system"]


for msg in messages:
    # st.chat_message(msg["role"]).write(msg["content"])
    body.chat_message(msg["role"]).write(msg["content"])


############ Main conversation and retrieval loop ############

if user_prompt := st.chat_input(placeholder="Find me something"):
    with st.spinner("👀"):
        

        ########### Get and filter retrievals/images ###########
        retrievals = query_db(user_prompt, num_results=2) 
        # print('\n-----retreivals-----\n',retrievals)

        # Filter out retrievals with distance greater than THRESHOLD 
        # filtered_retrievals = [doc for doc, dist in zip(retrievals['documents'][0], retrievals['distances'][0]) if dist > RETRIEVAL_RELEVANCE_THRESHOLD]
        filtered_retrievals = retrievals['documents'][0]

        # retrievals['documents'][0] = filtered_retrievals
    
        print('\n-----retreivals-----\n',retrievals)
        # Display the page title as a clickable link

        retrieval_and_metadata_list = []
        for i, doc in enumerate(filtered_retrievals):
            metadata = retrievals['metadatas'][0][i]
            retrieval_and_metadata_list.append(f"Metadata: Name - {metadata['person_name']}, Source - {metadata['text_source']}, Profile Snippet: {doc}")
            print('meadata: ', metadata)
        
        print('\n\n=========retrieval_and_metadata_list: ', retrieval_and_metadata_list)

        #### Get LLM response 
        network_mixer_prompt = "You are helping the user to look through their network and identify relevant people. Please see their query. Then there will be snippets from the profiles and private messages of different people in the user's network. Each snippet contains that person's NAME, the SOURCE (like Linkedin, facebook, twitter, etc) and then the profile snippet. Look through this list, identify the person's name, and describe a list of their experiences that are relevant to the user's query. \n\nUser Query: " + user_prompt + "\n\nRetrieved Documents: \n" + "\n".join(retrieval_and_metadata_list)
        print('\n\nnetwork_mixer_prompt: ', network_mixer_prompt)

        st.session_state.messages.append({"role": "user", "content": network_mixer_prompt})
        # st.chat_message("user").write(user_prompt)
        body.chat_message("user").write(user_prompt)

        ##### Display retrieved images #### 
        # sidebar.write(retrievals) ## displays the raw text 
        for i in range(len(retrievals['documents'][0])):
            metadata = retrievals['metadatas'][0][i]
            person_name = metadata['person_name']
            text_source = metadata['text_source']
            if metadata is None:
                continue 

            # Display the document
            sidebar.write(retrievals['documents'][0][i])

            sidebar.markdown(f"[Name: {person_name}  Source: ({text_source})]")


    ########### Display streaming LLM text response ###########
    with st.chat_message("assistant"):
        this_response_message = ""
        message_placeholder = body.empty()

    for response in create_streaming_chat_completion(messages=st.session_state.messages):
        print('response: ', response)
        this_response_message += (response.choices[0].delta.content or "")
        print('this_response_message: ', this_response_message)
        message_placeholder.markdown(this_response_message + " ")
        # message_placeholder.markdown(f"<p style='font-size:16px;'>{this_response_message}</p>", unsafe_allow_html=True)


    st.session_state.messages.append({"role": "assistant", "content": this_response_message})

    print ('message_placeholder: \n ', message_placeholder, '\n\nsession-state-messages: \n', st.session_state.messages, '\n\nresponse: \n', response)


