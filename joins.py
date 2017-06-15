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
         message = """Welcome to the official Slack for ZenCash!
    
The official links are:
https://github.com/ZenCashOfficial/
https://zencashofficial.io/
                        
We are not affiliated with:
https://github.com/zencashio/
https://zencash.io/

Please remember to be civil, and have a great day!"""
        return message

    # Bottesting
    if channel == "C5JCER3NG":
        pass
