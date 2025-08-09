'''
itertools is a Python module that provides functions that create iterators for memory efficient looping.

Flow of contents:
1. count(): Creates an iterator that generates consecutive integers starting from a specified number.
2. cycle(): Creates an iterator that cycles through an iterable indefinitely.
3. repeat(): Creates an iterator that repeats an object a specified number of times or indefinitely.
4. accumulate(): Creates an iterator that returns accumulated sums or results of a binary function applied to the elements of an iterable.
5. chain(): Combines multiple iterables into a single iterable.
6. compress(): Filters elements from an iterable based on a selector iterable.
7. dropwhile(): Drops elements from an iterable as long as a predicate is true, then returns the rest.
8. filterfalse(): Filters elements from an iterable where a predicate is false.
9. groupby(): Groups elements from an iterable based on a key function.
10. islice(): Returns selected elements from an iterable based on specified start, stop, and step parameters.
11. pairwise(): Returns consecutive pairs of elements from an iterable.
12. starmap(): Applies a function to elements from multiple iterables, returning results as tuples.
13. takewhile(): Takes elements from an iterable as long as a predicate is true, then stops.
14. tee(): Creates multiple independent iterators from a single iterable.
15. zip_longest(): Combines multiple iterables into tuples, filling missing values with a specified fill value.
16. product(): Computes the Cartesian product of input iterables.
17. permutations(): Generates all possible orderings of elements in an iterable.
18. combinations(): Generates all possible combinations of a specified length from an iterable.
19. combinations_with_replacement(): Generates combinations of a specified length from an iterable, allowing repeated elements.
'''

#--------------------------------------------------------------------------------------------#
#-------------------------------------- 1. count() ------------------------------------------#
#--------------------------------------------------------------------------------------------#

# count() creates an iterator that generates consecutive integers starting from a specified number.
# It can be used to create an infinite sequence of numbers, which can be useful in various
'''
NOTE: it will not stop until you stop it manually (using a stop condition or KeyboardInterrupt Ctrl+C).
'''

from itertools import count

counter = count(start = 10, step = 2)  # Start from 5, increment by 2

for num in counter:
    print(num)
    if num == 30:  # Stop condition to prevent infinite loop
        break

# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28
# 30


#--------------------------------------------------------------------------------------------#
#-------------------------------------- 2. cycle() ------------------------------------------#
#--------------------------------------------------------------------------------------------#

# cycle() creates an iterator that cycles through an iterable indefinitely.
'''
NOTE: it will not stop until you stop it manually (using a stop condition or KeyboardInterrupt Ctrl+C).
'''

from itertools import cycle

colors = ['red', 'green', 'blue']

cyler = cycle(colors)

for i, color in enumerate(cyler):
    print(f"{i} - {color}")
    if i == 8:  # Stop after 9 iterations to prevent infinite loop
        break

# 0 - red
# 1 - green
# 2 - blue
# 3 - red
# 4 - green
# 5 - blue
# 6 - red
# 7 - green
# 8 - blue