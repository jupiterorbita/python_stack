from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        # first_name check
        if len(postData['first_name']) < 1:
            errors['full_name'] = 'Full name should be at least 3 characters'
        elif len(postData['first_name']) < 3:
            errors['full_name'] = 'Full name should be at least 3 characters'
        # Last name
        if len(postData['last_name']) < 1:
            errors['last_name'] = 'LAST name should be at least 3 characters'
        elif len(postData['last_name']) < 3:
            errors['last_name'] = 'LAST name should be at least 3 characters'
        # email check
        if len(postData['email']) < 1:
            errors['email'] = 'email cannot be empty'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'email NOT valid'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def repr(self):
        return "<User objects: {}, {}, {}, {}>".format(self.first_name, self.last_name, self.email, self.created_at)
    
