#/usr/bin/env python

from slackclient import SlackClient

def getUserToken(username):
    """
    Gets the id of the given user, returns None if invalid user
    Params: user(string): Can be either username or token, with or without '@'
    Returns: the id(string)
    """

def fireAway(message, target, channel=None):
    """
    Send a message flagging someone, DM it if no channel is given
    Params: message: what we're yelling
            target:  who we're yelling it at
            channel: where we're yelling it
    """

