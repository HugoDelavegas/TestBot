import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()


print("Lancement du bot")
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot démarré ")
    try:
        syncro= await bot.tree.sync()
        print(f"Commandes slash syncro :{len(syncro)}")
    except Exception as e:
        print(e)

@bot.event
async def on_message(msg: discord.Message):
    if msg.author.bot:
        return
    if msg.content.lower() == 'bonjour':
        channel=msg.channel
        author = msg.author
        await channel.send("Salutation a toi")
        await author.send("Salutation a toi")
    if msg.content.lower() == 'ntm':
        log=bot.get_channel(1317235759505346654)
        await log.send("Attention une personne a utilisé un mot interdit")


@bot.tree.command(name="warning", description="Warn d'un utilisateur")
async def warning(interaction:discord.Interaction,member: discord.Member):
   await interaction.response.send_message("Warning envoyé")
   await member.send("Tu as reçu un warning , fais attention a ce que tu dis")

@bot.tree.command(name="ban", description="Ban d'un utilisateur")
async def ban(interaction:discord.Interaction,member: discord.Member):
   await interaction.response.send_message("Ban envoyé")
   await member.send("Tu as été banni. L'erreur que tu as commise est innaceptable")
   await member.ban(reason="Aucune")

@bot.tree.command(name="kick", description="kick d'un utilisateur")
async def ban(interaction:discord.Interaction,member: discord.Member):
   await interaction.response.send_message("kick envoyé")
   await member.send("Tu as été kick. L'erreur que tu as commise est innaceptable")
   await member.kick()


@bot.tree.command(name="deban", description="deban d'un utilisateur")
async def unban(
    interaction: discord.Interaction,
    user: discord.User
):
    await interaction.guild.unban(user)
    await interaction.response.send_message(f"{user} a été débanni.")

@bot.tree.command(name="test", description="Test du bot")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Voici le test avec un lieb : https://www.youtube.com/@HugoDiv2 ")
bot.run(os.getenv('DISCORD_TOKEN'))