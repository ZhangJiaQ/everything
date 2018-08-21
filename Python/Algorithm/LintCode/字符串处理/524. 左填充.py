class StringUtils:
    """
    @param: originalStr: the string we want to append to
    @param: size: the target length of the string
    @param: padChar: the character to pad to the left side of the string
    @return: A string
    """
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        '''
        524. �����
        ʵ��һ��leftpad�⣬�����֪��ʲô��leftpad���Կ�����
        
        ����
        leftpad("foo", 5)
        >> "  foo"
        
        leftpad("foobar", 6)
        >> "foobar"
        
        leftpad("1", 2, "0")
        >> "01"
        '''
        # write your code here
        len_str = len(originalStr)
        if (size - len_str) > 0:
            add_str = padChar * (size - len_str)
            return add_str + originalStr
        else:
            return originalStr