# EX1: Convert two lists into a dictionary.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
nums_dict = {}

for i, val in enumerate(keys): 
    nums_dict[val] = values[i]
print(nums_dict)

#EX2: Merge two Python dictionaries into one.
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

for key, val in dict2.items():
    dict1[key] = val
print(dict1)

#EX3: Print the value of key 'history' from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])
