from django.shortcuts import render
from .forms import UserForms

# Create your views here.

def index(request):
    return render(request, 'index.html', )


def register(request):
    if request.method != 'POST':
        form = UserForms()
    else:
            form = UserForms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'success.html', )

    context = {
        "form" : form
    }
    return render(request, 'register.html', context)