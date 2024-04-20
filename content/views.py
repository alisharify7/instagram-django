from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm

@login_required()
def index(request):
    ctx = {
        "form": AddPostForm()
    }
    return render(request,  'content/index.html', context=ctx)
