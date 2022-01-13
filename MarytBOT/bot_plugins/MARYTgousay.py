from typing import List
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from random import randint

__plugin_name__ = '苟语录'
__plugin_usage__ = '''
输入苟语录随机抽一手苟佬的语录截图
'''
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

@on_command('苟语录',aliases=('冷知识'))
async def _(session: CommandSession):
    MGS = await gousay()
    await session.send(MGS)

@on_natural_language(keywords={'苟语录'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '苟语录')