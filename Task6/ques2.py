students =['Smit', 'Jaya', 'Rayyan']
subjects=['CSE', 'Networking', 'Operating System']
dict(zip(students,subjects))

res = {}
for keys in students:
    for value in subjects:
        res[keys] = value
        subjects.remove(value)
        break
print("Result:"+str(res))

# using dictionary comprehension
students =['Smit', 'Jaya', 'Rayyan']
subjects=['CSE', 'Networking', 'Operating System']

data_dict = {key:value for (key,value) in zip(students,subjects)}
print("Result:" + str(data_dict))