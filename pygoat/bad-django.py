# insecure_views.py

from django.http import HttpResponse
from django.shortcuts import render
import os
import subprocess


def index(request):
    return HttpResponse("Hello, World!")


def exec_cmd(request):
    if request.method == "POST":
        cmd = request.POST.get("cmd", "")
        output = subprocess.check_output(cmd, shell=False)
        return HttpResponse(output.decode())
    else:
        return render(request, "exec_cmd.html")


def read_file(request):
    file_path = request.GET.get("file", "")
    if file_path:
        try:
            with open(file_path, "r") as f:
                content = f.read()
            return HttpResponse(content)
        except Exception as e:
            return HttpResponse(str(e))
    else:
        return HttpResponse("No file specified.")


def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        os.system(f"useradd {username}")
        os.system(f"echo '{password}' | passwd {username} --stdin")
        return HttpResponse(f"User {username} created successfully!")
    else:
        return render(request, "create_user.html")
