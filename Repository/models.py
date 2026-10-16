from django.db import models

# Create your models here.
class QuestionsDb(models.Model):
    title = models.CharField(max_length=200)
    LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
    ]

    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES,default='Python')

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES, default='Easy')

    topic= models.CharField(max_length=200)
    notes = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    sample_input = models.TextField()
    sample_output = models.TextField()
    is_active = models.BooleanField(default=True)
    score = models.IntegerField()
    

    