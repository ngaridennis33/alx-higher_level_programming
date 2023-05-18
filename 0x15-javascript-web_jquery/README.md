![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> Web Jquery

![please-forgive-me](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg)


## About
jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, animation, and Ajax (asynchronous JavaScript and XML) interactions for web development. It was released in 2006 by John Resig and has since become one of the most popular JavaScript libraries used by web developers. In this project, we will take a deep dive into Jquery to understand how to use it for the above mentioned functionalities and even more. Overall, jQuery is a powerful and widely-used tool for web development that can help simplify many common tasks and streamline the process of building interactive web applications.

## Concepts
For this project, look at the following concepts
- [JavaScript in the browser](https://intranet.alxswe.com/concepts/3)
- [Dealing with data statically versus dynamically](https://intranet.alxswe.com/concepts/35)

![did-somebody-say-jquery](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg)

## Resources
__Read or watch__:
1. [What is JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
2. [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
3. [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
4. [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
5. [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
6. [API](https://oscarotero.com/jquery/)
7. [Introdudction](https://jquery-tutorial.net/ajax/introduction/)
8. [GET and POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
9. [Jquery Ajax Tutorial#1 - Using Ajax and API's](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
10. [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
11. [Jquery](https://jquery.com/)
12. [Jquery API](https://api.jquery.com/)
13. [Jquery Ajax](https://learn.jquery.com/ajax/)

## Learning objectives
### General
By the end of this project, you are expected to be able to [explain to anyone]() __Without the help of Google__:


* [X] Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
* [X] How to select HTML elements in JavaScript
* [X] How to select HTML elements with JQuery
* [X] What are differences between ID, class and tag name selectors
* [X] How to modify an HTML element style
* [X] How to get and update an HTML element content
* [X] How to modify the DOM
* [X] How to make a GET request with JQuery Ajax
* [X] How to make a POST request with JQuery Ajax
* [X] How to listen/bind to DOM events

## More info
Import Jquery

```javascript
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

## Quiz
[Quizes](./quiz.md)
Tasks
-----

### 0\. Safe list printing

mandatory

Write a function that prints `x` elements of a list.

-   Prototype: `def safe_print_list(my_list=[], x=0):`
-   `my_list` can contain any type (integer, string, etc.)
-   All elements must be printed on the same line followed by a new line.
-   `x` represents the number of elements to print
-   `x` can be bigger than the length of `my_list`
-   Returns the real number of elements printed
-   You have to use `try: / except:`
-   You are not allowed to import any module
-   You are not allowed to use `len()`

```
guillaume@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x05-python-exceptions`
-   File: `0-safe_print_list.py`

### 1\. Safe printing of an integers list

mandatory

Write a function that prints an integer with `"{:d}".format()`.

-   Prototype: `def safe_print_integer(value):`
-   `value` can be any type (integer, string, etc.)
-   The integer should be printed followed by a new line
-   Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
-   Otherwise, returns `False`
-   You have to use `try: / except:`
-   You have to use `"{:d}".format()` to print as integer
-   You are not allowed to import any module
-   You are not allowed to use `type()`

```
guillaume@ubuntu:~/0x05$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/0x05$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x05-python-exceptions`
-   File: `1-safe_print_integer.py`

### 2\. Print and count integers

mandatory

Write a function that prints the first `x` elements of a list and only integers.

-   Prototype: `def safe_print_list_integers(my_list=[], x=0):`
-   `my_list` can contain any type (integer, string, etc.)
-   All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
-   `x` represents the number of elements to access in `my_list`
-   `x` can be bigger than the length of `my_list` - if it's the case, an exception is expected to occur
-   Returns the real number of integers printed
-   You have to use `try: / except:`
-   You have to use `"{:d}".format()` to print an integer
-   You are not allowed to import any module
-   You are not allowed to use `len()`

```
guillaume@ubuntu:~/0x05$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers =\
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/0x05$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x05-python-exceptions`
-   File: `2-safe_print_list_integers.py`

### 3\. Integers division with debug

mandatory

Write a function that divides 2 integers and prints the result.

-   Prototype: `def safe_print_division(a, b):`
-   You can assume that `a` and `b` are integers
-   The result of the division should print on the `finally:` section preceded by `Inside result:`
-   Returns the value of the division, otherwise: `None`
-   You have to use `try: / except: / finally:`
-   You have to use `"{}".format()` to print the result
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x05$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x05-python-exceptions`
-   File: `3-safe_print_division.py`

### 4\. Divide a list

mandatory

Write a function that divides element by element 2 lists.

-   Prototype: `def list_division(my_list_1, my_list_2, list_length):`
-   `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
-   `list_length` can be bigger than the length of both lists
-   Returns a new list (length = `list_length`) with all divisions
-   If 2 elements can't be divided, the division result should be equal to `0`
-   If an element is not an integer or float:
    -   print: `wrong type`
-   If the division can't be done (`/0`):
    -   print: `division by 0`
-   If `my_list_1` or `my_list_2` is too short
    -   print: `out of range`
-   You have to use `try: / except: / finally:`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x05$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

guillaume@ubuntu:~/0x05$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/0x05$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x05-python-exceptions`
-   File: `4-list_division.py`

### 5\. Raise exception

mandatory

Write a function that raises a type exception.

-   Prototype: `def raise_exception():`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

guillaume@ubuntu:~/0x05$ ./5-main.py
Exception raised
guillaume@ubuntu:~/0x05$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x05-python-exceptions`
-   File: `5-raise_exception.py`

### 6\. Raise a message

mandatory

Write a function that raises a name exception with a message.

-   Prototype: `def raise_exception_msg(message=""):`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x05$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/0x05$ ./6-main.py
C is fun
guillaume@ubuntu:~/0x05$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x05-python-exceptions`
-   File: `6-raise_exception_msg.py`
