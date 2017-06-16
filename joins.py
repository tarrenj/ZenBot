#/usr/bin/env python
import utils

# Module to handle join events

def newJoin(user, channel):
    """
    Figure out what to do when a user joins a channel
    Params: user(string), channel(string)
    Returns: none
    """
    # General
    if channel == 'C4QGQ8SEM':
         message = "Welcome to the official Slack for ZenCash!\n\nThe official links are:\nhttps://github.com/ZenCashOfficial/\nhttps://zencashofficial.io/\n\nWe are not affiliated with:\nhttps://github.com/zencashio/\nhttps://zencash.io/\n\nPlease remember to be civil, and have a great day!"
        return message

    # Bottesting
    if channel == "C5JCER3NG":
        pass
