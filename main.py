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
    if question.startswith("faq"):
        try:
            option = question.split(' ', 1)[1]
            rsp = faq.getRsp(option)
            return rsp
        except:
            return '(Probably) Invalid FAQ entry.  See: https://github.com/tarrenj/ZenBot/blob/master/faq.py'

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
                    # Who are we flagging in the response?  (If it's a DM, fireAway wont bother flagging)
                    target = utils.getUserName(post['user'])
                    if cmd.startswith('give'):
                        # Make sure we're giving to a valid user
                        target = utils.getUserName(cmd.split(' ', 1)[1].split(' ', 1)[0])
                        # Get everything after the given name
                        cmd = cmd.split(' ', 1)[1].split(' ', 1)[1].strip()
                    resp = getAnswer(cmd)
                    utils.fireAway(resp, target, post['channel'])


# Boiler plate....
if __name__ == "__main__":
    main()
