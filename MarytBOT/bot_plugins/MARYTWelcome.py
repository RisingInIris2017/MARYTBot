from nonebot import session, on_notice, NoticeSession
marytGroups = [640614812]
bocGroups = [481482264]
@on_notice('group_increase')
async def _(session: NoticeSession):
    group_id = session.event.group_id
    if group_id in marytGroups:
        welcomeMessage = '[CQ:at,qq='+str(session.event.user_id)+']'+'，欢迎来到MARYT.WORLD旗下服务器！'+'''
简单3步注册MARYT通行证，游玩我们旗下的所有服务器！
1. 首先前往 https://maryt.world 点击右上角的“注册通行证”进行注册，并记住您的邮箱与密码；
2. 在注册后访问 MARYT Skin （https://skin.maryt.world） 并使用您注册时所用邮箱与密码登录，登录后请绑定您的游戏ID到您的角色上，这将成为您在游戏内显示的ID；
3. 在群文件中找到【客户端】开头的客户端压缩包下载并解压，打开启动器，在弹出窗口中的“用户名”输入通行证邮箱，“密码”输入通行证密码，点击确定，启动游戏！
-------------------------
如果注册登录出现问题，请查看 https://maryt.world/qaa/ 或客户端文件夹下的文档获取解决方法。
想了解服务器的更多信息，
请仔细阅读群公告！
请文明交流，友善游戏！
MARYT.WORLD欢迎你的加入！'''
        await session.send(welcomeMessage)
    elif group_id in bocGroups:
        welcomeMessage = '[CQ:at,qq='+str(session.event.user_id)+']'+'，欢迎来到'+'''
《祝福或诅咒：无限力量之征》
整合包官方交流群！
在群里发送“教程”可以获取整合包相关教程，
整合包的下载、安装请仔细阅读整合包在MCBBS的发布帖。
除违法违规信息和服务器宣传外，
本群允许讨论与MC整合包相关的任何话题。
请文明交流，友善游戏！'''
        await session.send(welcomeMessage)