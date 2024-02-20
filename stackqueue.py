# teller = []

# teller.append("Greet Customer")
# print(teller)
# teller.pop()
# print(teller)
# teller.append("process deposit")
# print(teller)
# teller.append("phone ringing")
# print(teller)
# teller.pop()
# print(teller)
# teller.append("great caller, listen, answer question")
# print(teller)
# teller.pop()
# print(teller)
# teller.pop()

# processor = []
# processor.append({'type': 'page', 'path': '','header':[],'cookies':[]}),
# processor.append({'type': 'api', 'function':'', 'parameters': []})
# processor.append({'email': 'email', 'address':'bob@gmail.com', 'subject':''})

# print("PROCESSOR LIST", processor)

# for i in range(len(processor)):
#     item = processor.pop(0)
#     print("PROCESSING ITEM", item)
#     print("REMAINING LIST", processor)


# def say_hi(name):
#     print(f 'Hi, {name}!')

# def say_good_morning(name):
#     print(f 'Good morning, {name}!')

# def say_something_to_curtis(say_something_func):
#     return say_something_func('Curtis')

# say_something_to_curtis(say_hi)
# say_something_to_curtis(say_good_morning)

# def say_hi_to(name):
#     def say_from(author):
#         print(f'Hi, {name}!')
#         print(f'This is a message from {author}.')
#     return say_from

# say_hi_ryan_from = say_hi_to('Ryan')
# say_hi_ryan_from('Julia')
# say_hi_ryan_from('Erik')

# print(say_hi_ryan_from.__closure__)
# print(say_hi_ryan_from.__closure__[0].cell_contents)


def message_decorator(message_func):
    def message_wrapper(name):
        from_statement = 'This ia a message from ' + name
        print(message_func() + from_statement)
    return message_wrapper

def say_hi():
    return 'Hi! '

def say_bye():
    return 'Bye !'

say_hi = message_decorator(say_hi)  
print(say_hi) 
