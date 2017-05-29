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
    except KeyError: # Will activate when the user requests a FAQ that isn't below
        return "ERROR: I'm sorry. My responses are limited. You must ask the right questions."

faqs = {
   "why did you kill yourself?": "That, detective, is the right question.",
   "is there a problem with the three laws?": "The three laws are perfect.",
   "wallet": "Eleos is the recommended GUI wallet for Zen, but it's still in early development: https://github.com/zencashio/eleos\nMost of us are using the CLI wallet that's included with the official Zen project:  https://github.com/zencashio/zen",
   "exchange": "Many people here recommend using Bittrex: https://bittrex.com/",
   "translations": "We have several people working on translations, checkout #documentation if you want ot help out!",
   "secure node setup": "Blockops has started writing a guide on this:  https://blockoperations.com/build-zencash-secure-node-part-1-prepare-vps/",
   "about": "This bot was written by tarrenj, and is generously hosted on a VPS provided by our lord and savior joshuayabut.  The source is at https://github.com/tarrenj/ZenBot.  Pull requests are welcome!",
   "chainsplit": "A chain split was done at block 110,000 of the ZCL blockchain on May 18th.  Anyone who held ZCL at that time is able to import their wallet into Eleos to get an equivilent amount of Zen, if your ZCL was on Bittrex, you should see your ZEN in your account.  You are now free to move your ZCL without effecting your ZEN\nAlso see: wallet, launch, coins",
   "launch": "The launch is scheduled for 11:59 UTC, May 30th, 2017.\nhttps://blog.zencash.io/zencash-launch-scheduled-for-2359-utc-tuesday-may-30/",
   "coins": "Where are my coins?  How do I see them?\nIf you had your ZCL in Bittrex on May 18th, your Zen will show up automagically.  If not, you'll need to import your ZCL wallet.dat into a Zen wallet.\nAlso see: wallet",
   "mining": "Currently people are mining on our testnet, the mainnet will be ready when we launch.\nAlso see: pools, launch",
   "pools": "For a list of mining pools that support Zen, see https://bitcoin-and-altcoins.com/list-zen-mining-pools-zencash/\nAlso see: mining",
   "price": "No one can know what Zen will be priced at until after the launch.  Anything else is purly speculation.\nAlso see: launch, coins, chainsplit"
    }
