from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from .forms import ClassDetailsForm, BusScheduleForm
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
def classes(request, teacher_id, department_id=None, batch_id=None, section_id=None):
    # Get the day filter from the request GET parameters
    day_filter = request.GET.get('day')

    # Initialize a queryset to filter ClassDetails based on the provided parameters
    class_details = ClassDetails.objects.all()
    form = ClassDetailsForm()
    

    # Filter by department_id, batch_id, and section_id if provided
    if department_id & batch_id & section_id is not None:
        class_details = class_details.filter(department_id=department_id,batch_id=batch_id,section_id=section_id)
    
    

    if day_filter:
        class_details = class_details.filter(department_id=department_id,
        batch_id=batch_id,
        section_id=section_id,
        day=day_filter)

    items_per_page = 10  # Change this to your desired value
    

    # Create a Paginator instance
    paginator = Paginator(class_details, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    context = {
        'class_details': page_obj,  # Use page_obj instead of class_details for pagination
        'page_obj': page_obj,
        'teacher_id': teacher_id,  # Pass teacher_id to the template if needed
        'departmentId': department_id,  # Pass department_id to the template if needed
        'batchId': batch_id,  # Pass batch_id to the template if needed
        'sectionId': section_id,  # Pass section_id to the template if needed
        'form':form,
        'DAYS_OF_WEEK': DAYS_OF_WEEK
    }
    return render(request, "info/classes.html", context)


def all_class_details(request, teacher_id):

    day_filter = request.GET.get('day')
    all_class_details = ClassDetails.objects.all()
    form = ClassDetailsForm()

    if day_filter:
        all_class_details= all_class_details.filter(day=day_filter)

    context = {
        'class_details': all_class_details,
        'form':form,
        'DAYS_OF_WEEK': DAYS_OF_WEEK,
        'teacher_id':teacher_id
    }
    return render(request, "info/classes.html", context)


def bus_day(request):
    day_objects = BusDay.objects.all()

    context = {
        'day_objects': day_objects
    }
        
    return render(request, 'bus/buses.html', context)


def busschedule(request, routetype, busday_id):
    # Determine the routetype_id based on the string captured in the URL
    if routetype== "uproute":
        routetype_id = 1
    elif routetype == "downroute":
        routetype_id = 2
    else:
        routetype_id = 0
        # Handle other cases or provide a default value
        routetype_id = 0  # You can change this to an appropriate default value

    # Get the BusDay object based on the busday_id
    bus_day = get_object_or_404(BusDay, pk=busday_id)

    # Get the Route object based on the determined routetype_id
    route = get_object_or_404(Route, pk=routetype_id)

    # Filter BusSchedule objects based on the selected BusDay and Route
    schedules = BusSchedule.objects.filter(day=bus_day, route_type=route)

    context = {
        'schedules': schedules,
        'busday_id': busday_id,
        'routetype_id': routetype_id,
        'routetype': routetype
    }

    return render(request, "bus/busschedule.html", context)

def add_busschedule(request, routetype, busday_id):
    # Get the BusDay object based on the busday_id
    bus_day = get_object_or_404(BusDay, pk=busday_id)
    
    # Initialize route_type with a default value
    if routetype == "uproute":
        route_type = get_object_or_404(Route, route_type="uproute")
    elif routetype == "downroute":
        route_type = get_object_or_404(Route, route_type="downroute")
    else:
        # Provide a default value for unknown cases
        route_type = get_object_or_404(Route, route_type="default_value")# Provide a default value for unknown cases
    
    if request.method == 'POST':
        form = BusScheduleForm(request.POST)
        if form.is_valid():
            # Automatically determine the route_type based on the routetype
           # routetype = form.cleaned_data['route_type']  # Assuming you have a field named 'route_type' in your form

            # Save the BusSchedule instance with the selected BusDay and route_type
            busschedule = form.save(commit=False)
            busschedule.day = bus_day
            busschedule.route_type = route_type  # Set the route_type
            busschedule.save()
            
            return redirect('busschedule', routetype=routetype, busday_id=busday_id)
    else:
        # Initialize the form with the selected day
        form = BusScheduleForm(initial={'day': bus_day.id})
    
    # Get all available BusDay objects for the dropdown
    days = BusDay.objects.all()

    context = {
        'form': form,
        'bus_day': bus_day,
        'days': days,
        'route_type': route_type
    }

    return render(request, "bus/add_bus.html", context)

def view_busschedule(request, routetype, busday_id, busschedule_id):
    # Determine the route_id based on the route type
    route_id = 1 if routetype == 'uproute' else 2
    
    # Get the BusSchedule object based on the busschedule_id
    busschedule = get_object_or_404(BusSchedule, pk=busschedule_id)
    
    # Now, filter the data based on route_id and day
    filtered_busschedules = BusSchedule.objects.filter(
        route_type=route_id,
        day=busday_id
    )
    
    context = {
        'busschedule': busschedule,
        'filtered_busschedules': filtered_busschedules,
        'day': busday_id,
        'route_type': routetype
    }
    
    
    return render(request, "bus/view_busschedule.html", context)

def edit_busschedule(request, busschedule_id):
    # Get the BusSchedule object based on the busschedule_id
    busschedule = get_object_or_404(BusSchedule, pk=busschedule_id)

    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = BusScheduleForm(request.POST, instance=busschedule)
        if form.is_valid():
            form.save()
            return redirect('view_busschedule', routetype=busschedule.route_type, busday_id=busschedule.day.id, busschedule_id=busschedule.id)
    else:
        # If it's a GET request, pre-fill the form with existing data
        form = BusScheduleForm(instance=busschedule)

    context = {
        'form': form,
        'busschedule': busschedule,
    }

    return render(request, 'bus/edit_busschedule.html', context)

def delete_busschedule(request, busschedule_id):
    busschedule = get_object_or_404(BusSchedule, id = busschedule_id)
    if request.method == 'POST':
        #schedule = get_object_or_404(BusSchedule, pk=busschedule_id)
        busschedule.delete()
        
        # Get the routetype and busday_id
        routetype = busschedule.route_type.route_type  # Replace with the actual way to get routetype
        busday_id = busschedule.day.id
        
        # Construct the URL for redirection using the 'reverse' function
        redirect_url = reverse('busschedule', kwargs={'routetype': routetype, 'busday_id': busday_id})
        
        return HttpResponseRedirect(redirect_url)
    
    else:
        return redirect('uproute')

    # Handle cases where the request is not a POST request
    return redirect('uproute')


@login_required
def add_class(request, teacher_id, department_id, batch_id, section_id):
    try:
        # Retrieve the selected department, batch, and section based on URL parameters
        selected_department = get_object_or_404(Dept, id=department_id)
        selected_batch = get_object_or_404(Batch, id=batch_id)
        selected_section = get_object_or_404(Section, id=section_id)

        if request.method == 'POST':
            form = ClassDetailsForm(request.POST)
            if form.is_valid():
                # Create the class instance but don't save it yet
                class_instance = form.save(commit=False)
                class_instance.department = selected_department
                class_instance.batch = selected_batch
                class_instance.section = selected_section
                class_instance.save()
                return redirect('classes', teacher_id=teacher_id, department_id=department_id, batch_id=batch_id, section_id=section_id)
            else:
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'errors': errors})

        return JsonResponse({'success': False, 'errors': 'Invalid request'})

    except Exception as e:
        return JsonResponse({'success': False, 'errors': str(e)})
    


@login_required
def add_class_without_params(request, teacher_id):
    departments = Dept.objects.all()
    batches = Batch.objects.all()
    sections = Section.objects.all()
    
    
    if request.method == 'POST':
        # Rest of your view code here
        form = ClassDetailsForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            return redirect('all_classes', teacher_id=teacher_id )
        else:
            errors = form.errors
            return JsonResponse({'success': False, 'errors': errors})
    else:
        # Log the request method to help diagnose the issue
        print(f"Received a {request.method} request instead of a POST request.")
        return HttpResponseBadRequest("Invalid Request")


def get_departments(request):
    departments = Dept.objects.all()
    departments_options = '<option value="">Select a Department</option>'
    for depts in departments:
        departments_options += f'<option value="{depts.id}">{depts.name}</option>'
    return JsonResponse(departments_options, safe=False)

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
        return redirect('all_classes', teacher_id=teacher_id)
    
    context = {'class_id': class_id}
    return render(request, 'info/delete_class.html', context)

