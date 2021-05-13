import enum

Games = ['Fortnite', 'PUBG', 'COD', 'GTA-V', 'Rainbow-Six', 'Pocket-Tanks', 'FIFA25']

class Internal_Error(enum.Enum):
    NOT_DEFINED="command not defined"

class Enums(enum.Enum):
    tc_id = "TRACKER_CHANNEL_ID"
    wc_id = "WELCOME_CHANNEL_ID"
    token = "TOKEN"