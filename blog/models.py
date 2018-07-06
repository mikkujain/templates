from django.db import models
from django.utils import timezone
# Create your models here.

 #models.model means the at the post is a django Model, so django Knows that it should be in databse.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# models.CharField – this is how you define text with a limited number of characters.
# models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
# models.DateTimeField – this is a date and time.
# models.ForeignKey – this is a link to another model.        