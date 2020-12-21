from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

tasks = []

class NewTaskForm(forms.Form):
	Task = forms.CharField(label="New Task")
	#priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


def index(request):
	if "tasks" not in request.session:
		request.session["tasks"] = []
	return render(request, "Tasks/index.html", {
		"tasks": request.session["tasks"]
		})

def add(request):
	if request.method == "POST":
		form = NewTaskForm(request.POST)
		if form.is_valid():
			task = form.cleaned_data["task"]
			#Tasks.append(Task)
			request.session["tasks"] += [task]
			return HttpResponseRedirect(reverse("tasks:index"))
		else:
			return render(request, "Tasks/add.html", {
				"form": form
				})

	return render(request, "Tasks/add.html", {
		"form": NewTaskForm
		})
