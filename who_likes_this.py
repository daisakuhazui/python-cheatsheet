# -*- coding:utf-8 -*-
def likes(names: list[str]) -> str:
    """
    You probably know the "like" system from Facebook and other pages.
    People can "like" blog posts, pictures or other items.
    We want to create the text that should be displayed next to such an item.

    Implement a function likes :: [String] -> String,
    which must take in input array, containing the names of people who like an item.
    It must return the display text as shown in the examples:

    likes([]) # must be "no one likes this"
    likes(["Peter"]) # must be "Peter likes this"
    likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
    likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
    likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
    """
    names_length = len(names)

    if names_length == 0:
        return 'no one likes this'
    elif names_length == 1:
        text = '{} likes this'
        return text.format(names[0])
    elif names_length == 2:
        text = '{0} and {1} like this'
        return text.format(names[0], names[1])
    elif names_length == 3:
        text = '{0}, {1} and {2} like this'
        return text.format(names[0], names[1], names[2])

    text = '{0}, {1} and {2} others like this'
    return text.format(names[0], names[1], names_length - 2)
