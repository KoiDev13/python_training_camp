# Input Validation
## The PyInputPlus Module

inputStr() Is like the built-in input() function but has the general PyInputPlus features. You can also pass a custom validation function to it

inputNum() Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it

inputChoice() Ensures the user enters one of the provided choices

inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

inputDatetime() Ensures the user enters a date and time

inputYesNo() Ensures the user enters a “yes” or “no” response

inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value

inputEmail() Ensures the user enters a valid email address

inputFilepath() Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists

inputPassword() Is like the built-in input(), but displays * characters as the user types so that passwords, or other sensitive information, aren’t displayed on the screen


## Help
help(pyinputplus.parameters)
* ``prompt`` (str): The text to display before each prompt for user input. Identical to the prompt argument for Python's ``raw_input()`` and ``input()`` functions.
* ``default`` (str, None): A default value to use should the user time out or exceed the number of tries to enter valid input.
* ``blank`` (bool): If ``True``, a blank string will be accepted. Defaults to ``False``.
* ``timeout`` (int, float): The number of seconds since the first prompt for input after which a ``TimeoutException`` is raised the next time the user enters input.
* ``limit`` (int): The number of tries the user has to enter valid input before the default value is returned.
* ``strip`` (bool, str, None): If ``None``, whitespace is stripped from value. If a str, the characters in it are stripped from value. If ``False``, nothing is stripped.
* ``allowlistRegexes`` (Sequence, None): A sequence of regex str that will explicitly pass validation.
* ``blocklistRegexes`` (Sequence, None): A sequence of regex str or ``(regex_str, error_msg_str)`` tuples that, if matched, will explicitly fail validation.
* ``applyFunc`` (Callable, None): An optional function that is passed the user's input, and returns the new value to use as the input.
* ``postValidateApplyFunc`` (Callable, None): An optional function that is passed the user's input after it has passed validation, and returns a transformed version for the ``input*()`` function to return.

## The min, max, greaterThan, and lessThan Keyword Arguments
- Accept int and float numbers
- Specifying a range of valid values

>   response = pyip.inputNum('>', min=4, lessThan=6)
  
## The blank Keyword Argument
- Accept blank
  
## The limit, timeout, and default Keyword Arguments
- Limit gioi han so lan nhap vao
- Time out la so giay nhap vao
- Defaut value instead of raising an exception

> response = pyip.inputNum(timeout=10)

> pyip.inputNum(limit=2, default='N/A')

## The allowRegexes and blockRegexes Keyword Arguments