# LCS - Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/submissions/
# Runtime: 1752 ms, faster than 10.16% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 138.9 MB, less than 17.86% of Python3 online submissions for Longest Common Subsequence.

def lcs(i,j):

    if i == len(s1) or j == len(s2):
        cache[(i,j)] = 0
        return 0

    if (i,j) in cache.keys():
        return cache[(i,j)]
    ans = 0
    if s1[i] == s2[j]:
        ans = 1 + lcs(i+1,j+1)
    else:
        ans = max(lcs(i+1,j),lcs(i,j+1))
    cache[(i,j)] = ans
    return ans

if __name__ == "__main__":
    s1 = "abababab"
    s2 = "bcbb"
    cache = {}
    print("LCS of ",s1," and ",s2," is:",lcs(0,0))

    s1 = "abababab"
    s2 = "bcbab"
    cache = {}
    print("LCS of ",s1," and ",s2," is:",lcs(0,0))


# LCS of  abababab  and  bcbb  is: 3
# LCS of  abababab  and  bcbab  is: 4