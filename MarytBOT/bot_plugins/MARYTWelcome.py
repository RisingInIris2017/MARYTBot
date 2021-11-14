from nonebot import session, on_notice, NoticeSession
allowGroups = [640614812]
@on_notice('group_increase')
async def _(session: NoticeSession):
    group_id = session.event.group_id
    if group_id in allowGroups:
        welcomeMessage = '[CQ:at,qq='+str(session.event.user_id)+']'+'，欢迎来到MARYT服务器！'+'''
我们服务器MC版本：1.12.2
想了解服务器的更多信息，请仔细阅读群公告，
向群里发送“帮助”两个字可以获取机器人的帮助内容。
--------注册教程----------
按以下步骤操作：
1. 首先前往 https://maryt.world 点击右上角的“注册通行证”进行注册，并记住您的邮箱与密码；
2. 在注册后访问 MARYT Skin （https://skin.maryt.world） 并使用您注册时所用邮箱与密码登录，登录后请绑定您的游戏ID到您的角色上，这将成为您在游戏内显示的IDD；
3. 下载 MARYT 10th 客户端（群文件）并解压，随后双击“MARYT_10th_启动器.exe”。此时可能会进行更新，更新后会显示启动器，在弹出窗口中的“用户名”输入通行证邮箱，“密码”输入通行证密码，点击确定即可；
4. 如果注册登录出现问题，请前往 https://maryt.world/qaa/ 或客户端文件夹下的文档获取解决方法。
-------------------------
请文明交流，友善游戏！
MARYT服务器欢迎你的加入！'''
        await session.send(welcomeMessage)