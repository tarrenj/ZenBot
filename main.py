#/usr/bin/env python

import utils
import faq
import os
from slackclient import SlackClient
import responses # All responses go in dictionary format in this file, this is to keep it easy for people to submit PRs with updates/corrections.

# Get the things!
APIToken = os.environ["SLACK_BOT_TOKEN"]
BotName = 'zenbot'
READ_WEBSOCKET_DELAY = 1
SC = SlackClient(APIToken)
BotToken = ''

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
                    # Start checking for things to do
                    if cmd.startswith('faq'):
                        resp = faq.getResp(cmd.split(' ', 1)[1]
                        print resp

# Boiler plate....
if __name__ == "__main__":
    main()
