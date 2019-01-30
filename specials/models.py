from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateField(default=timezone.now)
	image = models.ImageField(upload_to='images', blank=True, null=True)
	author = models.ForeignKey(users.User, on_delete=models.CASCADE)
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url

	def __str__(self):
		return self.title