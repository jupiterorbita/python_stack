from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from bcrypt import checkpw
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        # FIRST NAME
        if len(postData['name']) < 1:
            errors['name'] = 'name cannot be empty'
        elif len(postData['name']) < 3:
            errors['name'] = 'name must be 3+ chars'
        # LAST NAME
        if len(postData['alias']) < 1:
            errors['alias'] = 'alias cannot be empty'
        elif len(postData['alias']) < 3:
            errors['alias'] = 'alias must be 3+ chars'
        # EMAIL
        if len(postData['email']) < 1:
            errors['email'] = 'EMAIL cannot be empty'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'EMAIL NOT valid'
        # if email exists in DB
        if User.objects.filter(email=postData['email']):
            errors['email'] = 'EMAIL already exists!!!'
        # PASSWORD
        if len(postData['password']) < 1:
            errors['password'] = 'Password cannot be BLANK!'
        elif len(postData['password']) < 3:
            errors['password'] = '@@@@@@ PW has to be AT LEAST 3 chars!'
        if postData['password'] != postData['password_confirm']:
            errors['password'] = 'Pws do not match!'
        return errors

    def login_validator(self, postData):
        errors = {}
        # check if email is valid
        if len(postData['email']) < 1:
            errors['email'] = 'EMAIL cannot be empty'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'EMAIL NOT valid'
        # check if email exists in DB
        if len(User.objects.filter(email=postData['email'])) < 1:
            errors['email'] = "EMAIL doesn't match (doesnt exist in db)!!"
        else:  # if email exists contiue to password check
            user_check = User.objects.filter(email=postData['email'])
            if len(postData['password']) < 1:
                errors['password'] = 'password cannot be empty'
            elif not checkpw(postData['password'].encode(), user_check[0].password.encode()):
                errors['password'] = 'pass doesnt match'
        return errors


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = 'Title must be filled in'
        if len(postData['author']) < 1:
            errors['author'] = 'Author cannot be blank'
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['review']) < 1:
            errors["review"] = "REVIEW MUST EXIST"
        if len(postData['rating']) < 1:
            errors["rating"] = "MUST GIVE RATING"
        return errors




class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=255)
    objects = UserManager()
    def repr(self):
        return "<User objects: {}, {}, {}>".format(self.name, self.alias, self.email)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=255)
    creator = models.ForeignKey(User, related_name='created_books')
    objects = BookManager()
    def repr(self):
        return "<User objects: {}, {}, {}, {}>".format(self.title, self.author)


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews')
    user = models.ForeignKey(User, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=255)
    objects = ReviewManager()
    def repr(self):
        return "<User objects: {}, {}, {}, {}>".format(self.review, self.rating, self.book, self.user)