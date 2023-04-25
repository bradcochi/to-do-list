from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from projects.forms import ProjectForm

# Create your views here.


@login_required
def list_projects(request):
    project = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": project,
    }
    return render(request, "list_projects.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project=id)
    context = {
        "tasks": tasks,
        "show_project": project,
    }
    return render(request, "project_details.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
        context = {
            "form": form,
        }
    return render(request, "create_project.html", context)
