import discord
import asyncio
import time
import platform
import os
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot

num1m = 0
num1 = 0
num_1 = 5

num2m = 0
num2 = 0

kk = False

call = '미르'
token = ""
userID = "419440374277341185"

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(50*'-')    
    print("bot call command : ",call)
    print("user call ID : ",userID)
    print(50*'-')

@bot.event  #다 지우고 되돌리기 해볼래요 why 재밌겠다 하다가 발가락으로 컴퓨터 끄면은 작업한거 다날아감 ㅋㅋ루삥뽕 powerof앙대여
async def on_message(message):
    if message.author.bot:
        return None

    global call,userID,kk
    global num1m,num2m,num1,num2,num_1,num_2

    user_id = message.author.id
    channel = message.channel
    
    
        

    if message.content.startswith("!무한!"):
        while True:
            print("맨션이 정상적으로 처리가 되었습니다!")
            print("맨션",num2m,"개 처리 완료 되었습니다")
            await message.channel.send("<@"+userID+">")
            num2m += 1
            time.sleep(0.1)

    if message.content.startswith("!정지!"):
        print("최종적으로 맨션을 종료 하였습니다")
        embed = Embed(title="맨션",description="최종적으로 맨션을 종료 하였습니다", color=0x00aaaa)
        embed.add_field(name="맨션 사용자", value = user_id , inline=False,)
        embed.add_field(name="맨션 사용위치", value = message.channel ,inline=False,)
        embed.add_field(name="맨션 최종 사용량", value = num2m ,inline=False,)
        embed.add_field(name="에러발생시", value = "!미르! 하여 초기화을 해주십시오" ,inline=False,)
        msg = await message.channel.send(embed=embed)
        print(50*"-")
        print("맨션이 정상적으로 처리가 되었습니다!")
        print("맨션",num2m,"개 처리 완료 되었습니다")
        print(50*"-")
        num2m = 0
        num2 = 0
        sys.exit()

    elif message.content.startswith("!"+call+"?"):
        for i in range(num_1):
            print("맨션이 정상적으로 처리가 되었습니다!")
            print("맨션",num1m,"개 처리 완료 되었습니다")
            await message.channel.send("<@"+userID+">")
            print(num1m)
            time.sleep(0.5)
            num1m += 1

            if num1m == num_1:
                print("최종적으로 맨션을 종료 하였습니다")
                embed = Embed(title="맨션",description="최종적으로 맨션을 종료 하였습니다", color=0x00aaaa)
                embed.add_field(name="맨션 사용자", value = user_id , inline=False,)
                embed.add_field(name="맨션 사용위치", value = message.channel ,inline=False,)
                embed.add_field(name="맨션 최종 사용량", value = num1m ,inline=False,)
                embed.add_field(name="에러발생시", value = "!미르! 하여 초기화을 해주십시오" ,inline=False,)
                msg = await message.channel.send(embed=embed)
                print(50*"-")
                print("맨션이 정상적으로 처리가 되었습니다!")
                print("맨션",num1m,"개 처리 완료 되었습니다")
                print(50*"-")
                num1m = 0
                num1 = 0
                break

    if message.content.startswith("!"+call+"!"):
        print("맨션이 정상적으로 처리가 되었습니다!")
        await message.channel.send(call + " 콜 초기화 하었습니다")
        num1m = 0 
        num1 = 0
        num2m = 0 
        num2 = 0



    if message.content.startswith("!도움!"):
        embed = Embed(title="맨션 도배 봇",description="주의 사항 작성 안함", color=0x00aaaa)
        embed.add_field(name="!"+call+"?", value = call+"을 부르기 위한 커멘드 입니다" , inline=False,)
        embed.add_field(name="!무한!", value ="무한으로 호출을 위한 커멘드 입니다" ,inline=False,)
        embed.add_field(name="!"+call+"!", value ="ERROR 210에러가 발생시 !"+call+"!을 하시고 사용해주십시오" ,inline=False,)
        embed.add_field(name="!호스팅!", value ="봇의 호스팅 서버의 상세 설명입니다" ,inline=False,)
        msg = await message.channel.send(embed=embed)

    if message.content.startswith("!호스팅!"):
        embed = Embed(title="맨션 도배 봇 호스팅", color=0x00aaaa)
        embed.add_field(name="운영체제 상세", value = platform.platform() , inline=False,)
        embed.add_field(name="운영체제 이름", value =platform.system() ,inline=False,)
        embed.add_field(name="운영체제 버전", value =platform.version() ,inline=False,)
        msg = await message.channel.send(embed=embed)

bot.run(token)
