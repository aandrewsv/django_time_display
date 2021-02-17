from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    return redirect("/time_display")

def time_display(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        "date": datetime.now().strftime("%b %d, %G"),
        "time": datetime.now().strftime("%H:%M %p")
    }
    return render(request, "time_display.html", context)