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