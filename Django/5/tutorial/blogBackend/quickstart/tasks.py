from celery import shared_task
import time
from django.core.mail import send_mail

@shared_task
def simulate_fast_task(name):
    time.sleep(1)
    print(f"Task done for {name}")
    return f"Hello, {name}"

@shared_task
def simulate_medium_task(name):
    time.sleep(3)
    print(f"Task done for {name}")
    return f"Hello, {name}"

@shared_task
def simulate_slow_task(name):
    time.sleep(5)
    print(f"Task done for {name}")
    return f"Hello, {name}!"


@shared_task
def send_welcome_email(email, name):
    subject = "Welcome to the Platform!"
    message = f"Hi {name},\n\nThanks for joining our platform. We're excited to have you!"
    from_email = "kritim10kafle@gmail.com"  # Use DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)