
# Telegram Auto Post

You can create a Telegram bot with this project.  This will allow you to create posts that can be sent to a group in a loop or at a given time.
## Acknowledgement

 - Python-telegram-bot

## Environment Variables

To run this project, you will need to add the following environment variables to config.toml

#### Bot_token

you will get a bot token when you make a bot with https://t.me://botfather

#### Owner

This is your id not the username to get it use https://t.me://getmy_idbot
## Deployment

###Notes
 - buy paid if you want to remove my name in code.
 - don't remove my name and sell the code.

To deploy this project run

 - pip install -r requirement.txt - python postbot.py

For any help join the [telegram group](htpps://t.me/nimmadev)
## Documentation

### Commands

- /start - the bot and displays buttons for making and editing posts.
- /send - after making a post you will get a post number. Use /send post_number interval_time [time in seconds] . it will resend post in loop of interval_time
- /time - use this to send post once after a wait time. /time post_number time . example: /time 87 65 this will send post after 1 hour 5 minutes
- /stop - stop a running post /stop post_number
- /rk - remove buttons if you used the /start command in group
- /cancel - use this if you want to stop making posts in the middle
### Note 

/send command is meant to be used in group don't send it to bot

## FAQ

### What is the post number?

You will get it after you make a post in the bot. It is a special tag for that particular post.

### What is the interval time?

You can set a time at which bot will repost example : /send 76 60 this will send post id 76 after 60 seconds again and again till You use /stop 76

### how to send single post?

use /time
example /time postid 60
this will send post after one hour

### How can i hide your name?
Buy a personal bot contact me

### Why does it not work in channels?

Buy a personal bot it will work in channel also
