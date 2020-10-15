import discord


def Embed(description=None, image=None, title="Identity", color=0xeb4034, footer="ismaeelakram.com | Mahjestic#9700"):
    return discord.Embed(description=description, image=image, title=title, color=color).set_footer(text=footer)


def SoftErrorEmbed(error):
    return discord.Embed(title="Oops!", description=error, color=0xd13f3f)
