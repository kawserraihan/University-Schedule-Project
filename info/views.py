from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from .forms import ClassDetailsForm
from django.http import JsonResponse
from django.core.paginator import Paginator



User = get_user_model()

# Create your views here.


@login_required
def index(request):
    if request.user.is_teacher:
        return render(request, 'info/dashboard.html')
    if request.user.is_superuser:
        return render(request, 'info/dashboard.html')
    return render(request, 'authentication/logout.html')

# Teacher Views



@login_required
def dashboard(request, teacher_id):
    # Retrieve the teacher object based on the teacher_id
    teacher = get_object_or_404(Teacher, id=teacher_id)
    

    # Pass the total_students variable to the template context
    context = {
        'teacher': teacher
    }
    
    # You can include any additional data or context you want to pass to the template
    
    return render(request, 'info/dashboard.html',context)

@login_required
def classes(request, teacher_id):
    # You can retrieve the data for the table from your database here
    # For now, let's create a sample data list for demonstration
    class_details = ClassDetails.objects.all()
    items_per_page = 10  # Change this to your desired value

    # Create a Paginator instance
    paginator = Paginator(class_details, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    context = {
        'class_details': class_details,
        'page_obj': page_obj
    }
    return render(request, "info/classes.html", context)
    
@login_required
def add_class(request, teacher_id):
    departments = Dept.objects.all()
    batches = Batch.objects.all()
    sections = Section.objects.all()
    
    
    if request.method == 'POST':
        form = ClassDetailsForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            return redirect('classes', teacher_id=teacher_id)
    else:
        form = ClassDetailsForm()
    
    context = {'form': form, 'departments': departments, 'batches': batches, 'sections':sections, 'days_of_week': DAYS_OF_WEEK}
    return render(request, 'info/add_class_form.html', context)


def get_batches(request):
    department_id = request.GET.get('department_id')
    batches = Batch.objects.filter(department_id=department_id)
    batch_options = '<option value="">Select a batch</option>'
    for batch in batches:
        batch_options += f'<option value="{batch.id}">{batch.name}</option>'
    return JsonResponse(batch_options, safe=False)

def get_sections(request):
    batch_id = request.GET.get('batch_id')
    sections = Section.objects.filter(batch_id=batch_id)
    section_options = '<option value="">Select a section</option>'
    for section in sections:
        section_options += f'<option value="{section.id}">{section.name}</option>'
    return JsonResponse(section_options, safe=False)


@login_required
def view_class(request, teacher_id, class_id):
    class_instance = get_object_or_404(ClassDetails, id=class_id)
    context = {'class_instance': class_instance}
    return render(request, 'info/view_class.html', context)

@login_required
def edit_class(request, teacher_id, class_id):
    class_data = get_object_or_404(ClassDetails, id=class_id)

    if request.method == 'POST':
        form = ClassDetailsForm(request.POST, instance=class_data)
        if form.is_valid():
            form.save()
            return redirect('view_class', teacher_id=teacher_id, class_id=class_id)
    else:
        form = ClassDetailsForm(instance=class_data)

    return render(request, 'info/edit_class.html', {'form': form})

@login_required
def delete_class(request, teacher_id, class_id):
    class_instance = get_object_or_404(ClassDetails, id=class_id)
    
    if request.method == 'POST':
        class_instance.delete()
        return redirect('classes', teacher_id=teacher_id)
    
    context = {'class_id': class_id}
    return render(request, 'info/delete_class.html', context)

