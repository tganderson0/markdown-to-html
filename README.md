# Markdown to HTML converter

## Why?

For my web development class in college, we had to create HTML plans for each of our projects. Sometimes, I would forgtet this and write my plan in markdown instead. I wanted to just create a way that would convert md to html for me, with me only having to make minor corrections.

## How to use

```sh
$ python converter.py <FILENAME> <DESTINATION>
```

Alternatively, just run

```sh
$ python converter.py
```

And a message will show.

## Note

This is not perfect. Particularly, with nested unordered lists, it will get some wonky output. You will most likely have to fix those yourself afterwards

In addition, while the output is a completely valid html page, it definitely will not be beautiful to look at as source code.
