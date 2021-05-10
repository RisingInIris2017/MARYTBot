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
4. 实在没有再到群里提问。''')

@on_command('客户端',aliases=('客户端下载'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''目前可以从QQ群文件中下载到文件名【客户端】开头的客户端压缩包。
转发给自己的QQ号，再下载，可以让下载变快。
推荐使用MARTY唯二指定压缩软件合作伙伴7-zip和Bandizip解压客户端！''')

@on_command('注册',aliases=('登陆','登入','登录'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''按以下步骤操作：
1. 进入官网maryt.world注册Maryt通行证，并在官网登录通行证，这很重要！；
2. 进入皮肤站skin.maryt.world，绑定一个用户名，就是你之后在服务器中的ID；
3. 进入启动器，点击启动器左上角“没有游戏账户”，点击右下角+号，在弹出窗口中的“用户名”输入Maryt通行证邮箱，“密码”输入Maryt通行证密码，点击确定，等待登陆完成。
4. 点击启动器左上角按钮，然后点击右下角“启动游戏”即可。进入游戏后无需再登陆，直接玩就行了。''')
