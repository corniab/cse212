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