# surfbot-python
Basic discord bot that will display current map as bot status.


Prerequisites:

Python 3.6.6 or 3.7(requires some dependencies that are out of date on pip)

python-valve 0.2.1

discord.py


Installation:

1. Install python
2. Install modules
3. Change server ip and port in script to your server
4. Change channel id to specific channel (or comment out if you dont want that)
5. Change token to your bot token
6. Run script

If everything is done correctly then you should be golden. If you're running 3.7 and are running into syntax errors with async you will need to get latest commit for discord.py which will fix issues with discord.py that are not yet present in pip. That's it, its a super basic bot that I did on a whim. I'll probably end up adding more to it later but feel free to integrate into your own. As of note python-valve querier does not work with all games but usually will work with source servers.
