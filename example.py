from telethon.sync import TelegramClient, events
import time

"""
api_id & api_hash are provided by Telegram when you create an application.
Get them: https://docs.telethon.dev/en/latest/basic/signing-in.html
"""      
api_id = 0000000 # your api_id.
api_hash = '################################' # your api_hash (must be inserted between '').

"""
The first parameter is the .session file name (absolute paths allowed)
You can also write your api_id and api_hash below.
"""
with TelegramClient('name', api_id, api_hash) as client:
   """
   Prints the current date and the two strings described on the terminal.
   It's a good idea to use prints in such a way that you always understand the state
   where the system is located.
   """
   print(time.asctime(), '-', 'Auto-replying...')

   """
   Server waits for a message from the client. When someone writes you on Telegram 
   a comparison is made on what has been written and what has been written as the first argument.

   The pattern argument can be constructed using regular expressions, like this
   you have the maximum management of the strings. To know more (https://duckduckgo.com/?q=regular+expression+python&t=h_&ia=web or https://duckduckgo.com/?q=regular+expression+%22telethon%22&t=h_&ia=web)
   Ad esempio: (?i) means that starts case-insensitive mode.
                ^ e $ identify the beginning and the end of the string on which to perform the analysis.
   In this example anyone who writes help, regardless of the characters (help, HElP, hElP etc.) will receive the automatic reply
   described in event.reply. ^ and $ they allow only those who write help to reply and that's it as a message:
      - help (ok)
      - Hello, help (no)
      - hELP (ok)
      - Yo help (no)

   time.sleep(n) is the time in n seconds to wait before the automatic reply is sent. It can also be omitted but
   adding a waiting time between replies creates a better conversational effect replied to an immediate reply.

   event.reply is the actual response message. Here, too, you can format the message (https://core.telegram.org/api/entities).
   For example **Hi** writes Hi in Bold format, \n allows new line etc.

   The second parameter of NewMessage allows you to evaluate the messages received only for private Telegram chats. If omitted then
   anyone writing "help" in any conversation (private chat, group, channels and more) will receive the scheduled automatic reply.
   More here (https://docs.telethon.dev/en/latest/modules/events.html)
   """
   @client.on(events.NewMessage(pattern='(?i)^help$', func=lambda e: e.is_private))
   async def handler(event):
      time.sleep(1) 
      await event.reply('**Hi there!**🧘‍♀️\nhow are you?')      
  
   """
   With link_preview = False, the message received as a reply will not automatically load the preview link.
   Using doge you will only receive the link https://i.gifer.com/3O6sm.gif without any preview, instead with doges the gif will be shown.
   """   
   @client.on(events.NewMessage(pattern='(?i)doge', func=lambda e: e.is_private))
   async def handler(event):
   	time.sleep(1) 
   	await event.reply('https://i.gifer.com/3O6sm.gif',link_preview=False)      

   @client.on(events.NewMessage(pattern='(?i)doges', func=lambda e: e.is_private))
   async def handler(event):
      time.sleep(1) 
      await event.reply('https://i.gifer.com/3O6sm.gif') 

   """
   Through the pipe it's possible to manage different messages that must have the same answer.
   """
   @client.on(events.NewMessage(pattern='(?i)^wow$|^ToTheMoon$', func=lambda e: e.is_private))
   async def handler(event):
   	time.sleep(1) 
   	await event.reply('woof 🐶') 

   """
   Yes, they also work with emoji. 
   """
   @client.on(events.NewMessage(pattern='(?i)^🧐$|^❤️$', func=lambda e: e.is_private))
   async def handler(event):
   	time.sleep(1) 
   	await event.reply('👀') 
	   
   client.run_until_disconnected()
   print(time.asctime(), '-', 'Stopped!')





