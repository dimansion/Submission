from django.db import models
from django.utils import timezone

class Submission(models.Model):
    fk = models.IntegerField()
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.fk)


class Package(models.Model):
	fk_form = models.IntegerField()
	fk_submission = models.IntegerField()
	name = models.CharField(max_length=100)
	key = models.ForeignKey(Submission)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name



