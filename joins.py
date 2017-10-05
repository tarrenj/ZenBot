#/usr/bin/env python
import utils

# Module to handle join events

def newJoin(user, channel):
    """
    Figure out what to do when a user joins a channel
    Params: user(string), channel(string)
    Returns: none
    """

    message = """
Welcome to the official Slack for ZenCash!


The official links are:
https://github.com/ZenCashOfficial/
https://zencashofficial.io/

NOTICE:
Due to the recent plague that is SlackBot spamming with `/remind`, please do not click any links sent to you in a DM from slackbot.

Additionally, please copy the message to #spam so the Admins can ban the user.

Please remember to be civil, and have a great day!
"""


    # General
    if channel == 'C4QGQ8SEM':
         return message

    # Bottesting
    if channel == "C5JCER3NG":
        return message
