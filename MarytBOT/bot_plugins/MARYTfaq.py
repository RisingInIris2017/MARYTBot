from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command


__plugin_name__ = 'MARYTfaq'
__plugin_usage__ = '''
用法：
响应出现在下表中的问题
'''

@on_command('玩法',aliases=('怎么玩'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''当你发现玩不来服务器的时候，你可以：
1. 鼠标指向物品，按键盘U查用途，R查配方。
2. 查阅mcmod百科可以得到大部分问题的答案。
3. 对于Create101整合包，你还可以阅读游戏加载、暂停界面的“雪尼的完美教室”提示。
4. 实在没有再到群里提问。
''')

@on_command('客户端',aliases=('客户端下载'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''目前可以从QQ群文件中下载到文件名【客户端】开头的客户端压缩包。
转发给自己的QQ号，再下载，可以让下载变快。
推荐使用MARTY唯二指定压缩软件合作伙伴7-zip和Bandizip解压客户端！
''')

@on_command('登录',aliases=('登陆','登入'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''目前服务器使用的是离线登录，只要在启动器填入你的游戏ID就可以啦！
''')
