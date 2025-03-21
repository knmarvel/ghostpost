from django.db import models


# Create your models here.
class GhostPost(models.Model):
    boast: models.BooleanField()
    text = models.CharField(max_length=200)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    public_url = models.CharField(max_length=30)
    private_url = models.CharField(max_length=6)

    def __str__(self):
        return self.text
    
    def score(self):
        return self.upvotes - self.downvotes
