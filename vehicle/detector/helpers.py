from django.core.mail import send_mail
import uuid 
from django.conf import settings 

def forgot_mail(email):
    token = str(uuid.uuid4())
    subject = 'your forgot password link temprary'
    message = f'Hi, click on link to reset your password http://127.0.0.1:8000/reset.html/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [sailauthority31@gmail.com] 
    send_mail(subject, message, email_from, recipient_list)
    return True