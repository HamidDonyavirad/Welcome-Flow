from celery import shared_task, chain
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import EmailStatus


User = get_user_model()


def send_email_html (subject,template_name,context,to_email,user_id,email_type):
    html_content = render_to_string(template_name,context)
    msg = EmailMultiAlternatives(subject=subject,body=html_content,to=[to_email])
    msg.attach_alternative(html_content,'text/html')
    
    try:
        msg.send()
        EmailStatus.objects.create(user_id=user_id, email_type=email_type, success=True)
    except Exception as e:
        EmailStatus.objects.create(user_id=user_id, email_type=email_type, success=False, error_message=str(e))



@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    send_email_html(
        subject='Welcome',
        template_name='welcome_email.html',
        context={'username': user.username},
        to_email=user.email,
        user_id=user.id,
        email_type='welcome'
    )
    return user_id


@shared_task
def send_profile_completion_email(user_id):
    user = User.objects.get(id=user_id)
    send_email_html(
        subject='Complete the profile',
        template_name='profile_completion_email.html',
        context={'username': user.username},
        to_email=user.email,
        user_id=user.id,
        email_type='profile_completion'
    )
    return user_id   

@shared_task
def send_reminder_email(user_id):
    user = User.objects.get(id=user_id)
    send_email_html(
        subject='Login reminder',
        template_name='reminder_email.html',
        context={'username': user.username},
        to_email=user.email,
        user_id=user.id,
        email_type='reminder'
    )             

@shared_task    
def schedule_welcome_emails(user_id):
    chain(
        send_welcome_email.s(user_id).set(countdown=5),
        send_profile_completion_email.s().set(countdown=10),
        send_reminder_email.s().set(countdown=15)
    )()    