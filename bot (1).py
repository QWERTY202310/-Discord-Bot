import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    activity = discord.Game(name="help")
    await client.change_presence(activity=activity)
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    embed = None

    if message.content.startswith('領地指令'):
        # 建立嵌入式訊息
        embed = discord.Embed(title="領地系統基本指令", description="建立、管理及傳送至領地的指令")
        embed.add_field(name="建立領地", value="1. 使用木鋤左鍵點選第一個角標，右鍵點選第二個角標來選擇區域。\n2. 執行 /res create [領地名] 指令來建立一個名為 [領地名] 的領地。")
        embed.add_field(name="傳送至領地", value="/res tp [領地名]：傳送至指定領地。")
        embed.add_field(name="管理領地", value="/res list：顯示所有您擁有的領地。\n/res remove [領地名]：移除指定領地。\n/res removeall：移除所有領地。")
        embed.add_field(name="設定領地權限", value="/res set：將指定領地設定為您的領地（您必須站在領地內）。\n/res pset [玩家名] [權限] [true/false/remove]：設定指定領地對指定玩家的權限。")
        embed.add_field(name="轉移領地", value="/res give [領地名] [玩家名]：將指定領地轉移給指定玩家（您必須是領主，且該玩家必須在線上）。")
        
    elif message.content.startswith('help'):
        # 建立嵌入式訊息
        embed = discord.Embed(title="伺服器基本指令", description="以下是機器人可用的指令：")
        embed = discord.Embed(title="伺服器基本指令", description="以下是機器人可用的指令：")
        embed.add_field(name="1.領地指令", value="顯示領地系統的基本指令。")
        embed.add_field(name="2.傳送指令", value="顯示傳送系統的基本指令。")
        
    elif message.content.startswith('傳送指令'):
        # 建立嵌入式訊息
        embed = discord.Embed(title="傳送指令", description="以下是傳送系統可用的指令：")
        embed.add_field(name="隨機傳送", value="/rtp")
        embed.add_field(name="傳送至其他玩家", value="/tpa [玩家名]")
        embed.add_field(name="其他玩家至傳送你", value="/tphere [玩家名]")
        embed.add_field(name="確認傳送", value="/tpyes")
        embed.add_field(name="拒絕傳送", value="/tpno")

    
        
    if embed:
        await message.channel.send(embed=embed)

client.run('token')
