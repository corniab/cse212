# Week 8 Notes - Recursion

# Rules

1. The problem must have an optimal substructure; meaning the solution can be constructed from optimal solutions of its subproblems. Essentially, the problem is able to be solved by repeatedly solving smaller problems.[See optimal substructure page on Wikipedia.](https://en.wikipedia.org/wiki/Optimal_substructure)
2. You must define a base case when met will end the recursive calls.

3. If your function does not return a value then you do not return the function. For example if you are printing values to the terminal, then you recursively call the function until you meet the base case.

# Examples

## Definitions

- base case: The scenario that will terminate (or stop) the recursive calls. If this is not designed properly, then the recursion will run forever.
- memoization: The technique of remembering previous results found through recursion so that the repetitive recursion can be avoided.
- recursion: The calling of a function with the same function. This can used to solve problems by identifying a solution which is written in terms of solving the same problem using smaller values. A base case is needed to ensure that the recursion eventually stops. The base cases are solved in the function without using recursion.
