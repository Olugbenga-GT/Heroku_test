from django.shortcuts import render
from .forms import PostForm

# Create your views here.

def post(request):
    return  render(request, 'postpage.html', )

def create_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'posted.html', )

    context = {
        "form" : form
    }
    return render(request, 'createPost.html', context)