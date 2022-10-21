import time

import progressbar


class Pwd_DCpr:
    """
    用于破解zip压缩文件简单密码
    """

    def __init__(self, path, pwd_len, password=None, ):
        self.path = path
        self.pwd_len = pwd_len
        self.password = password

    def create_pwd(self):
        import itertools as it
        import string
        words = "@" + string.ascii_lowercase  # + string.digits
        for i in range(1, self.pwd_len + 1):
            passwd_pool = it.product(words, repeat=i)
            for pp in passwd_pool:
                yield "".join(pp)

    def pwd_fun(self, pword):
        import zipfile, os
        file_type = os.path.splitext(self.path)[-1][1:]
        if file_type == "zip":
            with zipfile.ZipFile(self.path, "r") as zipf:
		try:
                    zipf.extractall("new_data", pwd=pword.encode())
                    time.sleep(1)
                    print(f"解压成功，密码是：{pword}")
                    return True
                except Exception as e:
                    print(pword, ">>>\t", e)

    def exec(self):
        for _ in self.create_pwd():
            flag = self.pwd_fun(_)
            if flag:
                break
