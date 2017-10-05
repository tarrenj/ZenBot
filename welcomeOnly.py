#/usr/bin/env python

import utils
import joins
import os
from slackclient import SlackClient

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
                # Catch all errrors...
                try:
                    # Check for any user join
                    if post['type'] == 'member_joined_channel':
                        resp = joins.newJoin(utils.getUserName(post['user']), post['channel'])
                        utils.fireAway(resp, post['user'])
                except:
                        # Should eventually send error message to @smrtz
                        e = sys.exec_info()[0]
                        print e

# Boiler plate....
if __name__ == "__main__":
    main()
