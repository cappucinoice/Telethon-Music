import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28441548"))
    API_HASH = os.environ.get("API_HASH", "10a0bc35781dd38b21fc4c3ab3bf103d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6354607928:AAFY0YHib3WjuWfmWdU18vWJFpQgqirMT8w")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJYBuxDOzV2i6tyR73V3KbS0Vv5wsFQKXaS3WOwI61xbhntkHQAJgda0mhWdpu-VlxyLxC3r9smPepXm4dsRUSwSpxQrvuZYSzYS4Sy-gbbd4FuxVmBizW-LMMPF_SGmfZuddp0Yri9Cpe9PtGg8_3l-vrLqrYZ7yw4Z8DZt2n-OvC4hO7QeWkxyDPMNo4j2riKDYzHlb1-tWPl9JCId-wkC0LLQP5jmBF0hrOuC8h1mK2NEAFSqBwLlBF44c_Sefw3WOMWIAI3AEAQK3oBEdxwCVntkFb0nT_r2tJqa5i8cC9qcl_HkUhkPylr1P8nxS3vqhjuPBDjNcuehT3FEYDRW5Tw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "CharviXtc_Bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5601025273")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
