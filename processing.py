users = [
    {'id':12323, 'displayName': 'Joe Smith', 'email': 'joe.smith@here.com'},
    {'id':22312, 'displayName': 'Bob Smith', 'email': 'bob.smith@here.com'},
    {'id':37373, 'displayName': 'angel chen', 'email': 'angel.cheng@here.com'},

]
# print(users)

def sorter(user):
    return user['displayName'].lower()

users.sort(key=sorter)
print(users)

reverseUsers = sorted(users, key=sorter, reverse=True)
print(reverseUsers)

titles1 = ['Mr', 'Mrs', 'Ms']
titles2 = ['Mr', 'Mrs', 'Ms', '']
titles3 = []

print(all(titles1))
print(all(titles2))
print(all(titles3))

# feedBack1 = ['', '', '']
# feedBack2 = ['So Much Fun', '', '']
# feedBack3 = []

# print(any(feedBack1), feedBack1)
# print(any(feedBack2), feedBack2)
# print(any(feedBack3), feedBack3)

# scores = (90, 86, 75, 91, 62, 99, 88, 90)
# print(scores)

# def isA(num):
#     return num >= 90

# aScores = filter(isA, scores)
# print(aScores)
# print(list(aScores))

# def getGrade(num):
#     if (num >= 90):
#         return "A"
#     elif (num < 90 and num >= 80):
#         return "B"
#     elif (num < 80 and num >= 70):
#         return "C"
#     elif (num < 70 and num >= 60):
#         return "D"
#     else:
#         return "F"

# grades = list(map(getGrade, scores))
# print(list(grades))

# print("ZIPPED GRADES ABD SCORES")
# combined = list(zip(scores, grades))
# print(combined)