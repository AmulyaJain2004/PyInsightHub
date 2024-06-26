from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver  # Import the receiver decorator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.db.models.signals import post_save  # Import the post_save signal


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Only send the welcome email if a new user is created
        subject = 'Welcome to Our Website!'
        message = render_to_string('welcome_email.html', {
            'user': instance,
        })
        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email])
