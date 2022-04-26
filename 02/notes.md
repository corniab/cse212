# Week 2 Notes

## Big O Notation

Big O notation is used to describe the performance of an algorithm (or function) for large datasets. It considers the amount of time it takes for an algorithm to execute based on the size of its input.

## Linear Time

- usually a single line of code like an assignment

## Constant Time

- typically one or more loops in serial
- or a nested loop where one of the loops is not dependent on input size

```python
# This is considered O(n) because the inner loop is not
# controlled by the outer.
n = 1000
for i in range(0, n):
	for j in range(0, 3)
```

## Logarithmic Time

```python
# This is considered O(log n) because the input size is split each loop.
def search(self, nums: List[int], target: int) -> int:
	low = 0
	high = len(nums)

	while low <= high:
		mid = (high + low) // 2		# The input size is divided.

		if nums[mid] < x:
			low = mid + 1
		elif nums[mid] > x:
			high = mid - 1
		else:
			return mid

	return -1
```

## Polynomial Time

```python
## Two nested loops controlled by input size.
n = 1000
for i in range(0, n):
	for j in range(0, n):
		print(i, j)
```

## Key Terms

1. algorithm: a solution to a problem including the steps to solve the problem. An algorithm is implemented as one or more functions in code.
2. benchmark: the measurement of actual execution time of an algorithm as observed in multiple executions of the algorithm. Benchmarks are often taken within different environments (e.g. operating system, processor, programming language).
3. big O: a way to represent the performance of an algorithm mathematically. Written as a function in terms of n, where n represents the input size.
4. coefficient: the number placed before the variable. The coefficient is dropped in Big O.
5. constant: an algorithm has constant time if it is not dependent on the size of data. Constant time is always reduced to O(1).
6. linear: execution time increases at the same rate as input size. O(n)
7. logarithmic: execution time decreases as the size of the data increases. O(log n)
8. performance: describes the amount of time and memory used to perform an algorithm in software.
9. polynomial: execution time increase by a fixed exponent relative to size of the data.
