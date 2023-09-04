from django.shortcuts import render

def task_view(request):
    dynamic_data = "This is dynamic data from the view."
    return render(request, 'task.html', {'dynamic_data': dynamic_data})
