import requests
import json
from cloudbot import hook

@hook.command()
def bplug(text, bot):
    #BattlePlugins shortner endpoint
    bp_shorten = "https://api.battleplugins.com/v1/shorturls"
    #BattlePluginsAPI key
    bp_key = bot.config.get("api_keys", {}).get("battleplugins_key", {})

    payload = {'_key': bp_key, 'url': text}
    r = requests.post(bp_shorten, data=payload)

    response = r.json()
    print(r)

    if response.get("success"):
        return "https://bplug.in/" + response["success"]["message"]
    else:
        return "Failed to shorten URL: " + response["error"]["message"]
