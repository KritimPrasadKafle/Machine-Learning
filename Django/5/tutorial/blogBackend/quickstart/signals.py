from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from quickstart.tasks import send_welcome_email

User = get_user_model()

@receiver(post_save, sender=User)
def send_email_on_user_creation(sender, instance, created, **kwargs):
    if created and instance.email:
        send_welcome_email.delay(instance.email, instance.name)
