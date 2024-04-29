from django.shortcuts import render

# Create your views here.
#this adds a inventory list function the defer to the post list html page. we respond to a request, send to the browser
def inventory_list(request):
    return render(request, 'blog/inventory_list.html', {})