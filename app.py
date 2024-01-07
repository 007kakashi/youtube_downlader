import streamlit as st
import os
from pytube import YouTube
import string

st.title('Welcome To Youtube Video Downloader')
st.header('You Can download Video and Audio of any YT Video')

input_link = st.text_input('Paste Video Link To Download')
selected_option = st.selectbox(label='Select One Option', options=['Video', 'Audio'])
download = st.button('Get')

def sanitize_filename(filename):
    valid_chars = "-_() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)

if download:
    if input_link:
        try:
            yt = YouTube(input_link)
            video_title = sanitize_filename(yt.title)  # Get the video's title and sanitize it

            if selected_option == 'Video':
                video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
                st.info("Downloading video...")
                video_file = video_stream.download(skip_existing=True, filename=video_title)
                st.success("Video downloaded successfully! Click below to download.")
                with open(video_file, 'rb') as file:
                    file_bytes = file.read()
                st.download_button(label='Click to download', data=file_bytes, file_name=f'{video_title}.mp4', mime='video/mp4')
                os.remove(video_file)
            else:
                audio_stream = yt.streams.filter(only_audio=True).first()
                st.info("Downloading audio...")
                audio_file = audio_stream.download(skip_existing=True, filename=video_title)
                st.success("Audio downloaded successfully! Click below to download.")
                with open(audio_file, 'rb') as file:
                    file_bytes = file.read()
                st.download_button(label='Click to download', data=file_bytes, file_name=f'{video_title}.mp4', mime='audio/mp4')
                os.remove(audio_file)
        except Exception as e:
            st.error(f'Error downloading the file: {str(e)}')
    else:
        st.warning('Please provide a valid YouTube video link.')
