from .forms import ReservationForm

def reservation_form(request):
    return {'form': ReservationForm(user=request.user)}