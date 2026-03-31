from django.shortcuts import render

def track_status(request):
    return render(request, 'service_desk/status.html')