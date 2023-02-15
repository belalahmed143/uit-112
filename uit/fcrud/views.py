from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def student_list(request):
    students = StudentData.objects.all()
    context = {
        'students':students
    }
    return render(request, 'fcrud/student.html', context)


def student_details(request, roll):
    student = StudentData.objects.get(roll=roll)
    context = {
        'student':student
    }
    return render(request, 'fcrud/details.html', context)

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('student-add')
    else:
        form = StudentForm()

    return render(request, 'fcrud/add.html', {'form':form})

def student_edit(request,roll):
    student = StudentData.objects.get(roll=roll)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return  redirect('student-list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'fcrud/edit.html', {'form':form})


def student_delete(request, roll):
    student = StudentData.objects.get(roll=roll)
    student.delete()
    return  redirect('student-list')
    


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class StudentListView(ListView):
    model = StudentData
    template_name = 'CBcrud/list.html'
    context_object_name = 'students'
    ordering = ['?']
    # paginate_by = 2

class StudentDetailView(DetailView):
    model = StudentData

class StudentCreateView(CreateView):
    model = StudentData
    fields = '__all__'
    template_name = 'CBcrud/create.html'
    success_url = reverse_lazy('list')


class StudentUpdateView(UpdateView):
    model = StudentData
    fields = '__all__'
    template_name = 'CBcrud/update.html'
    success_url = reverse_lazy('list')


class StudentDeleteView(DeleteView):
    model = StudentData
    template_name = 'CBcrud/delete.html'
    success_url = reverse_lazy('list')

    


    

    
