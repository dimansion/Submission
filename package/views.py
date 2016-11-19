from django.shortcuts import render, redirect
from .models import Submission, Package
from .forms import PackageForm, SubmissionForm

def list_sub(request):
	subs = Submission.objects.all()
	packages = Package.objects.all()
	if request.method == "POST":
		form = PackageForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
		return redirect('/')
	else:
		form = PackageForm()
	context = {
		'sub': subs,
		'packages': packages,
		'form' : form,
	}
	return render(request, 'package/list.html', context)

def create_sub(request):
	if request.method == "POST":
		form = SubmissionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
		return redirect('/')
	else:
		form = SubmissionForm()
	context = {
		'form' : form,
	}
	return render(request, 'package/add_sub.html', context)	