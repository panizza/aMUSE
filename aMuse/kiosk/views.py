from django.shortcuts import render


def home(request):
    """Show home page
    """
    return render(request, 'kiosk/index.html')
