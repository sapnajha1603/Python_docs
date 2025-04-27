'''
match statements (also known as match-case statements) were introduced in Python 3.10 as 
part of the Structural Pattern Matching feature. They provide a more readable and expressive way to
 handle multiple conditional branches, similar to switch-case statements in other programming languages.

 Basic syntax
 match variable:
    case pattern1:
        # Code for pattern1
    case pattern2:
        # Code for pattern2
    ...
    case _:
        # Code for the default case (optional)

Advantages of match-case

    Readability: The match-case statement can be more readable and concise, especially when dealing with multiple conditions.

    Pattern Matching: match-case supports more advanced pattern matching features, such as matching data structures 
    (tuples, lists, dictionaries), extracting values, and more.

'''

num  = int(input("Enter a number: "))
match num:
    case 1:
        return "one"
    case 2:
        return "two"
    case 3:
        return "three"
    case _:
        return "other"


        

