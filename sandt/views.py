from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import CreateSandt

# Create your views here.
def sandt_list(request):
    sandts = Sandt.objects.all()
    paginator = Paginator(sandts, 10)
    page = request.GET.get('page')
    paged_sandts = paginator.get_page(page)

    context = {
        "sandts": paged_sandts
    }
    return render(request, "sandt/sandts_list.html", context)



def sandt_regi(request):
    if request.method == "POST":
        forms = CreateSandt(request.POST)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Student and Teacher Registration Successfully!")
        return redirect("sandt_list")
    else:
        forms = CreateSandt()

    context = {
        "forms": forms
    }
    return render(request, "sandt/registration.html", context)



def edit_sandt(request, pk):
    sandt_edit = Sandt.objects.get(id=pk)
    edit_forms = CreateSandt(instance=sandt_edit)

    if request.method == "POST":
        edit_forms = CreateSandt(request.POST, instance=sandt_edit)

        if edit_forms.is_valid():
            edit_forms.save()
            messages.success(request, "Edit Student and Tescher Info Successfully!")
            return redirect("sandt_list")

    context = {
        "edit_forms": edit_forms
    }
    return render(request, "students/edit_student.html", context)



def delete_sandt(request, sandt_id):
    sandt_delete = Sandt.objects.get(id=sandt_id)
    sandt_delete.delete()
    messages.success(request, "Delete Student and Teacher Info Successfully")
    return redirect("student_list")