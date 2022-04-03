from django.shortcuts import render

# Create your views here.
def home(request):
    jobs="job1 summary"
    return render(request, "home.html", {"jobs": jobs})