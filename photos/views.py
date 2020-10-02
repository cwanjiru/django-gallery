from django.shortcuts import render
from .models import Image
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def homepage(request):
    all_images=Image.objects.all()
    paginator=Paginator(all_images,6)
    page=request.GET.get("page")
    
    try:
        all_images=paginator.page(page)

    except PageNotAnInteger:
        all_images=paginator.page(1)
    
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse("")
        all_images=paginator.page(paginator.num_pages)
    if request.is_ajax():
        
        return render(request,"images/list_ajax.html",{"all_images":all_images})   
    return render(request, "homepage.html",{"all_images":all_images})


def search_results(request):
    if "category" in request.GET and request.GET.get("category"):
        search_term=request.GET.get("category")
        found_images=Image.search_image(search_term)
        paginator=Paginator(found_images,6)
        page=request.GET.get("page")

        try:
            found_images=paginator.page(page)

        except PageNotAnInteger:
            found_images=paginator.page(1)

        except EmptyPage:
            if request.is_ajax():
                return HttpResponse("")

            found_images=paginator.page(paginator.num_pages)

        if request.is_ajax():
            return render(request,"images/list_ajax.html",{"all_images":found_images})   

        return render(request,"search_results.html",{"all_images":found_images})

    else:
        message="You havent Searched for any term try again"
        return render(request,"search_results.html",{"message":message})
