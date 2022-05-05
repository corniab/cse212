# Week 03 Notes

## Stacks

Stacks are really good for "remembering" where we have been. They maintain a history of the current execution context. You could use a stack to undo commands that you have performed.

Debuggers also use stacks to trace the current execution context.

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
