import time
import random

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

__plugin_name__ = 'MARYTDice'
__plugin_usage__ = '''用法：骰子。'''

@on_command('。r', aliases=('骰子','骰', r'.r'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    random.seed(int(str(int(time.time()))+str(session.event.user_id)))
    await session.send(
        '王牌！[CQ:at,qq=' +
        str(session.event.user_id) +
        ']' +
        '在决斗中亮出了' +
        str(random.randint(1, 100))
        + '点！')
