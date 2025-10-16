import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='Dso')  
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='demons_welcome') 
    if channel is not None:  
        await channel.send(
            f"Welcome, {member.mention}, to {member.guild.name}! 🩸\n"
            "The battlefield awaits… Only the brave survive! ⚔️⚔️\n"
            "📝 Register here: <#1383002628211871784>\n"
            "📖 Read the rules: <#1382772448914575360>\n"
            "📢 Stay updated: <#1382774081522237540>\n"
            "🏅 May the strongest rise and claim their glory!"
        )
bot.run('MTQyNDQzOTcwOTk0NTMwMzE2Nw.GMN8S4.EmIy0UsF461cTs2KTjlOMdrC0WSIYUQHyFPUJM')
