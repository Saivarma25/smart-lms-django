from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor')
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def is_student(self) -> bool:
        return self.role == 'student'

    def is_instructor(self) -> bool:
        return self.role == 'instructor'





