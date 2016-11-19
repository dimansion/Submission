from django import forms
from .models import Submission, Package

class SubmissionForm(forms.ModelForm):
	class Meta:
		model = Submission
		fields = (
			'fk',
			'name',
		)

class PackageForm(forms.ModelForm):
	class Meta:
		model = Package
		fields = (
			'fk_form',
			'fk_submission',
			'name',
			'key',
		)		