from django.db import models

# Create your models here.
class Idea(models.Model):
	author = models.ForeignKey('auth.User', related_name='ideas')
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128, blank=True, default='')
	content = models.TextField()

	class Meta:
		ordering = ('created',)