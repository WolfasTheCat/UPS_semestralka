from enum import Enum


class States(Enum):
    LOGGING = -1
    LOGGED = 0
    WANNA_PLAY = 1
    DISCONNECTED = 2
    YOU_PLAYING = 3
    OPPONENT_PLAYING = 4