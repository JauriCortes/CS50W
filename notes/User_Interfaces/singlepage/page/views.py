import time
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/posts.html")

texts = ["Text1","Text 2","Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")

def scroll(request):
    return render(request, "singlepage/index.html")

def posts(request):
    
    #get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1) :
        data.append(f"Post #{i}")
    
    # Artificial delay
    time.sleep(1)

    # Return list of spots
    return JsonResponse({
        "posts": data
    })

