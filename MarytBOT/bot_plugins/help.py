from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot import on_natural_language, NLPSession, IntentCommand

__plugin_name__ = 'help'
__plugin_usage__ = '显示机器人所有的命令。'


@on_command('帮助', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''我是MARYT自助问答机器人，在群里发送以下词语，我会回复对应的答案信息。希望对你有帮助！
------------
帮助 - 显示本条帮助信息。
------------
简介 / 服务器简介 - 介绍服务器的版本、模组内容。
模组 / 模组列表 - 主要模组的列表。
注册 / 登录 - 登录游戏指引。
客户端 / 客户端下载 - 客户端下载指引。
java - Java安装指引。
教室 / tips - 随机抽取一条游戏贴士
------------
领地 - 介绍领地插件的相关内容
箱子锁/锁箱子 - 介绍箱子权限的相关内容
新手包 - 介绍游戏内新手包的内容。
命令/常用命令 - 介绍服务器内的常用命令
崩溃 - 教你怎么对付客户端和服务器崩溃。
玩法 / 教程  - 服务器玩法指引和常用教程。
会员 / 充值 / 赞助 - 无偿赞助，或购买MARYT会员的相关引导。
------------
尝试发送以下词语体验整活功能：
黄历/老黄历

如果你认为机器人还应该回答其他的常见问题，可以私聊阿苟进行添加。
如果你会使用GitHub且了解Python编程，欢迎一起参与开发fork you！
https://github.com/RisingInIris2017/MARYTBot

本机器人参考了开源项目Box-s-ville/luciabot，在此向项目开发者致谢！
本机器人参考了MARYT热心玩家axty的代码，在此向axty致谢！
''')

@on_natural_language(keywords={'帮助'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '帮助')

