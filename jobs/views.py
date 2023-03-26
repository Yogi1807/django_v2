from django.shortcuts import render


# Create your views here.
def welcome(request):

    cricketers = ["virat", "dhoni", "Rohit", "sachin"]

    return render(
        request,
        "jobs/welcome.html",
        {"message": "Good morning", "cricketers": cricketers}
    )