# Stack
>Software engineering is the establishment and use of sound engineering principles in order to obtain economically software that is reliable and works efficiently on real machines. 
― Friedrich L. Bauer

A stack can be thought of as a stack of plates. 

You can only add or remove plates from the top of the stack. 
![stack of plates](../resources/plates.jpg)[^1]

In this example, each plate could be thought of as a function call. When a function is invoked, it is placed on the "call stack". When the function finishes execution, then it is removed from the call stack.

![stack graphical](../resources/stack.jpg)


## Usage
A stack follows the principle of Last In First Out[^2]. This means that the most recent data (last in) is the first to be processed (first out). This makes it useful for several different processes[^3]. 
* Call Stack (which we covered in the previous example)
* Reversing
	
	In this example we use the stack as place to temporarily store each letter of the string. 

  ![reversing a string](../resources/reverse_string.jpg)
* Undo/Redoing
  
	A stack is used to keep track of where we have been in a program, which makes it useful for undoing commands that we have used before.
* Backtracking


 If you have ever used the undo button in a program, then you have probably used a stack. A 

## Time Complexity
Operations in stacks are very efficient because we are only adding and removing from the top of the data structure.


## Example

## Practice Problem
````python

````
You can find the solution [here](solution.py).
### Footnotes

[^1]: Photo by Christopher Flaten: [https://www.pexels.com/photo/a-pile-of-gray-plates-5514789/]
[^2]: Last In First Out, [Geeks for Geeks](https://www.geeksforgeeks.org/lifo-last-in-first-out-approach-in-programming/)
[^3]: Alice Matthews, [The stack data structure — What is it and how is it used in JavaScript?](https://levelup.gitconnected.com/the-stack-data-structure-what-is-it-and-how-is-it-used-in-javascript-23562fb8a590)
[^4]: []()
[^5]: []()