import streamlit as st
from utils import download_video_audio, classify_accent

st.title( "Accent Classifier" )
url = st.text_input( "Enter video URL" )

if st.button( "Analyze Accent" ):
    if not url:
        st.warning( "Please enter a URL first." )
    else:
        audio_path = download_video_audio( url )
        accent, confidence = classify_accent( audio_path )

        st.subheader( "Accent Classification" )
        st.write( f"Accent: **{accent}**" )
        st.write( f"Confidence: **{confidence}%**" )