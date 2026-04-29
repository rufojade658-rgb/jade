import streamlit as st

st.title("👩 About Me")

st.image("pages/jade.jpg", width=200, caption="Jade🌸")
st.write("""
My name is Jade. I am passionate, creative, and hardworking.
I am very passionate in everything that I love to do. If you're interested to know me, this page if for you!
""")

st.header("My Personal information")

st.subheader("📌 Basic Details")

st.write("🎂 Birthday:April 9, 2005")
st.write("😊 Age:21  years old")
st.write("📍 Location: Masbate Philippines")


st.subheader("🏳️ My Hobbies")
st.markdown("""
- 🏐Playing Volleyball 
- 🎬 Watching Movies  
- 🎶Listening to Music
            
- 🕺Dancing
""")


st.subheader("🌟 Personality")

st.write("""
✔ Friendly  
✔ Hardworking  
✔ Positive Thinker  
✔ Goal Oriented
""")


st.subheader("🚀 Future Dream")

st.warning("To finish my studies and become stable in life.")


