from django.shortcuts import render, redirect

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")

def opensource(request):
    return render(request, "opensource.html")

def legal(request):
    return redirect("/legal/terms")