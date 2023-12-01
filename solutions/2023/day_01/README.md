# Day 1 (2023)

`TITLE` ([prompt](https://adventofcode.com/2023/day/1))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

- iterate over every character in given line of input text
  - check if current char is a digit
    - first digit already found => count as second digit
    - if there are more digits found while iterating => overwrite second digit with current found

## Part 2

- do the same as in part one but check substrings of given line of input text
  - check if the current substring starts with digit or with a defined string literal (zero ... nine)
    - do the same logic as in part1 considering first and second value