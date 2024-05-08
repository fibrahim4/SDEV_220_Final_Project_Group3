from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Inventory
from .inventory_input import InventoryInput
from django.shortcuts import redirect


# Create your views here.
#this adds a inventory list function the defer to the post list html page. we respond to a request, send to the browser
def inventory_list(request):
    Inventorys = Inventory.objects.filter(status='In Stock')
    return render(request, 'blog/inventory_list.html', {'Inventorys': Inventorys})

def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    return render(request, 'blog/inventory_detail.html', {'inventory' :inventory})

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


def inventory_order(request):
    Inventorys = Inventory.objects.filter(status='In Stock')
    return render(request, 'blog/inventory_order.html', {'Inventorys': Inventorys})

