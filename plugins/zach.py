import requests
import json
from cloudbot import hook

@hook.command()
def shorten(text, bot):
    #BattlePlugins shortner endpoint
    bp_shorten = "https://api.battleplugins.com/v1/shorturls"
    #BattlePluginsAPI key
    bp_key = bot.config.get("api_keys", {}).get("battleplugins_key", {})

    payload = {'_key': bp_key, 'url': text}
    r = requests.post(bp_shorten, params=payload)

    response = r.json()

    if 'message' in response:
        return "https://bplug.in/" + response['message']
    else:
        return "An error has occured :("
