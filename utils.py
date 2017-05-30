#/usr/bin/env python

from slackclient import SlackClient
import os

APIToken = os.environ["SLACK_BOT_TOKEN"]
SC = SlackClient(APIToken)
import re

def getUserToken(username):
    """
    Gets the id of the given user, returns None if invalid user
    Params: user(string): Can be either username or token, with or without '@'
    Returns: the id(string)
    """
    # Remove '@, <, >' if required
    # For some reason, this doesn't work...
    username = re.sub('<>@', '', username)
    api_call = SC.api_call("users.list")
    if api_call.get('ok'):
        people = api_call.get('members')
        for user in people:
            if 'name' in user:
                # If the given username is either this users id or username
                if username == user.get('name') or username == user.get('id'):
                    return user.get('id')

def getUserName(uuid):
    """
    Gets the username of a given user, None if invalid user
    Params: id(string): The id of the user
    Returns: the id(string)
    """
    # Remove '@, <, >' if required
    # For some reason, this doesn't work...
    uuid = re.sub('<>@', '', uuid)
    api_call = SC.api_call("users.list")
    if api_call.get("ok"):
        people = api_call.get('members')
        for user in people:
            # If the given ID is either this users id or name
            if uuid == user.get('id') or uuid == user.get('name'):
                return user.get('name')

def fireAway(message, target, channel=None):
    """
    Send a message flagging someone, DM it if no channel is given
    Params: message: what we're yelling
            target:  who we're yelling it at
            channel: where we're yelling it
    """
    # If no channel is given, DM to target
    if channel is None:
        SC.api_call("chat.postMessage", text=message, channel=target, as_user=True)
    else:
        SC.api_call("chat.postMessage", text=(target + ": " + message), channel=channel, as_user=True)
