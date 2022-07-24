# Discord-auto-moderation-bot
A simple xml configured self hosted discord bot that parses messages in all visible channels, deleting messages with unwanted substrings, and responding with a message.  
# What is this?
A project born out of necessity. I needed a simple self-hosted bot that removed unwanted messages, and replied appropriately with a response based on what specifically triggered the message removal. 

# How do I run this?
You can either use the executable I provided, or run/compile it yourself.

# How do I configure this?
Make sure you have created a discord bot, and have a bot token. This is not hard to do, and there are lots of tutorials on how to do this. Once you have your bot token, paste it into a file called "token.txt" and place that file in the same directory as the executable, or wherever you happen to be running the python file. Next, copy the config.xml I have provided as a framework to get started at configuring the bot yourself. 

# How does the configuration work?
The xml file contains a list of repsonses that the bot will reply with, and within each response is a trigger for that reponse. Responses can have multiple triggers, which all must be named differently. Messages from the channel are made lowercase automatically, so every trigger should also be lowercase. If you do not want the bot to respond at all, and just delete the message, set text equal to an empty string or "". 

