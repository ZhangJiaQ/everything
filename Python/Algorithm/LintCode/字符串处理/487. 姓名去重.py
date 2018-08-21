class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
		'''
        487. 姓名去重
        给一串名字，将他们去重之后返回。两个名字重复是说在忽略大小写的情况下是一样的。
        
        样例
        给出：
        
        [
          "James",
          "james",
          "Bill Gates",
          "bill Gates",
          "Hello World",
          "HELLO WORLD",
          "Helloworld"
        ]
        返回：
        
        [
          "james",
          "bill gates",
          "hello world",
          "helloworld"
        ]
        返回名字必须都是小写字母。
        '''
        name = []
        for d in names:
            if d.lower() not in name:
                name.append(d.lower())

        return name