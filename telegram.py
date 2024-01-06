from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pytube import YouTube
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOEKN')



def start(update, context):
    update.message.reply_text("Welcome! Send me a YouTube video URL, and I'll provide you with the video.")

def download_video(update, context):
    url = update.message.text

    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(filename='video')

        # Send the video file to the user
        context.bot.send_document(chat_id=update.message.chat_id, document=open('video.mp4', 'rb'))

    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.text & ~Filters.command, download_video)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
