from django.db import models


class UserManager(models.Manager):
    def create_user(self, name, password):
        # You can add more validation or processing here if needed
        user = self.create(name=name, password=password)
        return user


class users(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # Assign the custom manager to the model
    objects = UserManager()

    def __str__(self):
        return self.name
