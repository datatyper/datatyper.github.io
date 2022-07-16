title: A Complete Guide to Markdown
author: Philip
status: published
tags: reference, guide
date: 2021-11-23
summary: A complete guide to the Markdown language. Use it as a reference for your static website or GitHub readme files.
cover: markdown.png

[TOC]

# # This is Heading 1
## ## This is Heading 2
### ### This is Heading 3
#### #### This is Heading 4
##### ##### This is Heading 5

A horizontal rule is three or more dashes, asterisks, or underscores (e.g. `---` or `***` or `___`).  

---

# Text Styling 

Get bold or italic text using `*` or `_`

This is \**italic*\*. This is \*\***bold**\*\*. This is \*\*\****bold and italic***\*\*\*.  

Description    | Syntax      | Effect
-------------- | ----------- | -----------  
Italic         | `*datatype*` or `_datatype_`    | *datatype*
Bold           | `**datatype**` or `__datatype__`| **datatype**
Bold Italic    | `***datatype***` or `___datatype___`    | ***datatype***
Inline code    | `` `dataatype` `` | `datatype`
Strikethrough  | `~~datatype~~`      | ~~datatype~~

# Lists

## Unordered List

Create an unordered list with a dash `-` or asterisk `*`:  

```
- List item 1  
- List item 2  
- List item 3
    - List item 3a
    - List item 3b
- List item 4
```

- List item 1  
- List item 2  
- List item 3
    - List item 3a
    - List item 3b
- List item 4

## Ordered List

Create an ordered list with any number and a period (e.g. `1.`): 

```
1. List item
1. List item
1. List item
    1. List item
    1. List item
1. List item
```

1. List item
1. List item
1. List item  
    1. List item
    1. List item
1. List item

# Blockquotes

A block quote with a `>`

```
> This is a block quote.  
> This is the same block quote.
```

> This is a block quote.  
> This is the same block quote.

# Code

Create inline code by surrounding text with single backticks `` ` ``, e.g. `` `E = mc^2` ``.

A code block uses three backticks `` ``` ``,:

```md
 ```python
for i in range(10):
    print('Datatype')
 ``` 
```

```python
for i in range(10):
    print('Datatype')
```

Note the "python" after the first three backticks to get the code block to be interpreted as Python.

# Links

## Hyperlinks

This is a link to `[Wikipedia](https://en.wikipedia.org/wiki/Markdown)`  
This is a link to [Wikipedia](https://en.wikipedia.org/wiki/Markdown)  

## Images

This is an image,  
`![Solar System](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Planets2013.svg/390px-Planets2013.svg.png)`

This is an image,  
![Solar System](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Planets2013.svg/390px-Planets2013.svg.png)


# Markdown Extra {#markdown-extra}

It is possible to get additional markdown support with the Markdown Extra extension. You can find a list of the available features [here](https://python-markdown.github.io/extensions/).

## Tables

Tables are created with a pipe `|`,

```md
A | B | C
---|---|---
1 | 2 | 3
4 | 5 | 6
```

To get,

a | b | c
---|---|---
1 | 2 | 3
4 | 5 | 6

You can align the columns with a colon `:`

```md
left | center | right
:---|:---:|:---
cell | cell | cell
cell | cell | cell
```

left | center | right
:---|:---:|:---
cell | cell | cell
cell | cell | cell


## Abbreviations  
Declare some abbreviations (which are also useful for tooltip definitions) and then use them in your text,

```markdown
*[MD]: Markdown
*[HTML]: Hypertext Markup Language
*[CSS]: Cascading Style Sheets
```

*[MD]: Markdown
*[HTML]: Hypertext Markup Language
*[CSS]: Cascading Style Sheets

This page is written in MD, converted to HTML and styled with CSS.

## Attribute List
Add custom classes by adding `{: .classname}` _after_ a markdown element.

For example,
```md
This is a highlighted paragraph
{: .highlight}
```
will produce (with some css styling),

This is a highlighted paragraph
{: .highlight}

## Definition Lists
Create definition lists with,

```md
Mercury
: The smallest planet in the solar system.

Venus
: The second smallest planet in the solar system.

Earth
: The third planet from the sun.
: The red planet.
: Where the martians are from.
```

To produce,

Mercury
: The smallest planet in the solar system.

Venus
: The second smallest planet in the solar system.

Earth
: The third planet from the sun.

Mars
: The fourth planet from the sun.
: Where the martians are from.
: The red planet.

## Admonition

Create alerts with,
```md
!!! warning
    This is a warning message.  
    This is a warning message.  
    This is a warning message.  

!!! danger
    This is a danger message.

!!! info
    This is information message.

!!! success
    This is a success message.
```

!!! warning
    This is a warning message.  
    This is a warning message.  
    This is a warning message.  

!!! danger
    This is a danger message.

!!! info
    This is information message.

!!! success
    This is a success message.