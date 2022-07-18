from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

__plugin_name__ = 'MARYTPlayTogether'
__plugin_usage__ = '''用法：目前有一键约麻和一键约战地。'''

mahjongList = [
    # 咖喱
    3283843753,
    2634673570,
    1785362875,
    # 破粥
    3218691721,
    # 落柯
    1398007362,
    # 螺丝
    2530282232,
    # Shift
    1531411762,
    # 阿苟
    814217012,
    # 友谊
    1205262477,
    # 泥扣
    183106548,
    # 科星
    825802847,
    # 百猾
    972669714,
    # 圣君
    475204878]

bfList = [
    # 螺丝
    2530282232,
    # 文文
    2640597481,
    # 带屎
    295020840,
    # 菠萝
    764013956,
    # 东风
    2054973572,
    # 忻乐
    2497712772,
    # Shift
    1531411762,
    # 一逼
    3296782408
]

@on_command('有无麻将', aliases=('有无麻将？','有无麻将！','有无麻将?','有无麻将!'), permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812 and session.event.user_id in mahjongList:
        await session.send((' '.join(['[CQ:at,qq='+str(mahQQ)+']' for mahQQ in mahjongList]))+' ， [CQ:at,qq='+str(session.event.user_id)+'] 喊你们打麻将啦！')

@on_command('有无战地', aliases=(
        '有无战地？','有无战地！','有无战地?','有无战地!','有无BF？','有无BF！','有无BF?','有无BF!','有无bf？','有无bf！','有无bf?','有无bf!'
    ), permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812 and session.event.user_id in bfList:
        await session.send((' '.join(['[CQ:at,qq='+str(bfQQ)+']' for bfQQ in bfList]))+' ， [CQ:at,qq='+str(session.event.user_id)+'] 喊你们打战地啦！')