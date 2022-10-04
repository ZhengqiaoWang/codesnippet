
from ui_mgr import UIMgr

um = UIMgr("helloworld")

# 添加输入文本框
# 添加一个文本框，要求输入前缀
um.registInput("prefix", "前缀", "默认就是这个前缀")
# 添加一个文本框，要求输入后缀
um.registInput("suffix", "后缀", "默认就是这个后缀")

# 添加文件选择文本框
um.registPathSelect("filepath", "选个文件")

# 注册按钮点击事件


def onButtnClick(prefix, suffix, filepath):
    print("前缀：", prefix)
    print("后缀：", suffix)
    print("文件路径：", filepath)
    um.message("好啦！", "结果是：\n{}-{}-{}".format(prefix, filepath, suffix))


um.registOnButtonClickCB(onButtnClick)

um.show()
