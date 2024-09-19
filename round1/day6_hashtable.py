# LC242 Valid Anagram: https://leetcode.com/problems/valid-anagram/description/
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''
# method 1: create two dictionaries to store the count of each character in s and t, and then compare the two dictionaries
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
# method 2: use the Counter class from the collections module
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)
        if counterS == counterT:
            return True
        return False
# method 3: sort the two strings and compare them   
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        return False 

# LC49 Group Anagrams: https://leetcode.com/problems/group-anagrams/
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
# method 1: use the Counter class from the collections module
class Solution:
    # categorized by Count
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity: O(N*K + N*A) -- A is the size of the charSet i.e. 26
        # N is the length of strs, K is the maximum length of a string in strs
        # space complexity: O(N*K + N*A)
        ans: DefaultDict[int, List[str]] = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
# method 2: use the sorted string as the key
from collections import defaultdict
class Solution:
    # categorized by sorted String:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity: O(N*KlogK)
        # space complexity: O(N*K)
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

# LC438 Find All Anagrams in a String: https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
# method 1: use the Counter class from the collections module
# Understand: find the start indices of p's anagrams in s
# Match the problem with the sliding window algorithm
# Plan: use the sliding window algorithm with the Counter class
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding Window with Hashmap
        np = len(p)
        if len(s) < np:
            return []
        sCounter = Counter()
        pCounter = Counter(p)
        res = []
        for i in range(len(s)):
            # keep track pointer i as the end of the window
            sCounter[s[i]] += 1
            if i >= np:
                # keep track pointer i-np as the start of the window
                if sCounter[s[i-np]] == 1:
                    del sCounter[s[i-np]]
                else:
                    sCounter[s[i-np]] -= 1
            # compare the two counters
            if sCounter == pCounter:
                res.append(i-np+1)
        return res

# LC202 Happy Number: https://leetcode.com/problems/happy-number/
'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
# method 1: use the Floyd's cycle-finding algorithm
# Understand: determine if a number n is happy
# Match: the problem is related to the cycle detection
# Plan: use the Floyd's cycle-finding algorithm to detect
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        slow, fast = n, get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
# method 2: use the hashset to store the sum of the squares of the digits
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
    