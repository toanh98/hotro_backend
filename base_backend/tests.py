from django.test import TestCase
from .models import UserAccount
class TestModeCreatelUser(TestCase):
    username = 'toanh2'
    first_name = 'to'
    last_name = 'anh'
    account = UserAccount.objects.create(username=username,first_name=first_name,last_name=last_name)
    account.set_password(username)
    account.save()
    