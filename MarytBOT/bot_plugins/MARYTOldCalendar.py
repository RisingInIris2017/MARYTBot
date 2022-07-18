from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.message import MessageSegment
from asyncio import sleep

import time
from random import randint

__plugin_name__ = 'MARYTOldCalendar'
__plugin_usage__ = '''
用法：
输入“老黄历”随机抽取一对宜忌事项
'''
goodList = ["向阿苟表白","东风牛逼！","和弧弧贴贴","和吼姆一起提桶跑路","摸服","造自动化流水线","种小麦","种马铃薯","种胡萝卜","养动物","打末影龙","吃饱喝足","摸了","和Gastant交流自动化心得","建设方便玩家的基础设施","和axty一起整活"]
badList = ["上原神贴吧PVP","和微博女拳对线","上知乎键政","看嘭哈布打手冲","在pixiv找色图","看真夏夜的银梦","看潮汕英豪传","看cookie⭐","当乐子人","在别的MC群打M服的广告","在社交平台挂人","提问群公告上已经有的内容"]
async def todayGoodAndBad():
    timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    goodThing = goodList[randint(0,len(goodList)-1)]
    badThing = badList[randint(0,len(badList)-1)]
    return "现在是："+timeNow+"，\n"+"今日老黄历：\n"+"宜："+goodThing+"\n"+"忌："+badThing+"\n"

@on_command('黄历', permission=lambda sender: sender.from_group(640614812) and (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    todayGAB = await todayGoodAndBad()
    randomPicIndex = randint(0, 30)         
    if session.event.group_id == 640614812:
        await session.send(MessageSegment.text(todayGAB) + MessageSegment.text("【今日苟语录】\n") + MessageSegment.image('file:///' + f"C:/Users/东风佬/Desktop/newMarytRobot/MarytBOT/语录/" + str(randomPicIndex) + ".jpg"))
        await sleep(120)
    
@on_natural_language(keywords={'黄历'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '黄历')

