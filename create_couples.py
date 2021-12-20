import random

def create_couples(dict_name_mail):
    list_of_friends_sender = list(dict_name_mail.keys())
    random.shuffle(list_of_friends_sender)
    n = len(list_of_friends_sender)
    list_of_couples = []

    for i in range(0, n):
        list_of_couples.append((list_of_friends_sender[i], list_of_friends_sender[((i + 1) % n)]))

    return list_of_couples