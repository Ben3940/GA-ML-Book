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

## Chapter 2

This chapter focused on creating a **decision tree**, based on **information gain** from splitting the data on specific **features**. In the paper bag dataset there are only two features, x and y. There is also a _label_ indicating if this (x, y) coordinate is _inside_ or _outside_ the paper bag. Therefore, the decision tree constructed for this problem is fairly small but still gives an idea of how a decision tree can be created from splits based on features. The reader is guided through the underlying mathematics to compute **entropy**, the extent to which a dataset is _homogeneous_. Entropy ranges in value from 0 (purely homogeneous dataset) to 1 (purely heterogeneous). Information gain uses the baseline entropy of the dataset, the entropy without the dataset split by a feature, and the entropy of the dataset, after splitting on a particular feature. If the entropy of the dataset drops significantly after splitting on a feature, then we gain a lot of information (higher information gain) to more accurately categorize the dataset based on that feature. In other words, by splitting the dataset into different groups, based on a particular feature, the entropy (chaos/randomness) of the dataset decreases, and similar data points (based on this feature) will be within the same group. The book takes a _greedy approach_, in that, it considers all features and selects the split with the greatest information gain (largest entropy drop). This might not always provide the optimal solution, as there might be a better split, later towards the end, if we pick a few sub-optimal splits first.

#### Challenges/Insight:

I never knew that it was possible to define a _function_ within a _function_ in Python. At first this seems unintuitive and meaningless to do. However, researching into it more, it provides a way to control program _scope_ and _encapsulation_ by making a function, that only pertains to a specific part of the code, available to only that specific part. This is just the same as defining _local variables_, except with functions instead of variables.
