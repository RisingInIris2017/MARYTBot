import nonebot
from datetime import datetime
from random import randint
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.message import MessageSegment

__plugin_name__ = 'MARYTTimeReport'
__plugin_usage__ = '''
用法：
整点报时。
'''

# 变量和函数
tipsList = [
# '怪物在被打的时候有几率召唤援助，如果你的装备优良，这是刷杀敌数的好机会！',
# '当心突然出现在脚下的末影螨。',
# '喝下鸟之祝福药水之前务必把血量回满！',
# '当你想不起来模组怎么玩的时候，往群里发“教程”两个字试试！',
# '''在打开工作台的情况下用JEI查询配方，
# 点击配方右下角的+号按钮，
# JEI会将背包中的材料在工作台自动摆好！''',
# '斩杀之证和耀魂之瓶的配方并不真的消耗拔刀剑，只是从拔刀剑上提取指定数量的杀敌数和耀魂数而已！',
'如果你看到这条游戏贴士，说明你今天应该给M服提供一条属于你的游戏贴士。',
# '''如果你不想跑图寻找林地府邸，
# 可以在车万女仆祭坛上召唤唤魔者，
# 召唤配方可以通过在JEI中
# 查询魔力粉尘的用途看到。''',
# '''养殖村民的玩家务必用方块把村民围好，
# 因为原版MC的僵尸围城机制无视领地、蘑菇岛生物群系、亮度发生！
# 详情戳d.g-c-z.cc/MBJSWC'''
]

async def randomTips():
    tip = tipsList[randint(0,len(tipsList)-1)]
    return "【阿苟的完美教室】\n"+tip
# 定时部分
# 整点报时
@nonebot.scheduler.scheduled_job('cron', hour='8-21')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        time = f'现在是{now.hour}点整。\n'
        tips = await randomTips()
        fullMessage = time + tips
        randomPicIndex = randint(0, 31)
        await bot.send_group_msg(group_id=640614812,
                                message=MessageSegment.text(fullMessage + "\n") + MessageSegment.text("【今日苟语录】\n") + MessageSegment.image('file:///' + f"C:/Users/东风佬/Desktop/newMarytRobot/MarytBOT/语录/" + str(randomPicIndex) + ".jpg"))
    except CQHttpError:
        pass

# 早报时
@nonebot.scheduler.scheduled_job('cron', hour='7')
async def _():
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=640614812,
                                 message=MessageSegment.text("七点钟啦！让我看看是谁还没有起床搓MARYT服务器！") + MessageSegment.image('file:///' + f"C:/Users/东风佬/Desktop/newMarytRobot/MarytBOT/报时/wake.png"))
    except CQHttpError:
        pass

# 晚报时
@nonebot.scheduler.scheduled_job('cron', hour='22')
async def _():
    bot = nonebot.get_bot()
    try:
        await bot.send_group_msg(group_id=640614812,
                                 message=MessageSegment.text("晚上十点了还在打游戏，不睡觉的吗你们") + MessageSegment.image('file:///' + f"C:/Users/东风佬/Desktop/newMarytRobot/MarytBOT/报时/sleep.png"))
    except CQHttpError:
        pass
