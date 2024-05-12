# Genetic Algorithms and Machine Learning

## Description

This project will track my progress through the book _"Genetic Algorithms and Machine Learning for Programmers"_ by _Frances Buontempo_. The link to the accompanying website for the book:

    https://pragprog.com/titles/fbmach/genetic-algorithms-and-machine-learning-for-programmers/

The book is structured as having a problem to solve for each chapter. The main goal is for a turtle to escape a "paper bag" that is rendered on screen. The reader will be using techniques with machine learning and especially genetic algorithms to create efficient solutions to solve this problem.

This project will be structured quite differently than any other project on my GitHub. Each chapter will be given a section in this README, with a description/summary, insights gained, personal challenges (because even following along with a book involves troubleshooting), and any other thoughts I have for the chapter.

## Chapter 1

This chapter focused on familiarizing the reader with **Turtle graphics** in Python. This chapter takes a _brute force_ approach to getting out of the bag. By having the turtle move in a square path, turning and moving forward in larger and larger steps until it escapes the bag. Then the same idea is used but instead of a fixed 90 degree turn after each forward step, the turtle will turn at some constant, abritrary angle, creating a _spirangle_ until it escapes.

#### Challenges/Insight:

There were no challenges associated with this setup chaper. I was not aware of the built-in **turtle** and **argparse** modules for Python. I found the **argeparse** package very practical as it simplifies the process of setting up user interaction with the Python script using the _CLI_.
