from django.shortcuts import render

def create_report(request):
    return render(request, 'reports/report_form.html')