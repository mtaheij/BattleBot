from cloudbot import hook

@hook.command()
def lDucks(text):
    return "lDucks, I lost my virginity, can I have yours?"

@hook.command()
def clovis(text):
    return "I hear Cl loves the French!"

@hook.command()
def help(text):
    if not text:
        return " Please help us help you! Paste your log and clearly describe your problem. Thank you!"
    else:
        return "(" + text + ") Please help us help you! Paste your log and clearly describe your problem. Thank you!"

@hook.command()
def ask(text):
    if not text:
        return " If you have a question, please just ask it. Don't look for staff or topic experts or ask if people are awake or available. Just ask the question to the channel straight out, and wait patiently for a reply. "
    else:
        return "(" + text + ") If you have a question, please just ask it. Don't look for staff or topic experts or ask if people are awake or available. Just ask the question to the channel straight out, and wait patiently for a reply."

@hook.command()
def log(text):
    if not text:
        return " Stop your server. Now, start your server, let it load completely, then stop it. Please copy what's in 'logs/latest.log' and paste it on http://gist.github.com and post the link in the channel."
    else:
        return "(" + text + ") Stop your server. Now, start your server, let it load completely, then stop it. Please copy what's in logs/latest.log' and paste it on http://gist.github.com and post the link in the channel."

@hook.command("config", "baconfig")
def config(text):
    if not text:
        return " Please paste the content of your config.yml located in your plugins/BattleArena/ on http://gist.github.com and post the link in this channel."
    else:
        return "(" + text + ") Please paste the content of your config.yml located in your plugins/BattleArena/ on http://gist.github.com and post the link in this channel."

@hook.command()
def newconfig(text):
    if not text:
        return " Please delete the config.yml (and make a backup) located in plugins/BattleArena/, then stop your server. Now, start your server, let it load completely. You should now have the latest config."
    else:
        return "(" + text + ") Please delete the config.yml (and make a backup) located in plugins/BattleArena/, then stop your server. Now, start your server, let it load completely. You should now have the latest config."

@hook.command("version", "v", "vabout")
def version(text):
    if text in ['BattleArena', 'BA', 'battlearena', 'ba']:
        return "Please tell us your Server Variant (Spigot, Sponge, Bukkit, etc) and your BattleArena version as well as your current WorldGuard, WorldEdit, and BattleTracker Version's."
    elif text in ['BattleTracker', 'BT', 'battletracker','bt', 'statistics']:
        return "Please tell us your Server Variant (Spigot, Sponge, Bukkit, etc) and your BattleTracker version. If you are using BattleArena as well, please let us know what version's BattleArena, WolrdGuard, and WorldEdit."
    elif not text:
        return "Please let us know what version plugin you are currently running."
    else:
        return "Please tell us your Server Variant (Spigot, Sponge, Bukkit, etc) and your " + text + " version as well as BattleArena, BattleTracker, WorldEdit, and WorldGuard."

@hook.command("ticket", "t")
def ticket(text):
    if text in ['BattleArena', 'BA', 'battlearena', 'ba']:
        return "(BattleArena) Please create a ticket here: https://goo.gl/tNGE2Z and make sure to follow these guidelines: https://goo.gl/a84Qr8. Thank you for helping us make BattleArena better!"
    elif text in ['BattleTracker', 'BT', 'battletracker','bt', 'statistics']:
        return "(BattleTracker) Please create a ticket here: https://goo.gl/Ye8KnR and make sure to follow these guidelines: https://goo.gl/a84Qr8. Thank you for helping us make BattleTracker better!"
    elif not text:
        return "Please create a ticket on our GitHub at https://github.com/BattlePluginsDev."
    else:
        return "(" + text + ") Please create a ticket here: https://goo.gl/o5UIKe and make sure to follow these guidelines: https://goo.gl/a84Qr8. Thank you!"




