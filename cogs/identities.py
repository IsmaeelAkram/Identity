import discord
from discord.ext import commands
from utils import embed, config

class Identities(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def remove(self, ctx:commands.Context):
        user = ctx.author

        user_identity = config.get_user_identity(user.id)
        if user_identity is None:
            await ctx.channel.send(embed=embed.SoftErrorEmbed("You don't have an ID! Create one with `id create`."))
            return

        result = config.delete_identity(user.id)
        if result:
            await ctx.channel.send(embed=embed.Embed(title="Deleted :x:", description="Your ID has been deleted. To create a new one, use `id create`."))
        else:
            await ctx.channel.send(embed=embed.SoftErrorEmbed(f"A database error seems to have occurred! Please report this in our Discord server.\n**Error:** `{result}`"))

    @commands.command()
    async def show(self, ctx: commands.Context):
        user = ctx.author
        user_identity = config.get_user_identity(user.id)
        if user_identity is None:
            await ctx.channel.send(embed=embed.SoftErrorEmbed("You don't have an ID! Create one with `id create`."))
            return
        
        await ctx.channel.send(
            embed=embed.Embed(
                title=user_identity.name, 
            )
            .set_thumbnail(url=user.avatar_url)
            .set_footer(text=f"Requested by {ctx.author.name}")
            .add_field(name="Username", value=f"{user.name}#{user.discriminator}")
            .add_field(name="Created At", value=user.created_at)
            .add_field(name="Birthday", value=user_identity.birthday)
            .add_field(name="Socials", value=user_identity.socials)
        )

    @commands.command()
    async def create(self, ctx: commands.Context):
        if(config.get_user_identity(ctx.author.id) is not None):
            await ctx.channel.send(embed=embed.SoftErrorEmbed("You already have an ID! If you want to remove this ID, use `id remove`."))
            return

        def check(msg: discord.Message):
            if(msg.author == ctx.author):
                return True
            else:
                return False

        step_1 = await ctx.channel.send(embed=embed.Embed(title="Step 1/3 🔨", description=f"Hey, <@{ctx.author.id}>! I'm going to help you create your own ID on Discord! Firstly, say the name that you would like to put on your ID.").set_footer(text="Type cancel to end the creation process."))
        
        name = await self.bot.wait_for('message', check=check)

        if('cancel' in name.content):
            await ctx.channel.send(embed=embed.Embed(title="Cancelled :x:", description="The creation process has been cancelled."))
            return

        if(len(name.content) > 18):
            await ctx.channel.send(embed=embed.SoftErrorEmbed("Your name can only be 18 characters or less! Please run the `id create` command again."))
            return
        
        step_2 = await ctx.channel.send(embed=embed.Embed(title="Step 2/3 🔨", description=f"Your name will be set as **{name.content}**. Now, tell me your social media accounts. (You can use [Markdown](https://www.markdownguide.org/cheat-sheet/) to style it however you want.)").set_footer(text="Type cancel to end the creation process."))

        socials = await self.bot.wait_for('message', check=check)

        if('cancel' in socials.content):
            await ctx.channel.send(embed=embed.Embed(title="Cancelled :x:", description="The creation process has been cancelled."))
            return

        step_3 = await ctx.channel.send(embed=embed.Embed(title="Step 3/3 🔨", description=f"Now, tell me your birthday in whatever format you want. (1/1/2000 / January 1st, 2000)").set_footer(text="Type cancel to end the creation process."))

        birthday = await self.bot.wait_for('message', check=check)

        if('cancel' in socials.content):
            await ctx.channel.send(embed=embed.Embed(title="Cancelled :x:", description="The creation process has been cancelled."))
            return

        await ctx.channel.send(embed=embed.Embed(title="Confirmation 📝", description="That's it! Now, look over the information your provided and check if its accurate. Reply with `yes` if it's correct and `no` if it's incorrect.").set_footer(text="Type cancel to end the creation process."))

        confirmation = await self.bot.wait_for('message', check=check)

        if('cancel' in confirmation.content):
            await ctx.channel.send(embed=embed.Embed(title="Cancelled :x:", description="The creation process has been cancelled."))
            return

        if('yes' in confirmation.content):
            pass
        elif 'no' in confirmation.content:
            await ctx.channel.send(embed=embed.Embed(title=None, description="Okay, we have stopped the creation process because the information is incorrect. Try again with `id create`."))
            return

        result = config.create_identity(ctx.author.id, name.content, socials.content, birthday.content)

        if result:
            await ctx.channel.send(embed=embed.Embed(title="Done! ✅", description="Your ID has been made! View it with `id show`!"))
        else:
            await ctx.channel.send(embed=embed.SoftErrorEmbed(f"A database error seems to have occurred! Please report this in our Discord server.\n**Error:** `{result}`"))