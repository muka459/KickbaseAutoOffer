from kickbase_api.kickbase import Kickbase
from kickbase_api.models.player import Player
import time
import requests

headers = {
    'Content-Type': 'application/json',
}

EXPIRY_VALUE = 1800
SLEEP_TIMER = 600
DISCOUNT_FACTOR = 0.9902

kickbase = Kickbase()
user, leagues = kickbase.login("<LOGIN-MAIL-ADRESSE>", "LOGIN-PASSWORD>")

def notify_market_offer(player: Player):
   #Telegram notification
   subject = "Making offer for " + player.first_name + " " + player.last_name
   offer = "Offer: " + str(int(player.market_value * DISCOUNT_FACTOR))
   telegram_request = '{"chat_id": "<CHAT-ID>", "text": "%s %s", "disable_notification": false}' % (subject, offer)
   requests.post('https://api.telegram.org/bot<API-TOKEN>/sendMessage', headers=headers, data=telegram_request)

while(True):
   market = kickbase.market(leagues[0].id)
   my_info = kickbase.league_me(leagues[0].id)

   for player in market.players:
      if (player.expiry < EXPIRY_VALUE and player.market_value_trend == 1):          
         if ((my_info.budget - player.market_value * DISCOUNT_FACTOR) > -(my_info.team_value * 0.33)):
            kickbase.make_offer(int(player.market_value * DISCOUNT_FACTOR), player.id, leagues[0].id)
            #notify_market_offer(player)
            time.sleep(player.expiry)
         else:
            print("Not enough budget to place the order")

   print("Sleep until new run...")
   time.sleep(SLEEP_TIMER)



