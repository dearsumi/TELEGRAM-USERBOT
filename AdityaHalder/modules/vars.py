import os

from os import getenv
from dotenv import load_dotenv
from pyrogram import filters


if os.path.exists("Internal"):
  load_dotenv("Internal")


class Config(object):
    # REQUIRED VARIABLES
    API_ID = int(getenv("API_ID", 20098819))
    API_HASH = getenv("API_HASH", "2545d49cea8894d513726649b1bd5a1f")
    BOT_TOKEN = getenv("BOT_TOKEN", "7529913491:AAG43T71V7p6-cqFDRAlItKhTzucd1dUcws")
    STRING_SESSION = getenv("STRING_SESSION", "BQEyrwMAscGp1Qb6RcS_8wVRPZhRMOhqW4pg_GfO4AkrToQDjBgN1v6Y_pO2Su8fo25oOPgoW5gOKtlAzjwavVtab5ticg0Y645AS7LVeN50GkMXPjNq6UAQLmAsfwNCPKI0570z1bS2ZhtqES2sM72SJPxdpsD8zYjYFd588nSAwOm-5f0HDiXKli885rsh6gPPEQ2JyakWjZQyPu29ZZtwDpmvGiI58hkNd1Vta4urRgxjVNuYsWqQPDFFm5anG3C51BBGJikxx8paHPlepM0ZbW7JUHJwvi2CmEhkx9otzt7GXQo16uUOIxOQPBFtDe98RL-X5ecoqVtBKTw6p3puTtwCUgAAAAHXQT_PAA")
    MONGO_DATABASE = getenv("MONGO_DATABASE", "mongodb+srv://Alisha:Alisha123@cluster0.yqcpftw.mongodb.net/?retryWrites=true&w=majority")
  
    # OPTIONAL VARIABLES
    SESSION_STRING = getenv("SESSION_STRING", None)
    COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! > *").split())
    USERBOT_PICTURE = getenv("USERBOT_PICTURE", None)
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1002435242326))
  
  
    # do not edit these variables
    COMMAND_HANDLERS = []
    PLUGINS = {}
    SUPUSER = filters.me
    SUDOERS = filters.user([])
    CRAIDUB = filters.user([])
    LRAIDUB = filters.user([])
    RRAIDUB = filters.user([])
    GBANSUB = filters.user([])
    GMUTEUB = filters.user([])
    #######################################
    for x in COMMAND_PREFIXES:
        COMMAND_HANDLERS.append(x)
    COMMAND_HANDLERS.append('')
    #######################################


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys()]
all_vals = [i for i in Config.__dict__.values()]

