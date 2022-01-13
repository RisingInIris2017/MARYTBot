import nonebot
import time
from datetime import datetime
from random import randint
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

__plugin_name__ = 'MARYTTimeReport'
__plugin_usage__ = '''
用法：
半点报时。
'''

# 变量和函数
# 完美教室部分的随机
tipsList = [
'怪物在被打的时候有几率召唤援助，如果你的装备优良，这是刷杀敌数的好机会！',
'当心突然出现在脚下的末影螨。',
'喝下鸟之祝福药水之前务必把血量回满！',
'当你想不起来模组怎么玩的时候，往群里发“教程”两个字试试！',
'''在打开工作台的情况下用JEI查询配方，
点击配方右下角的+号按钮，
JEI会将背包中的材料在工作台自动摆好！''',
'斩杀之证和耀魂之瓶的配方并不真的消耗拔刀剑，只是从拔刀剑上提取指定数量的杀敌数和耀魂数而已！',
'如果你看到这条游戏贴士，说明你今天应该给M服提供一条属于你的游戏贴士。',
'''如果你不想跑图寻找林地府邸，
可以在车万女仆祭坛上召唤唤魔者，
召唤配方可以通过在JEI中
查询魔力粉尘的用途看到。'''
]

async def randomTips():
    tip = tipsList[randint(0,len(tipsList)-1)]
    return "【阿苟的完美教室】\n"+tip
# 苟语录部分的随机
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
# 定时部分
# 整点报时
@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        time = f'现在是{now.hour}点整。\n'
        if now.hour <= 5 or now.hour >= 22:
            time += '夜深了，宝友们！\n'
        tips = await randomTips()
        MGS = await gousay()
        fullMessage = time + tips +"\n"+MGS
        await bot.send_group_msg(group_id=640614812,
                                 message=fullMessage)
    except CQHttpError:
        pass

#半点报时
@nonebot.scheduler.scheduled_job('cron', hour='*',minute=30)
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        time = f'现在是{now.hour}点{now.minute}分。\n'
        if now.hour <= 5 or now.hour >= 22:
            time += '夜深了，宝友们！\n'
        tips = await randomTips()
        MGS = await gousay()
        fullMessage = time + tips +"\n"+MGS
        await bot.send_group_msg(group_id=640614812,
                                 message=fullMessage)
    except CQHttpError:
        pass
