from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = 'MARYTtestingserver'
__plugin_usage__ = '''用法：发送测试服有关信息'''

@on_command('测试服', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''测试服常见问题一览：
1. 测试服是Minecraft 1.16.5模组服，
没有任何魔改，仅供测试模组、插件和服务端的稳定性用。
大家当作体验新模组来玩就好。
可能会经常增加、删除模组和插件，可能会经常重启，
各位玩家需要做好一定的心理准备。
2. 测试服使用MARYT通行证外置登录，
IP地址客户端自带。
3. 测试服是删档内测，
预计在2022年寒假之前关服。
4. 在测试结束后，我们会向所有玩家发布调查问卷，请大家按照自己的游玩体验来填写，感谢配合和支持！
5. 测试服里有一些模组是大家从来没有见到过的，可能没有汉化和教程，阿苟会尽快提供一份自己摸索的模组教程，
我们会在MARYT的QQ频道设立“测试服教程频道”供大家发布和交流。
贡献优质教程的玩家将获得服务器内BetaTester永久头衔。
6. 最后也是最重要的，客户端和更新包下载地址【天翼云】：
https://cloud.189.cn/web/share?code=b2uEN3vMnuqe
访问码：ejp3''')

@on_natural_language(keywords={'测试服'})
async def _(session: NLPSession):
    return IntentCommand(90.0,'测试服')
