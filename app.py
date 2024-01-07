# from constant import audio_downloader,video_downloader,playlist_downloader
import streamlit as st
import os
from pytube import YouTube
from flask import Flask,request,render_template,send_file

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_link', methods=['POST'])
def process_link():
    if request.method == 'POST':
        user = request.form['videoLink']
        selected= request.form['formatSelect']
        
        try:

            if selected == 'audio':
                audio_file=YouTube(user)
                audio_download=audio_file.streams.get_audio_only()
                audio=audio_download.download(skip_existing=True)
                return send_file(audio, as_attachment=True)
            else:
                video_file=YouTube(user)
                video_download=video_file.streams.get_highest_resolution()
                video=video_download.download(skip_existing=True)
                return send_file(video, as_attachment=True)

        except Exception as e:
            raise str(e)


if __name__=='__main__':
    app.run(debug=True)
