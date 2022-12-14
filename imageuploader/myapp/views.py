from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import Image,BlogPost
from django.views.generic import DetailView
#
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        photo = request.POST.get('photo')
        check = Image.objects.filter(photo=photo).first()
       
        if form.is_valid():
            form.cleaned_data['photo']
            form.save()
            return redirect("/home")
    form = ImageForm()
    img = Image.objects.all()

    return render(request,'myapp/home.html',{'img':img,'form':form})
#
def BlogPostLike(request, pk):
    post = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail',args=[str(pk)]))

class BlogPotsDetailView(DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data




