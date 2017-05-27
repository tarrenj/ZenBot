#/usr/bin/env python

# Module to handle the FAQ function

def getRsp(cmd):
    # Given its own def to keep things standard
    """
    Return the correct value for the given key
    Params: cmd(string):
    Returns: The correct value
    """
    return faqs[cmd]

faqs = {
   "intro": "Hello!  I'm a FAQ bot, type '@faqbot help' and I'll DM you a list of commands",
   "eleos": "Eleos is the recommended wallet for Zen: https://github.com/zencashio/eleos",
   "exchange": "Many people here recommend using Bittrex: https://bittrex.com/",
   "translations": "We have several people working on translations, checkout #documentation if you want ot help out!",
   "secure node setup": "Blockops has started writing a guide on this:  https://blockoperations.com/build-zencash-secure-node-part-1-prepare-vps/",
   "about": "This bot was written by tarrenj, and is generously hosted on a VPS provided by our lord and savior joshuayabut.  The source is at https://github.com/tarrenj/ZenBot.  Pull requests are welcome!",
   "snapshot": "Anyone who had any zClassic at block 111,000 will be given 1 ZenCash for each zClassic they had.  You are free to move your zClassic without effecting your ZenCash",
   "why did you kill yourself?": "That, detective, is the right question.",
   "is there a problem with the three laws?": "The three laws are perfect."
    }
