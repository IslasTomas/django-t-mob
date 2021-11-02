from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

class Redirect(models.Model):
    key = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.key, self.url)

    @classmethod
    def get_redirect_instance(cls,key):
        try:
            instance = Redirect.objects.get(key=key)
            return {"key": instance.key, "url": instance.url}
        except Redirect.DoesNotExist:
            return None

    @classmethod
    def get_redirect(cls,key):
        redirect=cache.get(key)
        if redirect is not None:
            return {"key": redirect.key, "url": redirect.url}
        return Redirect.get_redirect_instance(key)


@receiver(post_save, sender=Redirect)
def take_instances_with_cache(sender, instance, **kwars):
    query = Redirect.objects.filter(active=True)
    for redirect in query:
        cache.set(redirect.key,redirect)
