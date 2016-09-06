from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Messages(models.Model):
	message_text = models.TextField('Message')
	create_time = models.DateTimeField('Date', auto_now_add=True)