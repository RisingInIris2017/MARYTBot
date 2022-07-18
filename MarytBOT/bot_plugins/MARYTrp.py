import nonebot
from nonebot.message import MessageSegment
from aiocqhttp import ApiError, Event
from datetime import datetime
import random
import pytz
from nonebot.message import MessageSegment
import datetime

__plugin_name__ = 'MARYTrp'
__plugin_usage__ = '''用法：今日人品'''

commandList = ['jrrp', '今日人品']

bot = nonebot.get_bot()

async def containsAny(seq, aset):
    return True if any(i in seq for i in aset) else False

async def seedDatePart():
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'));
    return str(now.year)+str(now.month)+str(now.day)

@bot.on_message
async def handle_msg(event: Event):
    full_seed = await seedDatePart() + str(event['user_id'])
    random.seed(full_seed)
    rp = str(random.randint(0,100))
    rp_reply = (
        MessageSegment.at(event['user_id']) +
        MessageSegment.text("你的今日人品是：" + rp + '，\n') +
        MessageSegment.text("话不多说，祝你下巡自摸。\n\n") +
        MessageSegment.text("【今日苟语录】\n")
        + MessageSegment.image('file:///' + f"C:/Users/东风佬/Desktop/newMarytRobot/MarytBOT/语录/" + str(random.randint(0, 31)) + ".jpg")
    )
    try:
        if event['message_type'] == 'group' and event['group_id'] == 640614812:
            if await containsAny(event['raw_message'], commandList):
                await bot.send_group_msg(group_id=640614812,
                                    message=rp_reply)
    except ApiError:
        pass
