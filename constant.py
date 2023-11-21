import pytube
from pytube import Playlist
from flask import Flask
import os


def audio_downloader(url):
    video=pytube.YouTube(url)
    stream= video.streams.get_audio_only()
    return stream.download(skip_existing=True)

def video_downloader(url):
    video=pytube.YouTube(url)
    stream= video.streams.get_highest_resolution()
    return stream.download(skip_existing=True)

def playlist_downloader(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        stream = video.streams.get_audio_only()
        stream.download(skip_existing=True)

