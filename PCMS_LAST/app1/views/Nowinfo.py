# 用来标记当前信息
class globalVariables:
    def __init__(self, user=None, corpus_name=None, corpus=None):
        self.USER = user
        self.CORPUS_NAME = corpus_name
        self.CORPUS = corpus


now = globalVariables()

# 服务器端数据存储地址
fileL = "D:\py code\PCMS\\app1\\corpusFiles\\"
# 服务器端和用户端存储临时文件的地址
fileS = "D:\py code\PCMS\\app1\\scratchFiles\\"
