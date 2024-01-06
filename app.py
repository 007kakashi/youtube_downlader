import streamlit as st
import os
from pytube import YouTube

st.title('Welcome To Youtube Video Downloader')
st.header('You Can download Video and Audio of any YT Video')

input_link = st.text_input('Paste Video Link To Download')
selected_option = st.selectbox(label='Select One Option', options=['Video', 'Audio'])
download = st.button('Download')

if download:
    try:
        if selected_option == 'Video':
            video_file = YouTube(input_link)
            video_download = video_file.streams.get_highest_resolution()
            video_download.download(filename='video')
            st.success("Video downloaded successfully! Click below to download.")
            with open('video.mp4', 'rb') as file:
                st.download_button(label='Click to download', data=file, file_name='video.mp4', mime='video/mp4')
            os.remove('video.mp4')
        else:
            video_file = YouTube(input_link)
            video_download = video_file.streams.get_audio_only()
            video_download.download(filename='audio')
            st.success("Audio downloaded successfully! Click below to download.")
            with open('audio.mp4', 'rb') as file:
                st.download_button(label='Click to download', data=file, file_name='audio.mp4', mime='audio/mp4')
            os.remove('audio.mp4')
    except Exception as e:
        st.error('Error downloading the file. Please check the provided link.')
