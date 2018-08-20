class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
		'''
		128. 哈希函数
		在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数，比如：

		hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE 

									  = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

									  = 3595978 % HASH_SIZE

		其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。

		给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。

		样例
		对于key="abcd" 并且 size=100， 返回 78
		'''
        hash_num = 0
        len_key = len(key)
        temp = 1
        temp_str = key[::-1]
        
        for k in temp_str:
            hash_num = ord(k) * temp % HASH_SIZE + hash_num
            temp = 33 * temp % HASH_SIZE 
        return hash_num % HASH_SIZE
		