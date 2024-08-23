from colorama import Fore
import requests
import threading
import random
import traceback
def iter(codes):
  proxy = random.choice(proxies).strip()
  polish_num = 0
  while polish_num < len(codes):
      target_code = codes[polish_num]
      try:
        pro_x = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        website = requests.get(f'https://www.discord.com/api/v9/invites/{target_code}',proxies=pro_x)
        polish_num += 1
        code = website.json()['code']
        if code != target_code:
            with open("goodCodes.txt","a+") as sucessfulCodes:
              sucessfulCodes.write(target_code+"\n")
            print(Fore.GREEN+target_code+" GOOD")
        else:
          print(Fore.RED+target_code)
      except Exception as e:
           print(e)
           proxy = random.choice(proxies).strip()



with open("codes.txt","r") as cod:
   codes = cod.readlines()
with open('proxies.txt',"r") as pro:
   proxies = pro.readlines()

first100 = []
for piece in codes:
   first100.append(piece.strip())
   if len(first100)==100:
      threading.Thread(target=iter,args=(first100,)).start()
      first100 = []
threading.Thread(target=iter,args=(first100,)).start()
