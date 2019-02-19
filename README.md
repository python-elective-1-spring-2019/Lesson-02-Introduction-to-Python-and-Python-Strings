# Lesson 02: Introduction to python and python strings
<div align="right">
<a href="../../../Lesson-01-Introduction-to-the-Python-elective/blob/master/README.md">prev</a> | 
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson_03_Python_Types_simple_types_Lists_Tuples_and_Sorting_Functions/blob/master/README.md">next</a>
</div>

> Agenda 19-02-2019

Today we will jump into the python programming world. You will get an overview of the language and you will start to get familiar with the language and the development enviroment. We will focus these first lesson on strings and string manipulations.
## Required reading
* [3. An Informal Introduction to Python](https://docs.python.org/3.7/tutorial/introduction.html#an-informal-introduction-to-python)
* [3.1. Using Python as a Calculator](https://docs.python.org/3.7/tutorial/introduction.html#using-python-as-a-calculator)
* [3.1.1. Numbers](https://docs.python.org/3.7/tutorial/introduction.html#numbers)
* [3.1.2. Strings](https://docs.python.org/3.7/tutorial/introduction.html#strings)
* [Text Sequence Type — str](https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str)
* [String Methods](https://docs.python.org/3.7/library/stdtypes.html#string-methods)
* [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/)


### Suplementary reading
* [RealPython Search results for "string"](https://realpython.com/search?q=string)
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [Splitting, Concatenating, and Joining Strings in Python](https://realpython.com/python-string-split-concatenate-join/)


## Exercises

* [string1.py](exercises/string1.py)
* [string2.py](exercises/string2.py)
<!--
* [letter_change.py](exercises/letter_change.py)
* [Python Strings and Character Data Quiz](https://realpython.com/quizzes/python-strings/)
* [Python Strings and Character Data Quiz](https://realpython.com/quizzes/python-strings/)
-->

## Strings

### Slicing
The "slice" syntax is a handy way to refer to sub-parts of sequences -- typically strings and lists. The slice s[start:end] is the elements beginning at start and extending up to but not including end. Suppose we have s = "Hello"

![](other_materials/hello.png)

* s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
* s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
* s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
* s[1:100] is 'ello' -- an index that is too big is truncated down to the string length

The standard zero-based index numbers give easy access to chars near the start of the string. As an alternative, Python uses negative numbers to give easy access to the chars at the end of the string: s[-1] is the last char 'o', s[-2] is 'l' the next-to-last char, and so on. Negative index numbers count back from the end of the string:

* s[-1] is 'o' -- last char (1st from the end)
* s[-4] is 'e' -- 4th from the end
* s[:-3] is 'He' -- going up to but not including the last 3 chars.
* s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

It is a neat truism of slices that for any index n, s[:n] + s[n:] == s. This works even for n negative or out of bounds. Or put another way s[:n] and s[n:] always partition the string into two string parts, conserving all the characters. As we'll see in the list section later, slices work with lists too. _(dev.google.com)_




<div align="center">
<a href="../../../Lesson-01-Introduction-to-the-Python-elective/blob/master/README.md">prev</a> | 
<a href="https://python-elective-1-spring-2019.github.io/">index</a> | 
<a href="../../../Lesson_03_Python_Types_simple_types_Lists_Tuples_and_Sorting_Functions/blob/master/README.md">next</a>
</div>
