import nonebot
from datetime import datetime
from random import randint
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.message import MessageSegment

__plugin_name__ = 'MARYTTimeReport'
__plugin_usage__ = '''
无命令，只汇报服务器状态。
'''
    
#半点报时
@nonebot.scheduler.scheduled_job('cron', hour='*',minute='0,30')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    await bot.send_private_msg(user_id=814217012,
        message=(
            now.strftime(r"%Y-%m-%d %H:%M")+ ", " + "服务器正常"
        ),
        auto_escape=True)
    