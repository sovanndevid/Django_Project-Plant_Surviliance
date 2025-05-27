from django.contrib.auth.signals import user_logged_in
from django.contrib import messages
from django.dispatch import receiver

@receiver(user_logged_in)
def welcome_message(sender, user, request, **kwargs):
    messages.success(request, f"Welcome back, {user.username}!")
