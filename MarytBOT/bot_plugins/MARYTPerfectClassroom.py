from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import time
from random import randint
from nonebot import on_natural_language, NLPSession, IntentCommand

__plugin_name__ = 'MARYTPerfectClassroom'
__plugin_usage__ = '''
用法：
随机抽取一条游戏贴士，可以主动响应玩家调用，无玩家调用时以半点报时形式出现。
'''

# 变量和函数
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

# 主动响应部分
@on_command('教室',permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    tips = await randomTips()
    await session.send(tips)

@on_natural_language(keywords={'教室', '贴士'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '教室')
