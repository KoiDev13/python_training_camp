# Regex Object
Regular expressions = regexes

Review of Regular Expression Matching
While there are several steps to using regular expressions in Python, each step is fairly simple.

1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual matched text.


## Grouping with Parentheses
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

## Matching Multiple Groups with the Pipe | 
    findall() method
    first occurrence of matching text will be returned
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

## Optional Matching with the Question Mark ? Optional part
The ? character flags the group that precedes it as an optional part of the pattern.
batRegex = re.compile(r'Bat(wo)?man')

## Matching Zero or More with the Star
The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text. It can be completely absent or repeated over and over again. 
batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
'Batwowowowoman'

## Matching Specific Repetitions with Braces
If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in braces.
(Ha){3}
(Ha)(Ha)(Ha)
haRegex = re.compile(r'(Ha){3}')

## Greedy and Non-greedy Matching
Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy (also called lazy) version of the braces, which matches the shortest string possible, has the closing brace followed by a question mark.

> greedyHaRegex = re.compile(r'(Ha){3,5}')
> mo1 = greedyHaRegex.search('HaHaHaHaHa')
> mo1.group()
'HaHaHaHaHa'

> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
> mo2.group()
>'HaHaHa'

## The findall() Method
Using findall() instead of search()

## Character Classes
\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the underscore character.
\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S Any character that is not a space, tab, or newline.

## Making Your Own Character Classes
By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class

## The Caret and Dollar Sign Characters
symbol (^) at the start -  a match must occur at the beginning
dollar sign ($) at the end -  to indicate the string must end with this regex pattern

## The Wildcard Character
The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

## Matching Everything with Dot-Star
 noNewlineRegex = re.compile('.*')

## Review of Regex Symbols

The ? matches zero or one of the preceding group.

The * matches zero or more of the preceding group.

The + matches one or more of the preceding group.

The {n} matches exactly n of the preceding group.

The {n,} matches n or more of the preceding group.

The {,m} matches 0 to m of the preceding group.

The {n,m} matches at least n and at most m of the preceding group.

{n,m}? or *? or +? performs a non-greedy match of the preceding group.

^spam means the string must begin with spam.

spam$ means the string must end with spam.

The . matches any character, except newline characters.

\d, \w, and \s match a digit, word, or space character, respectively.

\D, \W, and \S match anything except a digit, word, or space character, respectively.

[abc] matches any character between the brackets (such as a, b, or c).

[^abc] matches any character that isn’t between the brackets.


## Case-Insensitive Matching
re.IGNORECASE
robocop = re.compile(r'robocop', re.I)

## Substituting Strings with the sub() Method
> namesRegex = re.compile(r'Agent \w+')
> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'

## Managing Complex Regexes