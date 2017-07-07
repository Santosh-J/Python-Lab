# list of dictionary values in the course _marks
course_marks = [
    {'course': 'python', 'last exam': 90, 'current exam': 80},
    {'course': 'ase', 'last exam': 100, 'current exam': 90},
    {'course': 'na1', 'last exam': 80, 'current exam': 80},
]
# creation of function called average
def average(list):
    for d in list:   # use of for loop
        a1=d.pop('last exam')  # use of pop function
        a2=d.pop('current exam') # use of pop function
        d['last exam + current exam']= (a1+a2)/2 # average
    return list

print(average(course_marks))  # printing the average.

