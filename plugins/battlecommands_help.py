from cloudbot import hook
from cloudbot.util import formatting

@hook.command()
def bphelp (text, chan, conn, bot, notice, message, has_permission):
    if chan[:1] == "#":
        notice(" --- Welcome to BattleBot BattlePlugin Help Menu (v1.0) --- ")
        notice("  Commands        | Params          | What it does:")
        notice("- .help           | none / username | Tells users to describe their problem clearly with as much detail as possible.")
        notice("- .ask            | none / username | Tells users to cut straight to the question and wait patiently.")
        notice("- .log            | none / username | Asks user to paste their log to GitHub Gist and post link in chat.")
        notice("- .config         | none / username | Asks user to paste their config to GitHub Gist and post link in chat.")
        notice("- .newconfig      | none / username | Asks user to paste their log to GitHub Gist and post link in chat.")
        notice("- .version        | none / plugin   | Asks user what version plugin(s) they are using.")
        notice("- .ticket         | none / plugin   | Asks user to report their issue to GitHub tickets.")
    else:
        message(" --- Welcome to BattleBot BattlePlugin Help Menu (v1.0) --- ")
        message("  Commands        | Params          | What it does:")
        message("- .help           | none / username | Tells users to describe their problem clearly with as much detail as possible.")
        message("- .ask            | none / username | Tells users to cut straight to the question and wait patiently.")
        message("- .log            | none / username | Asks user to paste their log to GitHub Gist and post link in chat.")
        message("- .config         | none / username | Asks user to paste their config to GitHub Gist and post link in chat.")
        message("- .newconfig      | none / username | Asks user to paste their log to GitHub Gist and post link in chat.")
        message("- .version        | none / plugin   | Asks user what version plugin(s) they are using.")
        message("- .ticket         | none / plugin   | Asks user to report their issue to GitHub tickets.")
