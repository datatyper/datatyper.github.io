title:Post Guide
slug:path-to-page
date:2020-01-01
tags:template, reference
author:philip
summary:This provides an excerpt for the Post Template post. It is displayed when the post is shared and in the homepage summary.
status: published


A Reference Guide to creating posts for Pelican websites
=====

<!-- ## Metadata keys and values
|Metadata   |Description                                                |
|-----------|-----------------------------------------------------------|
|title      |Title of the article or page                               |
|date       |Publication date (`YYYY-MM-DD HH:SS`)                      |
|modified   |Modification date (`YYYY-MM-DD HH:SS`)                     |
|tags       |Content tags, separated by commas                          |
|keywords   |Content keywords, separated by commas (HTML content only)  |
|category   |Content category (one only — not multiple)                 |
|slug       |Identifier used in URLs and translations                   |
|author     |Content author, when there is only one                     |
|authors    |Content authors, when there are multiple                   |
|summary    |Brief description of content for index pages               |
|lang       |Content language ID (en, fr, etc.)                         |
|translation|If content is a translation of another (`true` or `false`) |
|status     |Content status: `draft`, `hidden` or `published`           |
|template   |Name of the template to use to generate content            |
|save_as    |Save content to this relative file path                    |
|url        |URL to use for this article/page                           | -->
Here is some codewritten in,

- Python  
- Jupyter  
- etc

Another list,  

+ milk
+ eggs
+ eggs



```python
for i in range(10):
    print(i, 'hello')

print('done!')
```

## Markdown Posts
The format for markdown posts and Jupyter Notebooks is colon separated keys and values at the top of the file. The minimum required is a title and date. For example,
```
title: Posts Guide
date: 2021-06-11
```

## HTML Posts
Here is `some text` formatted as code.
Posts written in HTML use the `<meta>` tag. Such as,
```html
<head>
    <title>Posts Guide</title>
    <meta name="tags" content="awesome, stuff" />
    <meta name="date" content="2021-06-11 22:00" />
    <meta name="category" content="miscellaneous" />
    <meta name="author" content="Philip" />
    <meta name="summary" content="This provides an excerpt for the Post Template post. It is displayed when the post is shared and in the homepage summary." />
</head>
```

