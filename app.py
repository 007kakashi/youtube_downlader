from constant import audio_downloader,video_downloader,playlist_downloader
import streamlit as st
import os
# import tkinter as tk
# from tkinter import filedialog

# def select_download_location():
#     root= tk.Tk()
#     root.withdraw()
#     folder_selected = filedialog.askdirectory()
#     return folder_selected

# def get_audio_download_link(file_path):
#     return f'<a href="{file_path}" download>Click here to download your audio</a>'

# def get_video_download_link(file_path):
#     # return f'<a href="{file_path}" download>Click here to download your video</a>'


st.header('Youtube Video and Audio Downloader')

user=st.text_input('Paste Your Link Here')

selection=st.selectbox('Please Select Format',['Video','Audio'])



download=st.button("Download")

if download and user:
    if selection == 'Audio':
        st.text("Download started for Audio...")
        audio_file_path = audio_downloader(user)
        st.text("Download completed for Audio!")
        # st.markdown(get_audio_download_link(audio_file_path), unsafe_allow_html=True)
    else:
        st.text("Download started for Video...")
        video_file_path = video_downloader(user)
        st.text("Download completed for Video!")
        # st.markdown(get_video_download_link(video_file_path), unsafe_allow_html=True)

