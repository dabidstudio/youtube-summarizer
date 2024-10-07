import streamlit as st

# Input for YouTube video URL
video_url = st.text_input(" YouTube video URL:")

if video_url:
    st.video(video_url)