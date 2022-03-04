# 🐍 30 Days Of Python 

|# Day | Topics                                                    |
|------|:---------------------------------------------------------:|
| 01  |  [Introduction](./readme.md)|

<div align="center">
  <h1> 30 Days Of Python: Day 1 - Introduction</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/luizfpavanello/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/nandovicentin">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/nandovicentin?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/luizfpavanello/" target="_blank">Fernando Vicentin Pavanello</a><br>
  <small> First Edition: March, 2022</small>
  </sub>
</div>

![30DaysOfPython](./Images/python_TreviIT.png)

- [🐍 30 Days Of Python](#-30-days-of-python)
- [📘 Day 1](#-day-1)
  - [Welcome](#welcome)
  - [Introduction](#introduction)
  - [Why should I learn Python?](#why-should-I-learn-python)
  - [What is Python actually used for?](#what-is-python-actually-used-for)
  - [Do I need any additional equipment for the course?](#additional-equipment-for-the-course)
  - [Introduction to Python and computer programming](#introduction-to-python-and-computer-programming)
    - [How does a computer program work?](#how-does-a-computer-program-work)
    - [Natural languages vs. programming languages](#natural-languages-vs-programming-languages)
    - [What makes a language?](#what-makes-a-language)
    - [Compilation vs. interpretation](#compilation-vs-interpretation)
  - [Basic Python](#basic-python)
    - [Python Syntax](#python-syntax)
    - [Python Indentation](#python-indentation)
    - [Comments](#comments)
    - [Data types](#data-types)
      - [Number](#number)
      - [String](#string)
      - [Booleans](#booleans)
      - [List](#list)
      - [Dictionary](#dictionary)
      - [Tuple](#tuple)
      - [Set](#set)
    - [Checking Data types](#checking-data-types)
    - [Python File](#python-file)
  - [💻 Exercises - Day 1](#-exercises---day-1)
    - [Exercise: Level 1](#exercise-level-1)
    - [Exercise: Level 2](#exercise-level-2)
    - [Exercise: Level 3](#exercise-level-3)

  # 📘 Day 1

## Welcome

**Congratulations** for deciding to participate in a _30 days of Python_ programming challenge . In this challenge you will learn everything you need to be a python programmer and the whole concept of programming. 

## Introduction

Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, objected-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of Python programming language was derived from a British sketch comedy series, *Month Python's Flying Circus*.  The first version was released on February 20, 1991. This 30 days of Python challenge will help you learn the latest version of Python, Python 3 step by step. The topics are broken down into 30 days, where each day contains several topics with easy-to-understand explanations, real-world examples, many hands on exercises and projects.

This challenge is designed for beginners and professionals who want to learn python programming language. It may take 30 to 100 days to complete the challenge, people who actively participate on the telegram group have a high probability of completing the challenge.

## Why should I learn Python?

It is a programming language which is very close to human language and because of that it is easy to learn and use.

It is omnipresent, people use numerous Python-powered devices on a daily basis, whether they realize it or not. There have been millions (well, actually billions) of lines of code written in Python, which means almost unlimited opportunities for code reuse and learning from well-crafted examples. What's more, there is a large and very active Python community, always happy to help.

There are also a couple of factors that make Python great for learning:

  - It is easy to learn - the time needed to learn Python is shorter than for many other languages; this means that it's possible to start the actual programming faster;
  - It is easy to use for writing new software - it's often possible to write code faster when using Python;
  - It is easy to obtain, install and deploy - Python is free, open and multiplatform; not all languages can boast that.

If you're not familiar with any other languages, Python is great to begin with, because it will give you a solid foundation and allow you to learn other programming languages (e.g., C++, Java, or C) much easier and much faster. Learning Python is fun and trendy!

I hope this is enough to convince you to start learning Python. Python is eating the world and you are killing it before it eats you.

## What is Python actually used for?

Do you remember Battlefield 2, Battlefield 2142 and Battlefield Heroes - strategy and first person shooter games from EA DICE? All the games use Python for logic and server controls. Python is frequently used for creating open-source, free games, e.g., OpenRTS, PySol, Metin 2, or Frets On Fire - famous Guitar Hero-like games written in pygame.

And what about the major websites and services? Dropbox? UBER? Spotify? Pintrest? BuzzFeed? Yes. They were all written, to a greater or lesser extent, in Python. Other examples?

  - Internet Applications (BitTorrent, Jogger Publishing Assistant, TheCircle, TwistedMatrix)
  - 3D CAD/CAM (FreeCAD, Fandango, Blender, Vintech RCAM)
  - Enterprise Applications (Odoo, Tryton, Picalo, LinOTP 2, RESTx)
  - Image Applications (Gnofract 4D, Gogh, imgSeek, MayaVi, VPython)
  - Mobile Applications (Aarlogic C05/3, AppBackup, Pyroute)
  - Office Applications (calibre, faces, Notalon, pyspread)
  - Personal Information Managers (BitPim, Narval, Prioritise, Task Coach, WikidPad) [Source: https://wiki.python.org/moin/PythonProjects]

Generally, Python is a great choice for:

  - Web and Internet development (e.g., Django and Pyramid frameworks, Flask and Bottle micro-frameworks)
  - Scientific and numeric computing (e.g., SciPy - a collection of packages for the purposes of mathematics, science, and engineering; Ipython - an interactive shell that features editing and recording of work sessions)
  - Education (it's a brilliant language for teaching programming! And that's why we're offering this course to you!)
  - Desktop GUIs (e.g., wxWidgets, Kivy, Qt)
  - Software Development (build control, management, and testing - Scons, Buildbot, Apache Gump, Roundup, Trac)
  - Business applications (ERP and e-commerce systems - Odoo, Tryton) [Source: https://www.python.org/about/apps]

And many, many other projects and development tools.

## Do I need any additional equipment for the course?

The course can be accessed online through any Internet browser, on computers with Linux, Windows, or Mac OS.

For the best learning experience, we recommend having the Python 3 standard installation on your computer. A copy of Python 3 can be downloaded from https://www.python.org/downloads. The installation contains a software application called IDLE (Integrated Development and Learning Environment), which will enable you to execute simple Python commands and see the effects of executing your programs.

Linux users most probably have Python already installed, as Python's infrastructure is intensively used by many Linux OS components.

## Introduction to Python and computer programming

### How does a computer program work?

Let's start the absolute basics... A makes a computer usable. Without a program, a computer, even the most powerful one, is nothing more than just an object. Similarly, without a player, a piano is nothing than a wooden box.
Computers are able to perform very complex tasks, but this ability is not innate. A computer's nature is quite different, it can execute simple operations. For example, a computer cannot understand the value of a complicated mathematical function by itself, although this isn't beyond the realms of possibility in the near future.
Contemporary computers can only evaluate the results of very fundamentals operations, like adding or dividing, but they can do it very fast, and can repeat these actions virtually any number of times.
Imagine that you want to know the average speed you're reached during a long journey. You know the distance, you know the time, you need the speed.
Naturally, the computer will be able to compute this, but the computer is not aware of such things as distance, speed, or time. Therefore, it is necessary to instruct the computer to:

  - accept a number representing the distance;
  - accept a number representing the travel time;
  - divide the former value by the latter and store the result in the memory;
  - display the result (representing the average speed) in a readable format.

These four simple actions form a program. Of course, these examples are not formalized, and they are very far from what the computer can understand, but they are good enough to be translated into a language the computer can accept.

Language is the keyword.

### Natural languages vs. programming languages

A language is a means (and a tool) for expressing and recording thoughts. there are many languages all around us. Some of them require neither speaking nor writing, such as body language; it's possible to express yor deepest feelings very precisely without saying a word.
Another language you use each day is your mother tongue, which you use to manifest your will and to ponder reality. Computers have their own language too, called machine language, which is very rudimentary.
A computer, even the most technically sophisticated, is devoid of even a trace of intelligence. You could say it is like a well-trained dog - it responds only to a predetermined set of known commands.
The commands it recognizes are very simple. We can imagine that the computer responds to orders like "take that number, divide by another and save the result".
A complete set of known commands is called an *'Instruction List'*, sometimes abbreviated to 'IL'. Different types of computers may vary depending on the size of their ILs, and the instructions could be completely different in different models.
No computer is currently capable of creating a new language. However, that may change soon. Just as people use a number of very different languages, machines have many different languages too. The difference, though, is that human  languages developed naturally.
moreover, they are still evolving, and new words are created every day as old words disappear. These languages are called 'natural languages'.

→ Note: Machine languages are develop by humans.

### What makes a language?

We can say that each language (machine or natural, it doesn't matter) consists fo the following elements:

  - _an alphabet_: a set of symbols used to build words of a certain language (e.g. the Latin alphabet for English, the Cyrillic alphabet for Russian, Kanji for Japanese, and so on.);
  - _a lexis_: (aka dictionary) a set of words the language offers its users (e.g., the word "computer" comes from the English language dictionary, while "cmoptrue" doesn't; the word "chat" is present both in english and French dictionaries, but their meanings are different);
  - _a syntax_: a set of rules (formal or informal, written or felt intuitively) used to determine if a certain string of words forms a valid sentence (e.g., 'I am a python' is a syntactically correct phrase, while 'I a python am' doesn't);
  - _semantics_: a set of rules determining if a certain phrase makes sense (e.g, "I ate a doughnut" makes sense, but "A doughnut ate me" doesn't)

The IL is, in fact, _the alphabet of a machine language_. This is the simplest and most primary set of symbols we can use to give commands. It's the computer's mother tongue.
Unfortunately, this tongue is a far cry from human mother tongue. We all (both computers and humans) need something else, a common language for computers and humans, or a bridge between the two different worlds.
We need a language in which humans can write their programs and a language that computers may use to execute the programs, one that is far more complex than machine language and yet far simpler than natural language.
Such languages are often called high-level programming language. They are at least somewhat similar to natural ones in that they use symbols, words and conventions readable to humans. These languages enable humans to express commands to computers that are much more complex than those offered by ILs.
A program written in a high-level programming language is called a _source code_ (in contrast to the machine code executed by computers). Similarly, the file containing the source code is called the _source file_.

### Compilation vs. interpretation

Computer programming is the act of composing the selected programming language's elements in the order that will cause the desired effect. The effect could be different in every specific case - it's up to the programmer's imagination, knowledge and experience.
Of course, such a composition has to be correct in many senses:
  
  - _alphabetically_: a program needs to be written in a recognizable script, such as Roman, Cyrillic, etc;
  - _lexically_: each programming language has it dictionary and you need to master it; thankfully, it's much simpler and smaller than the dictionary of any natural language;
  - _syntactically_: each language has its rules and they must be obeyed;
  - _semantically_: the program has to make sense.

Unfortunately, a programmer can also make mistakes with each of the above four senses. Each of then can cause the program to become completely useless.

Let's assume that you've successfully written a program. How do we persuade the computer to execute it? You have to render your program into machine language. Luckily, the translation can be done by a computer itself, making the whole process fast and efficient.
There are two different ways of _transforming a program from a high-level programming language into machine language_:

  - *COMPILATION*: the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing the machine code: now you can distribute the file worldwide; the program that performs this translation is called a compiler os translator;
  - *INTERPRETATION*: you (or any user of the code) can translate the source program each time it has to be run; the program performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed; it also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

  Due to some very fundamental reasons, a particular high-level programming language is designed to fall into one of these two categories.
  There are very few languages that can be both compiled and interpreted. Usually, a programming language is projected with this factor in its constructors'minds - will it be compiled or interpreted?

  

## Basic Python

### Python Sintax

