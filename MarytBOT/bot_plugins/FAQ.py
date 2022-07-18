from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot import on_natural_language, NLPSession, IntentCommand
import asyncio


__plugin_name__ = 'MARYTfaq'
__plugin_usage__ = '''用法：响应出现在下表中的问题'''

@on_command('简介', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''11th的整合包为MARYT Studio原创1.16.5模组整合包《魔球奇谭》,
农夫乐事及其附属、水产养殖、烹饪锅等农业模组加持，
德鲁伊工艺、热带世界、末地拓展等强力驱动探索内容，
以及任务、世界数据包、原创游戏机制等数量巨大的MARYT原创内容，
共同讲述了一个关于朋友的故事，
开启一场童话般的冒险旅程。''')
    if session.event.group_id == 481482264:
        await session.send('''本群是整合包为MCBBS精华整合包：
[BGM][1.12.2][中英双语|拔刀剑]祝福或诅咒：无限力量之征——关于剑与理想的故事
https://www.mcbbs.net/thread-1225741-1-1.html
的官方交流群。
以热量与气候和拔刀剑为核心模组，
以暮色森林和深渊国度为探索内容，
加上丰富多彩的建筑、农业和其他模组，
讲述了一个铸剑匠人在前人的引导下，
在追逐理想的道路上一步步成长的故事。''')

@on_natural_language(keywords={'简介'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '简介')

@on_command('模组', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''11th整合包主要模组：
农夫乐事，水产养殖，碧海新生，
食物储藏室，烹饪锅，
德鲁伊工艺，热带世界，DannysExpansion，末地拓展
特色建筑装饰模组：Kaleido
MARYT原创模组：物品魔法''')
    if session.event.group_id == 481482264:
        await session.send('''本整合包的核心模组：
热量与气候，拔刀剑+最后的太刀匠人+日系附属包，
暮色森林，深渊国度；
主要模组：车万女仆，樱，豆腐工艺，未来MC''')

@on_natural_language(keywords={'模组'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '模组')

@on_command('注册', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''按以下步骤操作：
1. 进入官网 https://maryt.world
注册Maryt通行证，并在官网登录通行证，这很重要！；
2. 进入皮肤站 https://skin.maryt.world
绑定一个用户名，就是你之后在服务器中的ID；
3. 进入启动器，点击启动器左上角“没有游戏账户”，点击右下角+号，在弹出窗口中的“用户名”输入Maryt通行证邮箱，“密码”输入Maryt通行证密码，点击确定，等待登陆完成。
4. 点击启动器左上角按钮，然后点击右下角“启动游戏”即可。进入游戏后无需再登陆，直接玩就行了。''')
        await asyncio.sleep(90)

@on_natural_language(keywords={'注册', '登陆', '登入', '登录'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '注册')

@on_command('客户端', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''目前可以从QQ群文件中下载到文件名【客户端】开头的客户端压缩包。
转发给自己的QQ号，再下载，可以让下载变快。
推荐使用MARTY唯二指定压缩软件合作伙伴7-zip和Bandizip解压客户端！''')

@on_natural_language(keywords={'客户端'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '客户端')

@on_command('java', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''按以下步骤操作：
1. 进入群文件；
2. 下载【64位Java8】开头的文件；
3. 双击打开，等待窗口出现。
4. 不管显示的内容是什么，一直点窗口右下角的Next键，最后点击Finish完成安装。''')

@on_natural_language(keywords={'java'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'java')

@on_command('领地', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''打开大地图（默认为按M键），
在大地图上左键来声明区块或右键取消圈占区块，
在已经圈占的区块上按shift左键或shift右键，
即可打开或关闭强制加载区块。
详情请看：https://www.mcmod.cn/class/3201.html''')

@on_natural_language(keywords={'领地', '圈地'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '领地')

@on_command('箱子锁', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''领地内的所有容器（原版的和模组的）都会自动上锁，无需再自己上锁啦！''')

@on_natural_language(keywords={'箱子锁','锁箱子'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '箱子锁')

@on_command('命令', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''你经常用到的指令包括：
/ftbteams 编辑团队信息（在打出这个命令头之后，空一格按Tab补全子命令）
/home 设置家
/back 回死亡地点
/delhome 删除家
/trashcan 打开随身垃圾桶

/spawn命令不能用。''')

@on_natural_language(keywords={'命令', '指令'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '命令')

@on_command('崩溃', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''如果你的游戏崩溃，
请用启动器的“导出崩溃信息”功能，
并将导出文件发给阿苟，
【请勿发送】游戏窗口或启动器的截图！''')
    if session.event.group_id == 481482264:
        await session.send('''请使用启动器的导出崩溃报告功能，
将导出的压缩包等文件直接发送入群，并 @NoName德里奇。
【请勿发送】游戏窗口或启动器的截图！''')

@on_natural_language(keywords={'崩了', '崩溃'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '崩溃')

@on_command('教程', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''【11th教程施工中，敬请期待】''')
    if session.event.group_id == 481482264:
        await session.send('''1. 鼠标指向物品，按键盘U查用途，R查配方，
注意查看显示窗口的标签，尤其留意蓝色的i字标志，
点进去可以看到重要的说明。
2. 在背包中用鼠标指向物品，有些物品的信息中包含提示。
3. 整合包完整All in one教程
https://shimo.im/docs/N2A1vYgE5LfRmj3D/read
强烈推荐！
———————
4. 主要模组的教程：
樱：
锻铁炉与炼钢：https://www.mcmod.cn/item/215249.html
热量与气候：
金属熔炼机制：
https://www.mcmod.cn/post/1049.html
https://www.mcmod.cn/post/1064.html
细菌培养机制：
https://www.mcmod.cn/post/1770.html
拔刀剑：
成就、进度解锁条件一览表
https://www.mcmod.cn/post/1705.html
暮色森林：
钻石不能用来开暮色门，请在JEI中搜索“沾满魔力的铜钥匙”，
用这个代替钻石开门！
BOSS攻略：https://www.mcmod.cn/post/155.html
BOSS击杀顺序：https://www.mcmod.cn/post/649.html
豆腐工艺：
用烤豆腐块搭成地狱门形状，
用豆腐魔杖代替打火石在门框点火，
前往豆腐世界的传送门！
深渊国度：
https://www.mcmod.cn/post/809.html
https://www.mcmod.cn/post/1145.html
车万女仆祭坛的建造方法：
1. 查看【记忆中的幻想乡】手册，在【祭坛】一节有投影工具；
2. https://www.mcmod.cn/item/192891.html''')
    await asyncio.sleep(60)

@on_natural_language(keywords={'教程', '玩法','攻略'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '教程')

@on_command('会员', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''由于技术上的困难，
目前服务器暂时没有会员系统，为公益状态。
持有会员激活码的玩家可在会员系统开放后再进行兑换，
感谢各位的理解和支持！

请认准唯一指定赞助渠道：
http://afdian.net/@maryt
无偿赞助不提供任何权限，但你的名字会被展示在群公告的感谢信上。''')

@on_natural_language(keywords={'会员', '充值', '赞助'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '会员')

@on_command('任务', permission=lambda sender: sender.from_group(640614812) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 640614812:
        await session.send('''请按照如下步骤打开任务系统：
1. 打开背包
2. 点击左上角的书本标志
3. 如果你没有加入团队或者创建自己的团队，请先点击“创建组”
这样你就可以查看任务系统了。''')

@on_natural_language(keywords={'任务'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '任务')

# BOC Only
@on_command('新手包', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    if session.event.group_id == 481482264:
        await session.send('''新手物品包含32个面包、
和石头工具相同耐久的钻石剑和钻石斧各一把，
以及一本拔刀剑模组的指导书。
指导书是你游玩过程的重要指引，如果不慎丢失，
用4个泥土2x2摆放即可合成这本书！''')

@on_natural_language(keywords={'新手包'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '新手包')

@on_command('暮色', permission=lambda sender: ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 481482264:
        await session.send('''暮色森林：
钻石不能用来开暮色门，请在JEI中搜索“沾满魔力的铜钥匙”，
用这个代替钻石开门！
BOSS攻略：https://www.mcmod.cn/post/155.html
BOSS击杀顺序：https://www.mcmod.cn/post/649.html''')
        await asyncio.sleep(30)

@on_natural_language(keywords={'暮色'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '暮色')

@on_command('豆腐', permission=lambda sender: ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 481482264:
        await session.send('''豆腐工艺：
用烤豆腐块搭成地狱门形状，
用豆腐魔杖代替打火石在门框点火，
前往豆腐世界的传送门！''')
        await asyncio.sleep(30)
        
@on_natural_language(keywords={'豆腐'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '豆腐')

@on_command('联机', permission=lambda sender: sender.from_group(481482264) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 481482264:
        await session.send('''本整合包可以自由联机或开服。
联机可以借助局域网联机、
游侠联机、PCL启动器联机等工具，
或阅读联机教学板块的相关帖子：
https://www.mcbbs.net/forum.php?mod=forumdisplay&fid=178&filter=typeid&typeid=2659
局域网联机如果遇到“登录失败：无效会话”的报错，
请查阅https://www.mcmod.cn/class/1158.html''')
@on_natural_language(keywords={'联机','连机'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '联机')

@on_command('没有中文', permission=lambda sender: sender.from_group(481482264) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 481482264:
        await session.send('''假如你发现整合包没有中文选项，
按照如下步骤操作：
1. 关闭游戏；
2. 下载群文件的SmoothFont.jar文件；
3. 用它覆盖mods文件夹中的同名文件；
4. 重启游戏。''')
@on_natural_language(keywords={'没中文','没有中文','选不了中文','只有英文'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '没有中文')

@on_command('安装', permission=lambda sender: sender.from_group(481482264) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 481482264:
        await session.send('''在群内或CurseForge下载的，大小为33M左右的压缩包即为客户端整合包，主流启动器均可安装。
安装视频教学请查阅：https://www.bilibili.com/video/av44819629
如果你的启动器无法正常安装，请在这里找到你熟悉的启动器，将其更新到最新版本：
https://www.mcbbs.net/forum.php?mod=forumdisplay&fid=43&filter=digest&digest=1&typeid=908''')
    await asyncio.sleep(60)

@on_natural_language(keywords={'安装','导入','下载'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '安装')

@on_command('工业', permission=lambda sender: sender.from_group(481482264) and ((not sender.is_privatechat) or sender.is_superuser))
async def _(session: CommandSession):
    if session.event.group_id == 481482264:
        await session.send('''本整合包【不含】工业（ic2）、神秘和植物魔法，仅保留了少部分物品材料，除此之外的所有内容均已删除。''')
@on_natural_language(keywords={'工业','神秘', '植物魔法', '植魔'})
async def _(session: NLPSession):
    return IntentCommand(90.0, '工业')

