from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blogsite.Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

