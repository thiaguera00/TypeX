import discord
from discord.ext import commands

class Photos(commands.Cog):
    """ Work with Photos """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="photo")
    async def get_random_image(self,ctx):
            url_image = "https://source.unsplash.com/random"

            embed_image = discord.Embed(
                title = "Random Photos Search",
                description = "é tudo de uma API não vai achando que é personagem 2D aqui",
                color = 0x0000FF
            )

            embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed_image.set_footer(text="Estou desempregado e desesperado " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

            embed_image.add_field(name= "API", value= "Peguei de uma API")
            embed_image.add_field(name="Parâmetros", value="{largura}/{altura}")

            embed_image.add_field(name="Exemplo", value=url_image, inline=False)

            embed_image.set_image(url=url_image)

            await ctx.send(embed=embed_image)

    

def setup(bot):
    bot.add_cog(Photos(bot))

