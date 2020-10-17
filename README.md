<h1><center>Identity</center></h1>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

### A simple way to give people IDs on Discord!

# Introduction
Identity is a bot that gives people the chance to introduce themselves, their social media, and more **across servers**. All servers the bot is in will carry the same data about every user so you don't have to create a new ID every single time.

## Get started
[Click here](https://discord.com/api/oauth2/authorize?client_id=766353177226248253&permissions=8&scope=bot) to add the hosted bot to your Discord server. That's it...

# Commands
So that was all. People can create their own IDs and look at other people's IDs now. But how?

### `id create`
The create command allows people to create their own IDs with the creation wizard.

### `id show @User`
The show command shows anyone's ID. If you leave the mentioned user empty, it will show your own ID.

### `id remove`
The remove command allows people to delete their IDs. This will remove it from our database and allow you to create a new one.

# Self hosting
To self host this bot, you'll need a PostgreSQL database and a Discord application. Once you have these, make a file in the root project directory called **`.env`**. Put this in the file,
```ini
token="DISCORD_BOT_TOKEN"
postgres_connection_string="POSTGRESQL_CONNECTION_STRING"
```
And replace the variables with your own token and connection string. Then, install the dependencies with:
```
pip install -r requirements.txt
```
And run it with:
```
python start.py
```
It will ask you if you want to run in production or development. If you choose to run in development, make sure you have [nodemon](https://www.npmjs.com/package/nodemon) installed globally on your computer.

**You're all set!**