from __future__ import unicode_literals
from django.db import models


class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        # first_name check
        if len(postData['name']) < 5:
            errors['name'] = 'name has to be more than 5 character'
        if len(postData['desc']) < 15:
            errors['desc'] = 'descriptio has to be more than 15 chars'
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    
    def repr(self):
        return "<Course objects: {}, {}, {}>".format(self.name, self.desc, self.created_at)
    