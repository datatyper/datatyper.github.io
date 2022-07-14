title: Pelican: Python's Static Website Builder
slug: pelican
category: python
tags: python
summary: testing123


<!-- cover:assets/images/Pelican-in-flight.webp -->
# Pelican Powered Websites

It can be difficult to know where to start when creating a website. 
<!-- Is the frontend based on a CMS like WordPress or HTML, CSS and JavaScript? -->

## The Why

There are many different options. Two such options are _static_ and _dynamic_. Dynamic basically means that the website has a backend server storing the content. Static means that it's serverless, not that you can't have dynamic elements on the page. 
The advantages of a static site is that they are simpler to build, require less maintenance and load quicker.
The disadvantages are x, y and z. But for most blogs and smaller websites the pros outweigh the cons.

So how can you build a static site? You need a static site generator. It turns out that there are many different static site generators written in different programming languages. Some popular ones are,

- Hugo (written in Go)
- Jekyll (written in Ruby)
- ...
- Pelican (written in Python)

Since I'm a Pythonista, I went with the Python based option Pelican.

Pelican is a command line tool that takes a folder full of markdown (or HTML files) and a Template (a site theme) and generates a complete website where the markdown files get converted to posts.

## How do I Use Pelican?

Documentation for installing Pelican can be found [here](www.bbc.co.uk). But, in Powershell, it's as easy as:
```powershell
pip install pelican
```
Then create a new folder and move into that folder:
```powershell
mkdir Datatype
chdir Datatype
```
To get started type:
```powershell
pelican-quickstart
```
This will walk you through some questions asking you things like "What is the name of your site?" and "Who is the author?", after which it will create a couple of directories and two or three files (depending on where you answer "Y" to "Do you want to generate a task.py/Makefile to automate generation and publishing?")






