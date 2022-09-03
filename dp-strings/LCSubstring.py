# Longest Common Substring
# https://www.spoj.com/problems/LCS/

# Input:
# alsdfkjfjkdsal
# fdjskalajfkdsla

# Output:
# 3

def lcsubstring(i,j,ans):
    if i == len(s1) or j == len(s2):
        return ans

    key = (i,j,ans)
    if key in cache:
        return cache[key]
    if s1[i] == s2[j]:
        ans = lcsubstring(i+1,j+1,ans+1)
    else:
        ans = max(ans,lcsubstring(i+1,j,0),lcsubstring(i,j+1,0))

    cache[key] = ans
    return ans

if __name__ == "__main__":
    s1 = "alsdfkjfjkdsal"
    s2 = "fdjskalajfkdsla"
    cache = {}
    print("Longest Common Substring of",s1, "and",s2,"is",lcsubstring(0,0,0))


    s1 = "aabaa"
    s2 = "xaabaa"
    cache = {}
    print("Longest Common Substring of",s1, "and",s2,"is",lcsubstring(0,0,0))