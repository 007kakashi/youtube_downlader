from constant import audio_downloader,video_downloader,playlist_downloader
import streamlit as st
import os
from pytube import YouTube
from flask import Flask,redirect,url_for,request,render_template,send_file

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
                audio=audio_downloader(user)
                return send_file(audio, as_attachment=True)
            else:
                video=video_downloader(user)
                return send_file(video, as_attachment=True)

        except Exception as e:
            raise str(e)


if __name__=='__main__':
    app.run(debug=True)
