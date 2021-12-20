"""This example shows all necessary steps for sending a basic plain text message."""

# Import the MailSender class from the sendmail module
from sendmail import MailSender
import json
from create_couples import  create_couples

# Opening JSON file
f = open('name_mail.json')
dict_name_mail = json.load(f)  # retrieve json as dict_mail
f.close()

# the list of friends are just the keys of the dictionary
list_of_friends_sender = list(dict_name_mail.keys())
list_of_friends_receiver = list_of_friends_sender.copy()  # the receivers are the same group of the senders

# SET THE SENDER MAIL ADDRESS AND THE PASSWORD
mail_sender = "giornogiovanna@gmail.com"
password = 'Gold_Experience'

for who_buy_the_gift,who_receive_the_gift in create_couples(dict_name_mail):
    plaintext = "Hi %s, \n" \
                "i am your secret santa manager. You must do a pretty present to %s taking into account that you have 10 euro as budget. \n" % (
                who_buy_the_gift, who_receive_the_gift)

    print(plaintext)

    # UNCOMMENT THE FOLLOWING LINES TO SEND THE MAILS
    # ourmailsender = MailSender(mail_sender,password, ("smtp.gmail.com", 587)) #default is gmail
    # ourmailsender.set_message(plaintext, "Message from secret santa")
    # ourmailsender.set_recipients([dict_name_mail[who_buy_the_gift]])
    # ourmailsender.connect()
    # ourmailsender.send_all()
