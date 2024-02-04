from streamlit_auth0_component import login_button
import streamlit as st
from dotenv import load_dotenv
import os
import json

load_dotenv()

clientId = os.environ.get("AUTH0_CLIENT_ID")
domain = os.environ.get("AUTH0_DOMAIN")

st.title("Welcome to Auth0-Streamlit")

user_info = login_button(clientId=clientId, domain=domain)
with st.echo():
    if user_info:
        tmp_user_info = user_info.copy()
        tmp_user_info["token"] = (
            user_info["token"][:10] + "..." + user_info["token"][-10:]
        )
        st.write(f'Hi {tmp_user_info["nickname"]}')
        user_json = json.dumps(tmp_user_info, indent=4)
        st.code(user_json, language="json")
        # st.write(user_info) # some private information here

if not user_info:
    st.write("Please login to continue")
