import os


class Config(object):
    API_HASH = os.environ.get("9758292b691b82c5915900c506fcbe83")
    BOT_TOKEN = os.environ.get("5848537364:AAEwt5ED7zOcTYOHBJdn1jMmJ1GJ8po3rv4")
    TELEGRAM_API = os.environ.get("26367674")
    OWNER = os.environ.get("5697445137")
    OWNER_USERNAME = os.environ.get("Khushveersinghdeora")
    PASSWORD = os.environ.get("qwerty1234")
    DATABASE_URL = os.environ.get("mongodb+srv://khushveersinghdeora67:qwerty1234@cluster0.10mfif5.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-100 + 1446516132")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
