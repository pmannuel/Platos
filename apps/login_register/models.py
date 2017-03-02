from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
      def check_password_match(self, chk_password, correctp):
          return correctp == bcrypt.hashpw(chk_password.encode(), correctp.encode())

      def encrypt(self, password):
          password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

          return password

      def register(self, firstname, lastname, email, password, cpassword):
          EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

          name_l = len(firstname)
          lastname_l = len(lastname)
          email_l = len(email)
          pw_l = len(password)
          cpass_l = len(cpassword)

          error_messages = []
          exists = User.objects.filter(email = email)
          if exists:
              error_messages.append('This email address is already in use, please log in above')
          if name_l < 1 or lastname_l < 1 or email_l < 1 or pw_l < 1 or cpass_l < 1 :
              error_messages.append('All fields are required and must not be blank')
              return error_messages
          if not str.isalpha(str(firstname)) or not str.isalpha(str(lastname)):
              error_messages.append('Invalid name')
          if not EMAIL_REGEX.match(email) :
              error_messages.append('Invalid email address')
          if pw_l < 8 :
              error_messages.append("Password must be more than 8 characters")
              return error_messages
          if password != cpassword:
              error_messages.append("Password do not match")


          return error_messages

class User(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45, default="poopyhead")
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
