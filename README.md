# KickbaseAutoOffer
Short quick script for the mobile soccor manager game Kickbase, automatically making an offer to trending players in market.  
**Only use this for your personal learning, you should not use it for anything else!**

## Introduction
This script makes an offer to the next expiring trending player in the kickbase market.

# How to Use
* pip3 install kickbase_api
* Add your credentials in kickbase.login
* OPTIONAL: add your Telegram Bot API Token and chat id for Telegram notification when an offer is made (uncomment notify_market_offer(player))
* Start script

* You can set the price offer by modifying the variable DISCOUNT_FACTOR.
* You can set the sleep timer by modifiying the variable SLEEP_TIMER

All credits go to kevinskyba unofficial [Kickbase-API](https://pypi.org/project/Kickbase-API/)
