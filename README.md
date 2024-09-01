# OOP Design Exercises

Welcome to **OOP Design Exercises**! This repository was created to address the lack of practical exercises focused on object-oriented programming (OOP) design. Whether you’re preparing for technical interviews or simply looking to sharpen your OOP skills, this repository offers a collection of exercises that will help you apply SOLID principles and coding best practices in real-world scenarios.

## How to Use This Repository

This repository is organized into folders, with each folder containing a separate exercise. Inside each folder, you'll find:

- A description of the exercise and its requirements
- The conditions and constraints to consider
- A reference Python solution with comprehensive unit tests
- A PlantUML file that illustrates the design of the solution

Feel free to browse through the exercises, work on them at your own pace, and compare your solutions with the provided ones. Keep in mind that the solutions are not absolute! You may find some improvements points. 

## Prerequisites

Before diving into these exercises, it’s recommended that you have a solid understanding of:

- Object-Oriented Programming (OOP) theory
- SOLID principles
- Unit testing

These concepts will be crucial as you work through the exercises and aim to develop clean, maintainable, and scalable solutions.

## Why Python?

Even though I usually work with Java, I strongly suggest using Python for these exercises, especially if you are preparing for interviews. Python is easy to use and read, which makes it a great choice for writing clear code quickly. Its flexible and simple syntax lets you focus more on solving the problem and designing your solution instead of worrying about complex code details.

Also, Python’s readability helps interviewers understand your thought process during interviews, which allows you to better show your knowledge of OOP principles.

## File Structure

Considering an 'Example Exercise,' its folder follows the file structure shown below. 

```
oop-design-exercises
└── example
    ├── example.puml
    ├── example.py
    ├── README.md
    └── test_example.py
```
- **example.puml**: PlantUML diagram representing the class relationships and design of the solution
- **example.py**: Python script containing the object-oriented solution for the exercise
- **README.md**: Provides details about the specific example exercise, including the problem statement and explanation
- **test_example.py**: Unit test script to validate the correctness of the solution in `example.py`

## Running Locally

Make sure you have Python3 installed on your machine. You can run the tests by navigating to each folder and executing the following command for the exercise `test_*.py` file.

```commandline
python3 test_example.py
```

To visualize the PlantUML diagrams, you can either install an extension in your preferred code editor or use a PlantUML server on your machine, or an existent one (see the "Online Server" section on the [official website](https://plantuml.com/starting)).
