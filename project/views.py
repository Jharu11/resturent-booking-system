from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from project.forms import UpdateUser, ReservationForm, LoginForm, RegisterForm, ChangePWD
from django.contrib import messages

from project.models import User, Reservation




def Profile(request):
    form = UpdateUser(instance=request.user)
    if request.method=='POST':
        form= UpdateUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            print('none')
    context ={'form':form}
    return render(request, 'super/Profile.html',context )

def Loginuser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.info(request, 'Check credentials.')
    return render(request, 'auth/login.html')


def LogoutView(request):
    logout(request)
    return redirect('Loginuser')

def AddReservation(request):
    form = ReservationForm()
    if request.method =='POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Place Reservation.')

    context = {'form':form}
    return render(request, 'super/new_reserve.html', context)

def UpdateReservation(request, pk):
    resev = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=resev)
    if request.method =='POST':
        form = ReservationForm(request.POST, instance=resev)
        if form.is_valid():
            form.save()
            messages.info(request, 'Place Reservation.')

    context = {'form':form}
    return render(request, 'super/update_reserve.html', context)


def dashboard(request):
    """Admin dashboard view."""
    reservations = Reservation.objects.all()
    users = User.objects.all()
    pending = Reservation.objects.filter(status="pending")
    confirmed = Reservation.objects.filter(status="confirmed")
    return render(request, "super/dashboard.html",
                  {'users': users,
                   'reservations': reservations,
                   'pending': pending, 'confirmed': confirmed})


# class AddReservation(LoginRequiredMixin, CreateView):
#     """Admin user add new reservation."""
#     template_name = "super/new_reserve.html"
#     form_class = ReservationForm
#     login_url = '/login/'

#     def form_valid(self, form):
#         new = form.save(commit=False)
#         new.save()
#         # send a flash message to the user
#         messages.success(
#             self.request,
#             "you have successfully added a new table reservation ")
#         # redirect the user back to his/her dashboard
#         return redirect("/dashboard")


# class UpdateReservation(LoginRequiredMixin, UpdateView):
#     """Admin user updates all the reservation."""
#     form_class = ReservationForm
#     template_name = "super/update_reserve.html"
#     model = Reservation

#     def get_object(self, *args, **kwargs):
#         obj = get_object_or_404(Reservation, pk=self.kwargs['pk'])
#         return obj

#     def form_valid(self, form):
#         form.save()
#         messages.success(
#             self.request, "you have successfully updated the reservation")
#         return redirect('/dashboard')



def view_reservations(request):
    """Admin user view all the reservations."""
    reservations = Reservation.objects.all()
    return render(request,"super/view_reserve.html",{'reservations': reservations})
