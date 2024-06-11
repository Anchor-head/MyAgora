from django.db import models

class DebateUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class SpeechHistory(models.Model):
    user = models.OneToOneField(DebateUser, on_delete=models.CASCADE)
    content = models.JSONField(default=list)

    def __str__(self):
        return f"SpeechHistory for {self.user.username}"
