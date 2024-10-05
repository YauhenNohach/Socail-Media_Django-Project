from accounts.models import Notification, Post
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Post)
def notify_followers(sender, instance, created, **kwargs):
    if created:
        followers = instance.user.followers.all()
        for follower in followers:
            Notification.objects.create(
                user=follower, message=f"{instance.user} new post."
            )
