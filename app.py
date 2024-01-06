import streamlit as st
import os
from pytube import YouTube

st.title('Welcome To Youtube Video Downloader')
st.header('You Can download Video and Audio of any YT Video')

input_link = st.text_input('Paste Video Link To Download')
selected_option = st.selectbox(label='Select One Option', options=['Video', 'Audio'])
start_download = st.button('Start Download')

if start_download:
    if input_link:
        try:
            yt = YouTube(input_link)

            if selected_option == 'Video':
                video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
                video_file = video_stream.download(output_path='./', filename='video')
                st.success("Video downloaded successfully! Click below to download.")
                with open(video_file, 'rb') as file:
                    st.download_button(label='Click to download', data=file, file_name='video.mp4', mime='video/mp4')
                os.remove(video_file)
            else:
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_file = audio_stream.download(output_path='./', filename='audio')
                st.success("Audio downloaded successfully! Click below to download.")
                with open(audio_file, 'rb') as file:
                    st.download_button(label='Click to download', data=file, file_name='audio.mp4', mime='audio/mp4')
                os.remove(audio_file)
        except Exception as e:
            st.error(f'Error downloading the file: {str(e)}')
    else:
        st.warning('Please provide a valid YouTube video link.')
