import requests
import time

Auth = "100" #replace 100 with Authorization Code
ChannelID = "100" #replace 100 with Channel ID

InfLoop = True

#Infinite Loop
while InfLoop = True:
    
    url = "https://discord.com/api/v9/channels/",ChannelID,"/messages"
    
    payload = {
        "content" : ";bump"
    }
    
    headers = {
        "Authorization" : Auth
    }
    
    res = requests.post(url, payload, headers=headers)
    
    time.sleep(21650) #6 Hours 50 Seconds
