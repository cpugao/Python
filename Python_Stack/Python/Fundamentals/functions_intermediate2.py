x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

def newVal(xVal):
    x[1][0] = 10
    return xVal
x = newVal([[5,2,3], [10,8,9]])
print(x)

#2. Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]['last_name'] = 'Bryant'
print(students)

#3. In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#4. Change the value 20 in z to 30

z[0]['y'] = 30
print(z)

#5. Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops 
#through each dictionary in the list and prints each key and the associated value. For example, given the following list:

studentsA = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

def iterateDictionary(some_list):
    for item in some_list:
        for key in item:
            print(key, '-', item[key])
iterateDictionary(studentsA)

#6. Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
#the function prints the value stored in that key for each dictionary. 
#For example, iterateDictionary2('first_name', students) should output:
#Michael
#John
#Mark
#KB

def iterateDictionary2(key, some_list):
    for item in some_list:
         print(item[key])
iterateDictionary2('first_name', studentsA)
iterateDictionary2('last_name', studentsA )


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#printInfo(dojo)

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]))
        for item in some_dict[key]:
            print(item)
printInfo(dojo)


 


