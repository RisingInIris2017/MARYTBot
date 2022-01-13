from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot import on_natural_language, NLPSession, IntentCommand


__plugin_name__ = 'MARYTfaq'
__plugin_usage__ = '''用法：响应出现在下表中的问题'''

@on_command('简介', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''我们的服务器版本为1.12.2，
整合包为MCBBS精华整合包：
[BGM][1.12.2][中英双语|拔刀剑]祝福或诅咒：无限力量之征——关于剑与理想的故事
https://www.mcbbs.net/thread-1225741-1-1.html
以热量与气候和拔刀剑为核心模组，
以暮色森林和深渊国度为探索内容，
加上丰富多彩的建筑、农业和其他模组，
讲述了一个铸剑匠人在前人的引导下，
在追逐理想的道路上一步步成长的故事。''')

@on_natural_language(keywords={'简介'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '简介')

@on_command('模组', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''核心模组：
热量与气候，拔刀剑+最后的太刀匠人+日系附属包，
暮色森林，深渊国度；
主要模组：车万女仆，樱，豆腐工艺，未来MC
建筑模组：Absent by Design
https://www.mcmod.cn/class/1375.html
土方工程
https://www.mcmod.cn/class/1508.html
Macaw的家具
https://www.mcmod.cn/class/2573.html''')

@on_natural_language(keywords={'模组'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '模组')

@on_command('注册', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''按以下步骤操作：
1. 进入官网 https://maryt.world
注册Maryt通行证，并在官网登录通行证，这很重要！；
2. 进入皮肤站 https://skin.maryt.world
绑定一个用户名，就是你之后在服务器中的ID；
3. 进入启动器，点击启动器左上角“没有游戏账户”，点击右下角+号，在弹出窗口中的“用户名”输入Maryt通行证邮箱，“密码”输入Maryt通行证密码，点击确定，等待登陆完成。
4. 点击启动器左上角按钮，然后点击右下角“启动游戏”即可。进入游戏后无需再登陆，直接玩就行了。''')

@on_natural_language(keywords={'注册', '登陆', '登入', '登录'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '注册')

@on_command('客户端', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''目前可以从QQ群文件中下载到文件名【客户端】开头的客户端压缩包。
转发给自己的QQ号，再下载，可以让下载变快。
推荐使用MARTY唯二指定压缩软件合作伙伴7-zip和Bandizip解压客户端！''')

@on_natural_language(keywords={'客户端'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '客户端')

@on_command('java', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''按以下步骤操作：
1. 进入群文件；
2. 下载【64位Java8】开头的文件；
3. 双击打开，等待窗口出现。
4. 不管显示的内容是什么，一直点窗口右下角的Next键，最后点击Finish完成安装。''')

@on_natural_language(keywords={'java'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'java')

@on_command('领地', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''使用木锄圈地，
左键一个点，右键一个点，
以两点为体对角线的长方体为你所圈领地的范围，
输入
/res create 领地名
即可买下这块领地。
非会员圈地每格0.3游戏币，会员每格0.1游戏币。
输入/res set可以打开领地权限菜单。
目前暂不开放领地飞行！''')

@on_natural_language(keywords={'领地', '圈地'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '领地')

@on_command('箱子锁', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''箱子锁使用指令
-----------
/cpublic - 创建一个公共箱子，任何人都能打开它。
/cprivate - 创建一个私人箱子，只有你（还有你添加的人）才能打开它。
/cpassword - 创建一个密码箱，只有知道密码的人才能打开它。
/cmodify - 修改受LWC保护容器的配置，你可以用它添加你信任的玩家或者权限组。
/cunlock - 解锁受密码保护的容器。
/cremove - 解锁受LWC保护的容器。
/cinfo - 查看一个受LWC保护的容器的信息。
/climits - 查看你已经锁过的容器数量。
/lwc flag <flag名字> <on/off>
所有可供使用的flag:
redstone - 如果打开, 红石将能够影响这个受保护的容器。
magnet - 打开后，容器会自动吸取附近的掉落物。
autoclose - 如果受保护的方块是门, 在打开后会帮你自动关上。
AllowExplosions - 打开后, 爆炸会摧毁受保护的箱子。
hopper - 打开后, 漏斗可以放入/取出箱子内的物品。''')

@on_natural_language(keywords={'箱子锁','锁箱子'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '箱子锁')

@on_command('新手包', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''新手物品包含32个面包、
和石头工具相同耐久的钻石剑和钻石斧各一把，
以及一本拔刀剑模组的指导书。
指导书是你游玩过程的重要指引，如果不慎丢失，
用4个泥土2x2摆放即可合成这本书！''')

@on_natural_language(keywords={'新手包'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '新手包')

@on_command('命令', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''你经常用到的指令包括：
/qd 每日签到
/cz 城镇系统
/sg 收购商店
/sd 出售商店
/lj 随身垃圾桶
/dt 领取 MCBBS 顶贴奖励''')

@on_natural_language(keywords={'命令', '指令'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '命令')

@on_command('崩溃', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''如果你的游戏崩溃，请按如下提示操作：
1. 点击游戏窗口中的“复制链接”按钮；
2. 点击“复制到剪贴板”；
3. 在QQ里粘贴，发给阿苟。''')

@on_natural_language(keywords={'崩了', '崩溃'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '崩溃')

@on_command('教程', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''1. 鼠标指向物品，按键盘U查用途，R查配方，
注意查看显示窗口的标签，尤其留意蓝色的i字标志，
点进去是阿苟留下的重要说明。
2. 在背包中用鼠标指向物品，有些物品的信息中包含提示。
3. 整合包完整All in one教程
https://shimo.im/docs/N2A1vYgE5LfRmj3D/read
强烈推荐！
———————
4. 主要模组的教程：
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
BOSS攻略：https://www.mcmod.cn/post/155.html
BOSS击杀顺序：https://www.mcmod.cn/post/649.html
深渊国度：
https://www.mcmod.cn/post/809.html
https://www.mcmod.cn/post/1145.html
车万女仆祭坛的建造方法：
1. 查看【记忆中的幻想乡】手册，在【祭坛】一节有投影工具；
2. https://www.mcmod.cn/item/192891.html''')

@on_natural_language(keywords={'教程', '玩法','攻略'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '教程')

@on_command('会员', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''请认准唯一指定赞助和会员购买渠道：
http://afdian.net/@maryt
【关于无偿赞助】
无偿赞助不提供任何权限，但你的名字会被展示在群公告的感谢信上。
【关于购买会员】
支付5.99元购买会员后，
将得到的兑换码命令输入游戏，
即可领取会员权限！
会员特权如下：
1. 领地最大空间
100x100x100升级到200x200x200；
2. 领地圈地价格
0.3游戏币/方格->0.1游戏币/方格；
3. 会员专属签到奖励；
4. 享受自定义头衔，如已有其他头衔，
享受个性化颜色定制权限。''')
@on_natural_language(keywords={'会员', '充值', '赞助'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '会员')

@on_command('任务', permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    await session.send('''MARYT 10th v2.3.0版本加入了教程任务，
没有使用过任务系统的玩家，
请按照如下步骤打开任务系统：
1. 打开背包
2. 点击左上角的书本标志
3. 直接点击创建组
4. 这样你就可以查看任务系统了。

任务没有奖励，仅仅作为游玩引导。''')
@on_natural_language(keywords={'任务'}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(90.0, '任务')
