from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount


@receiver(user_signed_up)
def populate_user_profile(request, user, **kwargs):
    social_account = SocialAccount.objects.filter(
        user=user, provider='google').first()
    if social_account:
        data = social_account.extra_data
        user.first_name = data.get('given_name', '')
        user.last_name = data.get('family_name', '')
        user.email = data.get('email', user.email)
        user.save()
