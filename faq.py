#/usr/bin/env python

# Module to handle the FAQ function

def getRsp(cmd):
    # Given its own def to keep things standard
    """
    Return the correct value for the given key
    Params: cmd(string):
    Returns: The correct value
    """
    try:
        return faqs[cmd]
    except KeyError:
        return "I'm sorry. My responses are limited. You must ask the right questions."

faqs = {
   "why did you kill yourself?": "That, detective, is the right question.",
   "is there a problem with the three laws?": "The three laws are perfect.",
   "wallet": "Eleos is the recommended GUI wallet for Zen, but it's still in early development: https://github.com/zencashio/eleos\nMost of us are using the CLI wallet that's included with the official Zen project:  https://github.com/zencashio/zen",
   "exchange": "Many people here recommend using Bittrex: https://bittrex.com/",
   "translations": "We have several people working on translations, checkout #documentation if you want ot help out!",
   "secure node setup": "Blockops has started writing a guide on this:  https://blockoperations.com/build-zencash-secure-node-part-1-prepare-vps/",
   "about": "This bot was written by tarrenj, and is generously hosted on a VPS provided by our lord and savior joshuayabut.  The source is at https://github.com/tarrenj/ZenBot.  Pull requests are welcome!",
   "chain split": "A chain split was done at block 110,000 of the ZCL blockchain.  Anyone who held ZCL at that time is able to import their wallet into Eleos to get an equivilent amount of Zen.  You are now free to move your ZCL without effecting your ZEN",
   "launch": "The launch is schedualed for May 30th, 2017.  The exact time has not been decided yet."
    }
