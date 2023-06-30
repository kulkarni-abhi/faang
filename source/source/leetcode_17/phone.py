
"""
Leetcode #17
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Fastest Solution ->
https://www.youtube.com/watch?v=0snEunUacZY


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]


     ,------,-----,-----,
     |   1  |  2  |  3  |
     |  @,- | abc | def |
     '------'-----'-----'
     |   4  |  5  |  6  |
     |  ghi | jkl | mno |
     '------'-----'-----'
     |   7  |  8  |  9  |
     | pqrs | tuv |wxyz |
     '------'-----'-----'



"""

def letters(digits):
    result = []
    digit_chars_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def dfs(pos, current_string):
        if len(current_string) == len(digits):
            result.append(current_string)
            return

        for char in digit_chars_map[digits[pos]]:
            dfs(pos + 1, current_string + char)

    if digits:
        dfs(0, "")

    return result

num = "23"
print(letters(num))
