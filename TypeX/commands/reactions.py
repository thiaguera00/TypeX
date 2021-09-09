from discord.ext import commands

class Reactions(commands.Cog):
    """ Work with Reactions"""
    def __init__(self, bot):
        self.bot = bot

    #Reações para Cargos

    @commands.Cog.listener()
    async def on_reaction_add(reaction, user):
            print(reaction.emoji)
            if reaction.emoji == "🥳":
                role = user.guild.get_role(885166748070977546)
                await user.add_roles(role)
            elif reaction.emoji=="🤠":
                role = user.guild.get_role(885166780492955738)
                await user.add_roles(role)
            elif reaction.emoji=="😁":
                role = user.guild.get_role(885183431724654682)
                await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))

