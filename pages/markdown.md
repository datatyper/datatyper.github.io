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

A horizontal rule is three or more dashes, asterisks, or underscores (e.g. \-\-\-, \*\*\*, \_\_\_).  

---

```python
# This is a code block
for i in range(10):
    print(i)
```


This is a regular paragraph.  
This is \**italic*\* text.  
This is \*\***bold**\*\* text.  
This is \*\*\****bold and italic***\*\*\* text.  

"This has quotation marks" -- "and".  
It's got an apostrophe - it works
Ellipsis...

This is ~~strikethrough~~ text.  
This is some ^^superscript^^ text.  
This is some ~~~subscript~~~ text.

Syntax      | Description
----------- | -----------  
`\*\*`      | Bold
`\_`        | Italic
`\*\*\*`    | Bold + Italic
`\~\~`      | Strikethrough
`\^\^`      | Superscript
`\~\~\~`    | Subscript

An unordered list with a dash or asterisk:  

- List item 1  
- List item 2  
- List item 3
    - List item 3a
    - List item 3b
- List item 4

An ordered list with any number and a period (e.g. `1.`): 

1. List item 1
1. List item 2
1. List item 3  
1. a List item 3.1  
    1. b List item 3.2
2. List item 4

A block quote with a `>`
> \> This is a block quote.  
> \> This is the same block quote.

Inline code with backticks, e.g. `E = mc^2`.

A code block uses three backticks:

```powershell
This is a code block.
```


This is a link to \[Wikipedia\](https://en.wikipedia.org/wiki/Markdown).  
This is a link to [Wikipedia](https://en.wikipedia.org/wiki/Markdown).

This is an image,  

![Solar System](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Planets2013.svg/390px-Planets2013.svg.png)


## Markdown Extra {#markdown-extra}

### Abbreviations  
Declare some abbreviations (which are also useful for tooltip definitions) and then use them in your text,

```markdown
*[HTML]: Hypertext Markup Language
*[MD]: Markdown
*[CSS]: Cascading Style Sheets

This page is written in MD, converted to HTML and styled with CSS.
```

*[HTML]: Hypertext Markup Language
*[MD]: Markdown
*[CSS]: Cascading Style Sheets

This page is written in MD, converted to HTML and styled with CSS.

### Attribute List
Create custom classes by adding `{: .classname}` after a markdown element.

For example,
```md
This is a highlighted paragraph
{: .highlight}
```

To produce (with some css styling),

This is a hightlighted paragraph
{: .highlight}

### Definition Lists
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
: The red planet.
: Where the martians are from.

### Admonition



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