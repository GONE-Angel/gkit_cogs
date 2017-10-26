"""What, do you want a..."""

import discord
from discord.ext import commands


class WannaCookie:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='wanna', pass_context=True)
    async def _wanna(self, context):
        """What, do you want a..."""
        if context.invoked_subcommand is None:
            await self.bot.say("Type `[p]help wanna` for info.")

    @wanna.command(name='cookie', pass_context=True)
    async def cookie(self, context, user: discord.Member=None):
        """What, do you want a cookie?"""
        msg = 'What, do you want a cookie {}?'
        if user is not None:
            if user.id == self.bot.user.id:
                user = '... Me??'
                await self.bot.say(msg.format(user) + "\n\nERROR: No, no I do not want a cookie, I am a bot and am not capable of eating cookies.")
            else:
                await self.bot.say(msg.format(user.mention))
        else:
            user = context.message.author
            await self.bot.say(msg.format(user.mention))


def setup(bot):
    bot.add_cog(WannaCookie(bot))
