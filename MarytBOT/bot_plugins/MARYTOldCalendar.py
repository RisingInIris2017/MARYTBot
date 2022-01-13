from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot import on_natural_language, NLPSession, IntentCommand
import time
from random import randint

__plugin_name__ = 'MARYTOldCalendar'
__plugin_usage__ = '''
用法：
输入“老黄历”随机抽取一对宜忌事项
'''
goodList = [
    "向阿苟表白"
    ,"东风牛逼！"
    ,"和弧弧贴贴"
    ,"和吼姆一起提桶跑路"
    ,"摸服"
    ,"造自动化流水线"
    ,"种小麦"
    ,"种马铃薯"
    ,"种胡萝卜"
    ,"养动物"
    ,"打末影龙"
    ,"吃饱喝足"
    ,"摸了"
    ,"和Gastant交流自动化心得"
    ,"建设方便玩家的基础设施"
    ,"和axty一起整活"
    ]
badList = [
    "上原神贴吧PVP"
    ,"和微博女拳对线"
    ,"上知乎键政"
    ,"看嘭哈布打手冲",
    "在pixiv找色图"
    ,"看真夏夜的银梦"
    ,"看潮汕英豪传"
    ,"看cookie⭐"
    ,"当乐子人"
    ,"在别的MC群打M服的广告"
    ,"在社交平台挂人"
    ,"提问群公告上已经有的内容"
    ]
List = [
    '[CQ:image,file=http://vps.g-c-z.cc/marytbot/1.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/2.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/3.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/4.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/5.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/6.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/7.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/8.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/9.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/10.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/11.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/12.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/13.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/14.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/15.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/16.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/17.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/18.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/19.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/20.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/21.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/22.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/23.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/24.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/25.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/26.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/27.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/28.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/29.png]'
    ,'[CQ:image,file=http://vps.g-c-z.cc/marytbot/30.png]'
    ]
    
async def gousay():
    Gousay = List[randint(0,len(List)-1)]
    return "【今日苟语录】"+Gousay

async def todayGoodAndBad():
    timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    goodThing = goodList[randint(0,len(goodList)-1)]
    badThing = badList[randint(0,len(badList)-1)]
    MGS = await gousay()
    return "现在是："+timeNow+"，\n"+"今日老黄历：\n"+"宜："+goodThing+"\n"+"忌："+badThing+"\n"+MGS

@on_command('黄历',aliases=('老黄历'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    todayGAB = await todayGoodAndBad()
    await session.send(todayGAB)

@on_natural_language(keywords={'黄历'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '黄历')
