# Assignment: Functions Intermediate II
# Write the following function.

# Part I (essential)
# Given the following list:

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

students = [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]


def dictfunction():

    for i in range(len(students)):
        print(i+1,' - ',students[i]['first_name'], students[i]['last_name'], ' - ', ((len(students[i]['first_name']))+(len(students[i]['last_name']))))

dictfunction()
