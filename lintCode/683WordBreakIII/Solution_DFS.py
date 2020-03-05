class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here

        if not s :
            return 0 
                
        if not dict :
            return 0 
        
        self.sentencesCt = 0 
        
        visited={}
        #  use set to remove duplication, UT2 
        self.dfs(s.lower(), set([x.lower() for x in dict]))
        
        return self.sentencesCt
    def dfs(self, s, dict):
        if not s:
            self.sentencesCt += 1 
            return True
        # removed due to UT1, sub string in dict  
        # if s in dict:
        #     self.sentencesCt += 1 
        #     return True 
            
        for word in dict:
            idx = s.find(word)
            if idx != 0 :
                continue
            subs = s[len(word):]    

            self.dfs(subs, dict)

        return False 

if __name__=='__main__':
    s = Solution()

    uts = ( ( "aaaaaaaa",["aaaa","aa","a"], 55 ),
            ("qoekmvHseoPurbx",
             ["qoe","Qoe","kmv","kmvHseoPurbx","HseoPurbx","Purbx",
               "Hseo","qoekmv"],
             5 ),
            ("aaaaaaaaaaaaaaaaaaaaa",
             ["a","aa","aaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
             504156),
#		("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
#             ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa",
#              "aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
#             265816832),
          )

    for ut in uts:
        ret = s.wordBreak3(ut[0],ut[1])
        if ret != ut[2] or True :
            print('str:{}\ndict:{}\nExp:{}, Got:{}'.format(ut[0],
                           ut[1], ut[2], ret))

'''
UT3
Time Limit Exceeded

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

Expected  265816832

----UT2 --
"qoekmvHseoPurbx"
["qoe","Qoe","kmv","kmvHseoPurbx","HseoPurbx","Purbx","Hseo","qoekmv"]

----UT1-----
"aaaaaaaa"
["aaaa","aa","a"]

exp: 55 
''' 
