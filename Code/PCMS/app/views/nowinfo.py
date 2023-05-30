# 用来标记当前信息
global USER
global CORPUS_NAME
global CORPUS
USER = None
CORPUS_NAME = None
CORPUS = None


class globalVariables:
    def __init__(self, user=None, corpus_name=None, corpus=None):
        self.USER = user
        self.CORPUS_NAME = corpus_name
        self.CORPUS = corpus


now = globalVariables()
