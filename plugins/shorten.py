import requests
import json
from cloudbot import hook

#BattlePluginsAPI key
bp_key = bot.config.get("api_keys", {}).get("battleplugins_key", {})
#BattlePlugins shortner endpoint
bp_shorten = https://api.battleplugins.com/v1/shorturls

@hook.command()
def shorten(text):
    url = args[0]

    payload = {'_key': bp_key, 'url': url}
    r = requests.post(bp_shorten, params=payload)

    message = r.text()

    return "https://bplug.in/" + message
