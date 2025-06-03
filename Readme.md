# Python Practice Assessment - Module 2

## Purpose
This assessment is designed to help you practice and solidify your understanding of intermediate Python concepts, with a focus on structured problem-solving and Test-Driven Development (TDD) principles. You will implement functions in `assessment.py`, and your solutions will be verified using `test_assessment.py`.

## Learning Outcomes Assessed
This assessment focuses on:
- Understanding and implementing **Functions** with clear inputs and outputs.
- Using **Loops (1D and 2D)** effectively for iteration and data processing (e.g., over lists and lists of lists).
- Applying **Control Flow Statements** (if, elif, else, nested conditions) to direct program logic.
- Working with **Data Structures** (primarily lists, including lists of lists/matrices, and dictionaries for intermediate results).
- Demonstrating **Problem-solving skills** by designing and implementing algorithms for given tasks.
- Performing **String Manipulation** (e.g. parsing, cleaning, transforming strings).
- Practicing **Test-Driven Development (TDD)** by writing code to pass pre-defined unit tests.

## Files
- `assessment.py`: This is the file you need to edit. It contains function stubs that you must complete according to their docstrings.
- `test_assessment.py`: This file contains unit tests to check if your functions in `assessment_module2.py` work correctly. **Do not modify this file.** Your goal is to make all tests in this file pass.
- `README.md`: This file, providing instructions.

## Instructions: Practicing TDD

1. **Fork the Repository:**
   - Create a personal copy of the repository on your GitHub account by forking it.
   - 
2. **Understand the Goal (Read the Test First):**
    *   Open `test_assessment_module2.py`. Look at a test case for a function you are about to implement (e.g., `test_generate_fibonacci_sequence`). See what inputs are given and what output is `assertEqual`ed. This helps you understand the requirements from a testing perspective.
    *   Run the tests *before* writing any code for a function: `python -m unittest test_assessment_module2.py`. You will see that test fail – this is expected! This is the "Red" step in Red-Green-Refactor.

3. **Implement the Function (Write Code - Green):**
    *   Open `assessment_module2.py`. Read the docstring for the function you are working on.
    *   Write the minimum amount of code in `assessment_module2.py` to make the failing test (and related tests for that function) pass.
    *   Run the tests again: `python -m unittest test_assessment_module2.py`.
    *   If the test passes, you are in the "Green" step.

4. **Refactor (Improve Code - Refactor):**
    *   (Optional but good practice) Once the test passes, look at your code. Can it be made cleaner, more efficient, or more readable without changing its functionality (i.e., without breaking the test)? This is the "Refactor" step. After refactoring, run tests again to ensure you haven't broken anything.

5. **Repeat:**
    *   Move to the next function or the next failing test and repeat the cycle.

6.**Interpret Test Results:**
    *   **OK:** All tests pass.
    *   **FAILURES/ERRORS:** `unittest` will detail which tests failed and why. Use this feedback to debug your functions in `assessment_module2.py`.

Good luck with your assessment! Remember, the goal is to practice and improve your Python skills through structured problem-solving and TDD principles. If you have any questions, feel free to ask for help or clarification.