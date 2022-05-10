# Week 04 Notes - Queues

Queues are used when we need to process a collection of requests in a fair and orderly way.
They

```python
from typing import List

class Queue(List):
	def __init__(self):
		super().__init__(self)
		self = []
	def enqueue(self, val):
		self.append(val)
	def dequeue(self):
		return self.pop(0)

web_server_queue = Queue()

request1 = "request1"
request2 = "request2"
request3 = "request3"

web_server_queue.enqueue(request1)
web_server_queue.enqueue(request2)
web_server_queue.enqueue(request3)

print(web_server_queue.dequeue())
print(web_server_queue.dequeue())
print(web_server_queue.dequeue())
```

Use assertions to build test cases

```python
def is_leap_year(year: int):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False


assert is_leap_year(1996) == True
assert is_leap_year(1900) == False
assert is_leap_year(2000) == True
assert is_leap_year(2003) == False
```

## Definitions

- back: Refers to the location in the queue where an enqueue occurs. The last item put in the queue is found in the back.
- defect: This is an error in code
- dequeue: The operation to remove an item from the queue. The item is removed from the front of the queue.
- enqueue: The operation to add an item to the queue. The item is added to the back of the queue.
- expected result: The result that you expect to receive when you run a test case. The expected result is based on your understanding of the software requirements.
- front: Refers to the location in the queue where a dequeue occurs. The first item put in the queue is found in the front. Traditionally this is index 0 of a dynamic array.
- process: The place where software runs. A process has code that is executed and memory used for variables in that doed. Multiple processes can run at the same time. Processes can share memory
- queue: A data structure that follows a First In, First Out (FIFO) rule. The queue is used both to maintain order in data and to remember data when there is not time to process it
- requiremetns: Written description of what software should do.
- test cases: Scenarios that are written to test that code behaves per the requirements. A test case will usually have test code unless the procedure is for the user to interact with the software. An expected result is written for each test case.
- testing: An activity to demonstrate that the code correctly implements the requirements.
