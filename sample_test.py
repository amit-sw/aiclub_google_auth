import streamlit as st
import uuid
import os
from dotenv import load_dotenv
from aiclub_auth_lib.oauth import AIClubGoogleAuth

load_dotenv()

auth_config = {
    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
    "redirect_uri": os.getenv("GOOGLE_REDIRECT_URI"),
    "allow_insecure_http": True
}

auth = AIClubGoogleAuth(auth_config)

st.title("Task Management System")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

query_params = st.query_params

if "code" not in query_params:
    st.write("Please log in to access your tasks.")
    #print(f"CODE not in query_params: {query_params}")
    auth_url, state = auth.get_authorization_url()
    st.session_state.state = state
    st.markdown(f"[Login with Google]({auth_url})")
else:
    st.write("Processing login...")
    #print(f"Else Processing login...{query_params}")
    user_info = auth.get_user_info(query_params, st.session_state.get("state"))
    st.success(f"Logged in as {user_info['email']}")
    st.write("You can now view your tasks here.")