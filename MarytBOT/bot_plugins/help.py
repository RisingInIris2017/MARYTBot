from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command


__plugin_name__ = 'help'
__plugin_usage__ = '显示机器人所有的命令。'


@on_command('帮助', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''我是MARYT自助问答机器人，
在群里发送以下词语，我会回复对应的答案信息。
希望对你有帮助！
帮助 - 显示本条帮助信息。
玩法/怎么玩 - 服务器玩法指引。
客户端/客户端下载 - 客户端下载指引。
登录/登陆/登入 - 登录游戏指引。

如果你认为机器人还应该回答其他的常见问题，可以私聊阿苟进行添加。
如果你会使用GitHub且了解Python编程，欢迎一起参与开发fork you！
https://github.com/RisingInIris2017/MARYTBot

本机器人参考了开源项目Box-s-ville/luciabot，在此向项目开发者致谢！
''')
