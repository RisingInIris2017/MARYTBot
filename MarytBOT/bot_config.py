from nonebot.default_config import *

from datetime import timedelta


# 表示“超级用户”，也就是机器人的主人。
# 超级用户拥有最高的权限。在这里填入你的 QQ 号。
SUPERUSERS = { 814217012 }
# 表示命令的前缀，例如假如命令叫 `天气`，那么只有用户在输入 `/天气` 时候才会触发命令。
COMMAND_START = { "" }
# 机器人会识别以下列字符串开头的消息并回复
NICKNAME = { "" }
# 关闭调试输出，提升性能。
DEBUG = False
# 表示一条命令的超时（没有用户输入）时间。
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)
# 服务器和端口
HOST = '127.0.0.1'
PORT = 5702

SESSION_RUNNING_EXPRESSION = ''
"""
{anno}`nonebot.typing.Expression_T`
当有命令会话正在运行时，给用户新消息的回复。
**默认值:** `'您有命令正在执行，请稍后再试'`
用法:
    ```python
    SESSION_RUNNING_EXPRESSION = ''
    ```
    设置为空，表示当有命令会话正在运行时，不回复用户的新消息。
"""
