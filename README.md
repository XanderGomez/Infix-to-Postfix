# Infix-to-Postfix
This program is a terminal based program that will repeatedly ask the user for an equation to input.This equation is then converted to postfix and printed out for the user and then passed to a functionfor evaluation. 

The program only supports equations utilizing *, /, +, and - operators as well as only numbers. It does however support numbers greater than 1 digit so it is not limited to only doing math with 0-9 digits. Also catches edge cases such as open parentheses, multiples operators such as **, ++, */, -+, etc., letters being inputed, numbers without evaluation(such as (3)3-2), and also makes sure to remove whitespace in the inputted equation so evaluation can be conducted only on the inputted values.
