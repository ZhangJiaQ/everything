  #535. Encode and Decode TinyURL

#TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

#Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


import random
class Codec:
    
    def __init__(self):
        self.short_url_array = []
        self.url_dict = {}
    
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        short_str = self.range_str()
        self.short_url_array.append(short_str)
        self.url_dict[short_str] = longUrl
        return 'http://tinyurl.com/'+short_str
        
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        str_short = shortUrl[-6:]
        return self.url_dict[str_short]
        
    
    def range_str(self):
        str_num_str = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        str_six = ''
        for i in range(6):
            str_six += str_num_str[random.randint(0,len(str_num_str)-1)]
        return str_six
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))