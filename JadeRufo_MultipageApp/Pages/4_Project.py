import streamlit as st

st.title("📂 Projects")

project = st.selectbox("Choose a Project", [
    "Sports Activities",
    "School activities and Assignment"
    
])

st.success(f"You selected: {project}")
