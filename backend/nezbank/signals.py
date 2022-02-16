from nezbank.models import User
from django.db.models import signals
from django.dispatch import receiver
from .services import send_email_verification


@receiver(signals.pre_save, sender=User)
def email_verification_pre(sender, instance, *args, **kwargs):
    if instance.id and instance.email_status != User.EmailStatus.NOT_VERIFIED:
        old_user = User.objects.get(id=instance.id)
        if old_user.email != instance.email:
            instance.email_status = User.EmailStatus.NOT_VERIFIED
            instance.save()


@receiver(signals.post_save, sender=User)
def email_verification_post(sender, instance, *args, **kwargs):
    if not bool(instance.email_status) or instance.email_status == User.EmailStatus.NOT_VERIFIED:
        instance.email_status = User.EmailStatus.EMAIL_SENT
        instance.save()
        send_email_verification(instance)
