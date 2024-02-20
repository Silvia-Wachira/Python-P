# users = [
#     {'id':12323, 'displayName': 'Joe Smith', 'email': 'joe.smith@here.com'},
#     {'id':22312, 'displayName': 'Bob Smith', 'email': 'bob.smith@here.com'},
#     {'id':37373, 'displayName': 'angel chen', 'email': 'angel.cheng@here.com'},

# ]
# # print(users)

# def sorter(user):
#     return user['displayName'].lower()

# users.sort(key=sorter)
# print(users)

# reverseUsers = sorted(users, key=sorter, reverse=True)
# print(reverseUsers)

# titles1 = ['Mr', 'Mrs', 'Ms']
# titles2 = ['Mr', 'Mrs', 'Ms', '']
# titles3 = []

# print(all(titles1))
# print(all(titles2))
# print(all(titles3))

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

# squares = []
# for i in range(10):
#     squares.append(i**2)

# print(squares)

# squares = map(lambda x: x**2, range(10))

# print(list(squares))

# squares = [i**2 for i in range (10)]
# print(list(squares))

# sentence = 'the rocket came back from mars'
# vowels = [c for c in sentence if c in 'aeiou']

# print(vowels)

# sentence = 'Mary, Mary, quite contrary, how does your garden grow'
# def is_constant(letter):
#     vowels = "aeiou"
#     return letter.isalpha() and letter.lower() not in vowels

# consonants = [i for i in sentence if is_constant(i)]
# print(consonants)

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# prices = [i if i > 0 else 0 for i in original_prices]
# print(prices)