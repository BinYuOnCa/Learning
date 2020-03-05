class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here

        #DP 
        
        # define f[i][j] as max sentences count for string s[i:j+1] based on given dict 
        # then f[i][j] = sumx( f[i][k]*f[k+1][j] | k=i,...j) 
        
        l = len(s)
        f = [[0]*l for _ in range(l)]
        
        s = s.lower()
        dict = set([w.lower() for w in dict])
       
        for i in range(l):
            for j in range(i, l):
                if s[i:j+1] in dict:
                    f[i][j] = 1 
    
        for i in range(l):
            for j in range(l):
                for k in range(i,j):
                    f[i][j] += f[i][k]*f[k+1][j]
        
        return f[0][-1]        
        
'''
Time Limit Exceeded

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

Expected  265816832


"qoekmvHseoPurbx"
["qoe","Qoe","kmv","kmvHseoPurbx","HseoPurbx","Purbx","Hseo","qoekmv"]


"aaaaaaaa"
["aaaa","aa","a"]

exp: 55 
''' 
