import nonebot
from nonebot.permission import SenderRoles
from aiocqhttp import ApiError, Event
__plugin_name__ = 'MARYTBlacklist'
__plugin_usage__ = '''用法：当特定的QQ号发送特定消息时，消息会被撤回'''
bot = nonebot.get_bot()
# Please put your own list here
badWordList = []

async def containsAny(seq, aset):
    return seq if (seq != "") and any(i in seq for i in aset) else False
@bot.on_message
async def handle_msg(event: Event):
    try:
        if event['message_type'] == 'group' and event['group_id'] == 640614812: # 是正确的 QQ 群
            sender = await SenderRoles.create(bot, event)
            if not (sender.is_owner or sender.is_admin):
                messageToCheck = await containsAny(event['raw_message'], badWordList)
                if messageToCheck:
                    await bot.send_private_msg(user_id=814217012,
                    message=(
                        'QQ群' + str(event['group_id']) + '的群员' + str(event['user_id']) + '发送了可疑的消息：“' + messageToCheck + '”已被撤回。'
                    ),
                    auto_escape=True)
                    return {
                        'reply': '你发送的消息中包含可疑的词汇，\n现已撤回，消息原文已抄送群管理员。\n请文明交流，友善游戏！',
                        'delete': True
                    }
                elif 'ax' in event['raw_message']:
                    if event['user_id'] == 414304803:
                        return {'delete': True}
    except ApiError:
        pass
