from multiprocessing import parent_process
from urllib.request import Request

from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory #modelform for querysets
from django.urls import reverse
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Scratch
from customers.models import Customer, Contact
from .forms import WorkorderForm
from .forms import WorkorderDynamicForm

# Create your views here.

##Attempt at HTMX Dropdown
def customer(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'scratch/customform.html', context)

#def customer(request):
#    form = WorkorderDynamicForm()
#    context = {'form': form}
#    return render(request, 'scratch/dynamiccustomer.html', context)

#def contacts(request):
#    form = WorkorderDynamicForm(request.GET)
#    print(form['contact'])
#    return HttpResponse(form['contact'])

#@login_required
def workorder_create_view(request):
    form = WorkorderForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Redirect": obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers)
        return redirect(obj.get_absolute_url())
    return render(request, "scratch/add-update.html", context)

def custom_workorder_create(request):
    #print(request.POST)
    context = {}
    if request.method == "POST":
        customer = request.POST.get("customer")
        contact = request.POST.get("contact")
        workorder = request.POST.get("workorder")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        budget = request.POST.get("budget")
        quoted_price = request.POST.get("quoted_price")
        Scratch.objects.create(customer=customer, contact=contact, workorder=workorder, description=description, deadline=deadline, budget=budget, quoted_price=quoted_price)
        context['workorder'] = workorder #return workorder number to form
        context['created'] = True
    return render(request, "scratch/customform.html", context=context)
