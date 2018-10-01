# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

teststring = 'pwwkew'

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    seen_before = []
    len_counter = 0
    for letter in s:
        print(letter)
        if letter in seen_before:
            if len(seen_before) > len_counter:
                biglist = seen_before[:]
                len_counter = len(biglist)
            del seen_before[:]
            print('deleting seen before')
            print(f'len_counter is {len_counter}')
            print(f'biglist is {biglist}')
            seen_before.append(letter)
            print('new seen before', seen_before)
        else:
            seen_before.append(letter)
            print('appending, seen before is now', seen_before)
    return ''.join(biglist)

print(lengthOfLongestSubstring(teststring))
