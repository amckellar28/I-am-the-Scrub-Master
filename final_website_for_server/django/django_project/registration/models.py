from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, BaseUserManager, PermissionsMixin, Group)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def assign_group(self, email, password, **extra_fields):
    user = self.model(email=email, is_staff=is_staff, is_active=is_active,
                      is_superuser=is_superuser, last_login=now,
                      date_joined=now, Label=label, **extra_fields)
    if is_truck(user) == true:
        g1 = Group.objects.get(name=truck)
        g1.user_set.add(user)
        user_group.save()
 
        return user
    elif user.Label == 'Company':
        g2 = Group.objects.get(name=Company)
        g2.user_set.add(COMPANY_USER)
        user_group.save()

        return user

def is_truck(user):
    return user.groups.filter(name='truck').exists()

def is_company(user):
    return user.groups.filter(name='company').exists()
