import nonebot
from datetime import datetime
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.message import MessageSegment
import datetime

from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import asyncio

__plugin_name__ = 'MARYTGKCountdown'
__plugin_usage__ = '''用法：发送高考倒计时。'''

async def GKCountdown():
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'));
    year = now.year
    month = now.month
    day = now.day
    countdown = (datetime.datetime(year, 6, 7) - datetime.datetime(year, month, day)).days
    if countdown < 1:
        return False
    return "距离" + str(year) + "高考还有" + str(countdown) + "天"

async def AXCountdown():
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'));
    if now.month >= 6 and now.day >= 21:
        return False
    else:
        year = now.year
        month = now.month
        day = now.day
        countdown = (datetime.datetime(year, 6, 21) - datetime.datetime(year, month, day)).days
        if countdown < 1:
            return False
        return "距离" + str(year) + "高考还有" + str(countdown) + "天"

# 定时部分
@nonebot.scheduler.scheduled_job('cron', hour='6,23')
async def _():
    bot = nonebot.get_bot()
    try:
        countdowntextA = await GKCountdown()
        if countdowntextA:
            await bot.send_group_msg(group_id=640614812,
                                    message=MessageSegment.text(countdowntextA))
        countdowntextB = await AXCountdown()
        if countdowntextB:
            await bot.send_group_msg(group_id=640614812,
                                    message=MessageSegment.text(countdowntextB))
    except CQHttpError:
        pass

@on_natural_language(keywords={'高考', '中考'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '高考')

@on_command('高考', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    countdowntextA = await GKCountdown()
    if countdowntextA:
        await session.send(countdowntextA)
    countdowntextB = await AXCountdown()
    if countdowntextB:
        await session.send(countdowntextB)
    await asyncio.sleep(60)
