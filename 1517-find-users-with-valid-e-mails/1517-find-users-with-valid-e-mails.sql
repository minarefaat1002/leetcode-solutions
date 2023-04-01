# Write your MySQL query statement below
SELECT
  *
FROM
  Users
WHERE
  mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$';
# Explanation: The regular expression may be broken down in chunks and explained as follows (refer to the documentation immediately below if needed):

# ^[a-zA-Z]: The email must start with an alphanumeric letter (i.e., not digit). [Ref: D2, D5a]
# [a-zA-Z0-9_.-]*:
# The next zero or more characters must be either alphanumeric (letters a-z, A-Z, or digits 0-9) [Ref: D4, D5a]
# or a _ or . [Ref: D5b]
# or a - [Ref: D5c]
# @leetcode[.]com$:
# @leetcode: The next sequence of characters must exactly match @leetcode
# [.]: The . character within a [] pair does not have special meaning so it must be matched exactly after @leetcode. [Ref: D5c]
# com$: The string must end with com. [Ref: D3]