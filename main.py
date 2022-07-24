import discord
import time
import xml.etree.ElementTree as ET

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):  #on new message, read only if message not sent by itself
        if message.author == self.user:
            return
        messagetext = message.content.lower()    #lowercase the message text
        for response in root.findall('response'):
            for element in response:
                if (response.find(element.tag).text in messagetext):    #if the current message contains a trigger word
                    time.sleep(0.5)       #sleep to prevent client side lingering message bug
                    await message.delete()
                    if response.get('text') != '':      #send response if response exists
                        await message.channel.send(response.get('text'))
                    return

    async def on_message_edit(self, oldmsg , message):  #same but for message edits
        if message.author == self.user:
            return
        messagetext = message.content.lower()
        for response in root.findall('response'):
            for element in response:
                if (response.find(element.tag).text in messagetext):
                    time.sleep(0.5)
                    await message.delete()
                    if response.get('text') != '':
                        await message.channel.send(response.get('text'))
                    return

#setup
root = ET.parse('config.xml').getroot()  #parse xml file and store it in memory as 'root'
file = open('token.txt')  #open and read the bot token file
token = file.readline()
print(token)
client = MyClient() #create and run the bot
client.run(token)