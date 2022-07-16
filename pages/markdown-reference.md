title: A Complete Guide to Markdown
subtitle: The Lowdown on Markdown
summary: Your complete guide to the Markdown language. Use it as a reference for your static website or GitHub ReadMe files.
author: Philip Mannering
date: 2021-11-23
status: published
category: miscellaneous
tags: [reference, guide]

[TOC]

# Titles and Subtitles

# # This is Heading 1
## ## This is Heading 2
### ### This is Heading 3
#### #### This is Heading 4
##### ##### This is Heading 5
###### ###### This is Heading 6

Markdown is the simplest way to create a static website. It is a plain text format that is easy to read and write. Indeed, the page you're reading now was initially typed up in Markdown. You can then use this [Python-Markdown](https://pypi.org/project/Markdown/) module to convert this to HTML. Then use [Jinja2](https://pypi.org/project/Jinja2/) to insert into an HTML template. Indeed this is what I've used to create the webpage you're reading now.

# Horizontal Rule  

A horizontal rule is three or more dashes, asterisks, or underscores (e.g. `---`, `***`, `___`).  

---

# Text Styling 

Get bold or italic text by surrounding text with asterisks `*` or underscores `_`

This is \**italic*\*. This is \*\***bold**\*\*. This is \*\*\****bold and italic***\*\*\*. The complete list of styling text inlined in markdown is:

Style          | Syntax      | Result
-------------- | ----------- | -----------  
Italic         | `*datatype*` or `_datatype_`    | *datatype*
Bold           | `**datatype**` or `__datatype__`| **datatype**
Bold italic    | `***datatype***` or `___datatype___`    | ***datatype***
Inline code    | `` `dataatype` `` | `datatype`
Strikethrough  | `~~datatype~~`      | ~~datatype~~


# Tables

Tables are much simpler in Markdown than they are in HTML. Simply add a few pipes (`|`) to separate the columns and a row of dashes `---` to separate the headers with the values. On this row you can use the `:` character to align the columns.
 
Left  \| Center \| Right  
:----\|:------:\|------:  
Value \| Value  \| Value  
Value \| Value  \| Value  
{.code}

Becomes,  
<!-- Make sure there is a space before the table -->

Left  | Center | Right  
:-----|:------:|------:  
Value | Value  | Value  
Value | Value  | Value  


# Lists

## Unordered Lists

Create an unordered list with a dash (`-`) or asterisk (`*`) at the beginning of each line.  

\- list item  
\- list item  
&nbsp;&nbsp;\- list item  
&nbsp;&nbsp;&nbsp;&nbsp;\- list item  
&nbsp;&nbsp;\- list item  
\- list item  
{.code}

- list item
- list item
    - list item
        - list item
    - list item
- list item

## Ordered Lists

Create an ordered list with any number and a period. Any number can be used (e.g. all `1.`) and markdown will automatically number the list appropriately


1\. List item  
1\. List item  
&nbsp;&nbsp;1\. List item  
&nbsp;&nbsp;&nbsp;&nbsp;1\. List item    
&nbsp;&nbsp;1\. List item  
1\. List item  
{.code}

1. List item
1. List item
    1. List item
        1. List item  
    1. List item
1. List item

# Block Quote

Create a block quote by starting each line with a `>`

\> This is a block quote.  
\> This is the same block quote.
{.code}

To produce,

> This is a block quote.  
> This is the same block quote.


# Code

Create inline code by surrounding text with single backticks `` ` ``, e.g. `` `E = mc^2` ``.

A code block uses three backticks or three tildes to delimit the code.

\```python  
\# print 'hello' 10 times  
for i in range(10):  
&nbsp;&nbsp;print('hello')  
\```
{.code}  

To produce,

```python
# print 'hello' 10 times
for i in range(10):
    print('hello')
```

# Links

The markdown syntax for creating links is:

This is a link: \[Wikipedia](https://en.wikipedia.org/wiki/Markdown).
{.code}

To produce,

This is a link: [Wikipedia](https://en.wikipedia.org/wiki/Markdown).

# Images

The markdown syntax for creating images is:

This is an image: !\[](https://en.wikipedia.org/wiki/Markdown#/media/File:Markdown-mark.svg)
{.code}

This is an image: ![](https://en.wikipedia.org/wiki/Markdown#/media/File:Markdown-mark.svg)


# Markdown Extra {#markdown-extra}

It is possible to get additional markdown support with the Markdown Extra extension. You can find a list of the available features [here](https://python-markdown.github.io/extensions/).

## Abbreviations  
Declare some abbreviations (which are also useful for tooltip definitions) and then use them in your text,

\*[MD]: Markdown  
\*[HTML]: Hypertext Markup Language  
\*[CSS]: Cascading Style Sheets<br>  
This page is written in MD, converted to HTML and styled with CSS.
{.code}

To produce,

*[MD]: Markdown  
*[HTML]: Hypertext Markup Language  
*[CSS]: Cascading Style Sheets  

This page is written in MD, converted to HTML and styled with CSS.

## Attribute List
Create custom classes by adding `{: .classname}` after a markdown element.

For example,

This is a highlighted paragraph  
\{.inverse}
{.code}

To produce (with CSS styling),

This is a hightlighted paragraph
{: .inverse}

## Definition Lists
Create definition lists with,

Mercury <br>: The smallest planet in the solar system.<br>  
Venus <br>: The second smallest planet in the solar system.<br>  
Earth <br>: The third planet from the sun.  <br>: The red planet.  <br>: Where the martians are from.
{.code}

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

## Admonition

Create some admonitions / alerts with:


\!!! warning  
    This is a warning message.  
    This is a warning message.  
    This is a warning message.  
<br>
\!!! danger  
    This is a danger message.  
<br>
\!!! info  
    This is information message.  
<br>
\!!! success  
    This is a success message.
{.code}


!!! warning
    This is a warning message.  
    This is a warning message.  
    This is a warning message.  

!!! danger
    This is a danger message.

!!! info
    This is an information message.

!!! success
    This is a success message.

## Using HTML

<div class="row" markdown=1>
<div class="col" markdown=1>
# Left
The paragraph on the right
</div>
<div class="col" markdown=1>
# Right
The paragraph on the right
</div>
</div>
