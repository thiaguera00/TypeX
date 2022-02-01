from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
class Manager(commands.Cog):
    """ Manager the Bot """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"pai ta on!{self.bot.user}")

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return

        if "palavrão" in message.content:
            await message.channel.send(
                f"Por favor, {message.author.name}, não ofenda os demais usúarios!"
            )
            await message.delete()
        elif "palavrão" in message.content:
            await message.channel.send(
                f"Por favor, {message.author.name}, não ofenda os demais usúarios!"
            )
            await message.delete()
        elif "palavrão" in message.content:
            await message.channel.send(
                f"Por favor, {message.author.name}, não ofenda os demais usúarios!"
            )
            await message.delete()
        elif "palavrão" in message.content:
            await message.channel.send(
                f"Por favor, {message.author.name}, não ofenda os demais usúarios!"
            )
            await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos, digite !help para vê todos comandos")
        elif isinstance(error,CommandNotFound):
            await ctx.send("O comando não existe, digite !help para vê todos comandos")
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))
