from discord.ext import commands
import discord
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
class Talks(commands.Cog):
    """ Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="dm", help="Envia uma mensagem privada"
        )
    async def secret(self,ctx):
            try:
                await ctx.author.send("Olá, desculpa incomodar, só vim agradecer por deixar eu monitorar o servidor :)")
                await ctx.author.send("Da uma passada no meu Git: https://github.com/thiaguera00")
            except discord.errors.Forbidden:
                await ctx.send(
                    "Não posso te mandar DM :(, habilite receber mensagens de qualquer (Opções => Privacidade e Segurança)"
                    )

def setup(bot):
    bot.add_cog(Talks(bot))

