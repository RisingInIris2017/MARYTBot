import nonebot
from aiocqhttp import ApiError, Event
__plugin_name__ = 'MARYTBlacklist'
__plugin_usage__ = '''用法：有人问服务器的状态时，发出命令调用状态bot'''
bot = nonebot.get_bot()
commandList = ['服务器没了','服务器崩了','服务器炸了','服务器咋没了','服务器咋崩了','服务器咋炸了','服没了','服崩了','服炸了','服务器怎么没了','服务器怎么崩了','服务器怎么炸了']

async def containsAny(seq, aset):
    return True if any(i in seq for i in aset) else False
@bot.on_message
async def handle_msg(event: Event):
    try:
        if event['message_type'] == 'group' and event['group_id'] == 640614812:
            if await containsAny(event['raw_message'], commandList):
                return {'reply': r'/状态'}
    except ApiError:
        pass
