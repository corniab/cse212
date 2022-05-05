# Week 03 Notes

> It is not easy to convey, unless one has experienced it, the dramatic feeling of sudden enlightenment that floods the mind when the right idea finally clicks into place. One immediately sees how many previously puzzling facts are neatly explained by the new hypothesis. One could kick oneself for not having the idea earlier, it now seems so obvious. Yet before, everything was in a fog.”
> ― Francis Crick, What Mad Pursuit[^1]

## Stacks

Stacks are really good for "remembering" where we have been. They maintain a history of the current execution context. You could use a stack to undo commands that you have performed.

Debuggers also use stacks to trace the current execution context.

```python
# An example of a simple stack.
stack = []

stack.append('item1')
stack.append('item2')
print(stack)
# expected output: ['item1', 'item2']

stack.pop()
print(stack)
# expected output: ['item1']

stack.pop()
print(stack)
# expected output: []
```

## Code Reviews

If I got in the pilot's seat of an airplane (assuming I am not a pilot), I would have little idea of how it actually works. I might work the main controls and see how they move the flaps. I could turn on the engine and maybe even try to take off. There is a good chance I will die in a fiery inferno.

If I take the time to understand how each part of the plane influences it as a whole then I stand a much better chance of surviving. The same is true of code reviews.

I start a code review by forming a hypothesis of what I think the code should be doing. As I continue to review, I can revise my hypothesis. The clash of expectations and reality will generate a complete mental model of the program.

### Tooling

- use structure charts for diagramming multiple function calls
- use UML to diagram class relationships
- use flow charts to diagram behavior of a single function or algorithm
- execute the code manually on paper
- analyze the use of data structures

### Teach Assignment

This week's team assignment[^2], proved very difficult for me. Partially, because I was feeling rushed and partially because there were new techniques. Let me explain.

```python
def do_something_complicated(line):
	stack = []
	for item in line:
		if item == '(' or item == '[' or item == '{':
			stack.append(item)
		elif item == ')':
			if len(stack) == 0 or stack.pop() != '(':
				return False
		elif item == ']':
			if len(stack) == 0 or stack.pop() != '[':
				return False
		elif item == '}':
			if len(stack) == 0 or stack.pop() != '{':
				return False
	return len(stack) == 0
```

What threw me off is the 'stack.pop()' in the if statements. It didn't make sense to me to remove the item until after the statement was evaluated. It also didn't make sense to me what order everything was being removed. This is how it works.

```python
# Add all opening brackets to the stack
# Ignore all other characters
# If we encounter a closing bracket
# And the stack is empty then return false
# Or remove the last value of the stack
# And if it is not a matching bracket to the removed value
# Then return False
# If all of our brackets have a pair then the stack should be 0 in size then return True
# If the stack is not empty then there are missing matches and we will return False
```

On a high level, the function returns true if there is a matching pair of brackets. It returns false otherwise. It is actually a really clever algorithm.

## Definitions

- back: refers to the location in a stack where a push and pop occurs. The last item put into the stack is found in the back.
- flow charts: a diagram that models the behavior of a program, algorithm, or funciton. Actions are shown in boxes, decisions shown in diamonds, and arrows are used to show execution flow
- front: refers to the location in a stack where the first item added to the stack can be found. Traditionally, this is index 0 of a dynamic array
- pop: removes the last item pushed to the stack. the item from the back of the stack is removed and returned
- push: the operation to add a new item onto the stack. the item is placed at the back of the stack
- review: a formal process of ensuring code is written correctly. code is reviewed against the design and coding standards. frequently, checklists are used to help the reveiwer
- stack: a data structure that follows a last in, first out rule. the stack is used to reverse data or remember previous data including previous results
- structure chart: a diagram showing which functions call which functions. Frequently, the arrows used to show function calls also include parameters that are passed between the functions
- UML: Unified Modeling Language. A formal modelling language to represent object-oriented designs. UML includes many types of diagrams including class diagrams, activity diagrams, and state diagrams.

### Footnotes

[^1]: [goodreads](https://www.goodreads.com/quotes/tag/hypothesis)
[^2]: [teach assignment](https://byui-cse.github.io/cse212-course/lesson03/03-teach.html)
