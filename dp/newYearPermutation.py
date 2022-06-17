# https://codeforces.com/problemset/problem/1091/D
# D. New Year and the Permutation Concatenation
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Let n be an integer. Consider all permutations on integers 1 to n in lexicographic order, and concatenate them into 
# one big sequence p. For example, if n=3, then p=[1,2,3,1,3,2,2,1,3,2,3,1,3,1,2,3,2,1]. 
# The length of this sequence will be n⋅n!.

# Let 1≤i≤j≤n⋅n! be a pair of indices. We call the sequence (pi,pi+1,…,pj−1,pj) a subarray of p. 
# Its length is defined as the number of its elements, i.e., j−i+1. Its sum is the sum of all its elements, i.e., ∑jk=ipk.

# You are given n. Find the number of subarrays of p of length n having sum n(n+1)2. 
# Since this number may be large, output it modulo 998244353 (a prime number).

# Input
# The only line contains one integer n (1≤n≤106), as described in the problem statement.

# Output
# Output a single integer — the number of subarrays of length n having sum n(n+1)2, modulo 998244353.

# Examples
# input - 3
# output - 9
# input - 4
# output - 56
# input - 10
# output - 30052700
# Note
# In the first sample, there are 16 subarrays of length 3. In order of appearance, they are:
# [1,2,3], [2,3,1], [3,1,3], [1,3,2], [3,2,2], [2,2,1], [2,1,3], [1,3,2], [3,2,3], [2,3,1], [3,1,3]
# , [1,3,1], [3,1,2], [1,2,3], [2,3,2], [3,2,1].

# Their sums are 6, 6, 7, 6, 7, 5, 6, 6, 8, 6, 7, 5, 6, 6, 7, 6. As n(n+1)2=6, the answer is 9.
# Reference - https://books.google.co.in/books?id=x_D2DwAAQBAJ&pg=PA264&lpg=PA264&dq=New+Year+and+the+Permutation+Concatenation&source=bl&ots=0oOynO71V-&sig=ACfU3U0bhFWyeSyTQGVNK1AO4MqNX4nGKg&hl=en&sa=X&ved=2ahUKEwjZp5nj47H4AhUQR2wGHYofBJgQ6AF6BAhYEAM#v=onepage&q=New%20Year%20and%20the%20Permutation%20Concatenation&f=false

def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

def countPermuation(n):
    global memo
    if n <= 0:
        return 0
    if n == 1:
        return n
    if memo[n] != None:
        return memo[n]
    memo[n] = fact(n) + (countPermuation(n-1) - 1)*n
    return memo[n]

if __name__ == "__main__":

    for i in range(11):
        memo = [None for j in range(i+1)]
        print("For n=",i," count is:",countPermuation(i))