#/usr/bin/env python

import utils
import faq
import os
from slackclient import SlackClient

# Get the things!
APIToken = os.environ["SLACK_BOT_TOKEN"]
BotName = 'zenbot'
READ_WEBSOCKET_DELAY = 1
SC = SlackClient(APIToken)
BotToken = ''

def getAnswer(question):
    """
    Get's the desired response for a given command, except the 'give' comand, that's done before this...
    Param question(string): the command
    Return answer(string): the desiered response
    """
    # Check for broken command
    if question is None:
        return 'Error: Give me something to work with.'
    # Sols
    if question.startswith("sols"):
        try:
            # Just here for now...
            raise Exception('sols')
        except:
            return 'ERROR: Something happened with sols command.'
    # Get current block height
    if question.startswith("height"):
        try:
            # Just here for now...
            raise Exception('height')
        except:
            return 'ERROR: Something happened with height command.'
    # FAQ command
    if question.startswith("faq"):
        try:
            option = question.split(' ', 1)[1]
            rsp = faq.getRsp(option)
            return rsp
        except:
            return 'ERROR: Invalid FAQ entry.  See: https://github.com/tarrenj/ZenBot/blob/master/faq.py'
    # Get current exchange rate command
    elif question.startswith("EXC"):
        try:
            return 'ERROR: Not yet written... Sorry'
        except:
            pass
    # Gotta keep people happy
    elif question.startswith("gotta keep"):
        try:
            # Get the given user
            user = '@chronic'
            # And keep them happy
            return user + " can blow me."
        except:
            pass
    # Help command
    elif question.startswith("help"):
        try:
            # Eventually this should be dynamic
            return 'Currently, I can only do faq and give.  FAQ is at https://github.com/tarrenj/zenbot/blob/master/faq.py'
        except:
            pass
    # Unknown command
    return 'ERROR: That\'s not a thing yet.\nAlso see: help'

def main():
    """
    Where all the magic happens
    Params: None
    Returns: None
    """
    # Start off by getting the token.
    global BotToken
    BotToken = utils.getUserToken(BotName)
    
    if SC.rtm_connect():
        while True:
            # This triggers me
            for post in SC.rtm_read():
                if 'text' in post and post['text'].startswith('!'):
                    print 'Ahh, I\'m triggered!'
                    print post
                    # Get an easy name for the post (minus the bang)
                    cmd = post['text'][1:]
                    # Who are we flagging in the response? fireAway won't flag if DM
                    if cmd.startswith('give'):
                        # Make sure we're giving to a valid user
                        try:
                            target = '@' + utils.getUserName(cmd.split(' ', 1)[1].split(' ', 1)[0])
                        except IndexError:
                            target = None
                        # Get everything after the given name
                        try:
                            cmd = cmd.split(' ', 1)[1].split(' ', 1)[1].strip()
                        except:
                            cmd = None
                    else:
                        target = '@' +  utils.getUserName(post['user'])
                    if cmd is not None:
                        resp = getAnswer(cmd)
                    else:
                        resp = "ERROR: cmd was None"
                    # Flag the poster if error
                    if resp.startswith('ERROR:'):
                        target = '@' + utils.getUserName(post['user'])
                    try:
                        utils.fireAway(resp, target, post['channel'])
                    except:
                        resp = 'ERROR: something weird happened...'
                        utils.fireAway(resp, post['user'], post['channel'])


# Boiler plate....
if __name__ == "__main__":
    main()
