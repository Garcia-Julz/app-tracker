from apptrackerapp.models import Position
from apptrackerapp.models import Applicant
from django.shortcuts import render, reverse, redirect

def home(request):
    """View function for home page.  Will show user info and jobs applied for"""

    user = Applicant.objects.filter(id=request.user.applicant.user_id)
    positions = Position.objects.filter(user_id=user.id)

    context = {
        'positions': positions
    }

    return render(request, 'home.html', context=context)