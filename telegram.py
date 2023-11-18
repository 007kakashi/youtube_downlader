from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pytube import YouTube

# Replace 'YOUR_BOT_TOKEN' with the token you obtained from BotFather
TOKEN = '6806724985:AAGGanOXIRqj3bhorMXKoSgZN8TtE8kz-VA'

def start(update, context):
    update.message.reply_text("Welcome! Send me a YouTube video URL, and I'll provide you with the video.")

def download_video(update, context):
    # Get the user's message (URL)
    url = update.message.text

    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_stream.download()

        # Send the video to the user
        update.message.reply_video(video_stream.file_path)

    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Add message handler for any text
    message_handler = MessageHandler(Filters.text & ~Filters.command, download_video)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
