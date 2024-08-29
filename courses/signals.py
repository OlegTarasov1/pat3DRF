from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course

@receiver(post_save, sender=Course)
def subscriber_add(sender, instance, created, **kwargs):
    if created:
        instance.subscribers.add(instance.creator)        
