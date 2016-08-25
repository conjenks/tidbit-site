from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tidbit(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '%s: %s' % (self.user.username, self.pk)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='images/')
