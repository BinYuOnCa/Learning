# 683. Word Break III

https://www.lintcode.com/problem/word-break-iii/

## Description

Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

## Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output: 0
Notice
Ignore case

# Questions before coding

Input: 
  We shold ignore case, but do we have upper case in parameters? 
  Do we have duplication in dict (ignore case)?
  Max length of string and dict?

Output:
  What should we return for both NULL parameters? 



# Solution

# DFS 

  Will get correct answer, except Time Limit Exceed for following test case:


"aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

Expected  265816832


# DP 
        
        # define f[i][j] as max sentences count for string s[i:j+1] based on given dict 
        # then f[i][j] = sumx( f[i][k]*f[k+1][j] | k=i,...j) 

	# Initialization: for each words in string, set f[i][j]=1, for s[i:j+1] == word

	# result is f[0][-1]
 
