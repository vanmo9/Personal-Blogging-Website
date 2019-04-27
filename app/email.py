from flask_mail import Message
from flask import render_template
from . import mail


# create sender_email where we store our email address.
# We then create a mail_message function that takes in 4 parameters which are the subject of the email, the template which is where we create the message body, We pass in the template without an extension because we need to create the text version and a HTML version, the recipient and any keyword arguments.
def mail_message(subject,template,to,**kwargs):
    sender_email = "vanmowha@gmail.com"


    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.txt = render_template(template + ".html",**kwargs)
    mail.send(email) 