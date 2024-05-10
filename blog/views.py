from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Inventory
from .inventory_input import InventoryInput
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
#this adds a inventory list function the defer to the post list html page. we respond to a request, send to the browser
@login_required
def inventory_list(request):
    Inventorys = Inventory.objects.all()
    return render(request, 'blog/inventory_list.html', {'Inventorys': Inventorys})

def inventory_shop(request):
    Inventorys = Inventory.objects.filter(status='In Stock')
    return render(request, 'blog/inventory_shop.html', {'Inventorys': Inventorys})

@login_required
def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    return render(request, 'blog/inventory_detail.html', {'inventory' :inventory})

@login_required
def inventory_new(request):
    if request.method == "POST":
        form = InventoryInput(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.user = request.user
            inventory.save()
            return redirect('inventory_detail', pk=inventory.pk)
    else:
        form = InventoryInput()
    return render(request, 'blog/inventory_edit.html', {'form': form})

@login_required
def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryInput(request.POST, instance=inventory)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.user = request.user
            inventory.save()
            return redirect('inventory_detail', pk=inventory.pk)
    else:
        form = InventoryInput(instance=inventory)
    return render(request, 'blog/inventory_edit.html', {'form': form})



@login_required
def inventory_remove(request, pk):
    invenotry = get_object_or_404(Inventory, pk=pk)
    invenotry.delete()
    return redirect('inventory_list')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')      
        fname = request.POST.get('fname')
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "Your Account has been successfully created.")
        
        return redirect('inventory_shop')

    return render(request, "registration/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passs1 = request.POST['pass1']
        
        user = authenticate(username=username, password=passs1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('inventory_shop')
            
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('inventory_shop')
        
    return render(request, "registration/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('inventory_shop')

