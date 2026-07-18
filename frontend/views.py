from django.shortcuts import render

def welcome_page_baby(request):
    return render(request, "frontend/welcome-page.html")

