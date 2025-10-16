from discord.ext import commands = 
bot = commands.bot(command_perfix='Dso')
@bot.event async def on_member_join(member):chanel=discord.utils.get(member.guild.text_chanels,name='demons_welcome') if channel is not none:await chanel.send(f"
Welcome, {member.mention}, to {member.guild.name}! 🩸
The battlefield awaits… Only the brave survive! ⚔️⚔️ 
📝 Register here: <#1383002628211871784> 
📖 Read the rules: <#1382772448914575360> 
📢 Stay updated: <#1382774081522237540> 
🏅 May the strongest rise and claim their glory!")
