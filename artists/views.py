# from django.shortcuts import render  
from django.http.response import JsonResponse
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView ,CreateView,ListView,UpdateView,DeleteView
from .forms import ArtistForm ,ArtistEditForm, ArtistSearchForm,CommentForm,ArtistSearchForm
from .models import Artist,Comment
from django.contrib.auth.models import User
from artists.models import Category
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.db.models import F
from django.contrib.messages.views import SuccessMessageMixin 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.loader import render_to_string
from django.http import HttpResponse
import datetime
from django.db.models import Q
# Create your views here.
class ArtistView(ListView):
    paginate_by = 4
    model= Artist
    template_name ='artists/artists.html'
    ordering =['-created_date']     
    # queryset = Artist.objects.filter(event_start_date__gte=datetime.datetime.today())
    # def get_context_data(self, **kwargs):
    #       context =super(ArtistView,self).get_context_data(**kwargs)
    #       context['artist']=Artist.objects.filter(event_start_date__gte=datetime.datetime.today())          
    #       return context

    # def get_queryset(self):       
    #     queryset  = super().get_queryset()        
    #     queryset.filter(event_start_date__gte=datetime.datetime.now())
    #     return queryset
    
class ArtistDetailView(DetailView):
    model = Artist
    template_name ='artists/artist_details.html'


# for counting number of vistor to that page
    def get_object(self,**kwargs):
        obj = super().get_object()
        obj.artist_view +=1
        obj.save()
        return obj 

# end for counting number of vistor to that page

# for getting reletaed artist by tags

    def get_related_artist_by_tags(self):
       return Artist.objects.filter(category_slug=self.category_slug).exclude(slug=self.slug) 

# end for getting reletaed artist by tags
    
    def  get_context_data(self, *args, **kwargs):
     context = super(ArtistDetailView,self).get_context_data(**kwargs)
  
# for like unlike
     artists_to_like=get_object_or_404(Artist, slug=self.kwargs['slug'])     
     total_likes = artists_to_like.total_likes()
     liked=False
     if artists_to_like.likes.filter(id=self.request.user.id).exists():
         liked=True
     context['artists_to_like']=artists_to_like
    
# for getting  commenting form
    
     artist_to_comment = get_object_or_404(Artist, slug=self.kwargs['slug'])
     form = CommentForm()
     comments = Comment.objects.filter( artist = artist_to_comment).order_by('created_date')
     context["total_likes"] =total_likes
     context["liked"] =liked
     context['form']= form
    #  context['artist_to_like']=artists_to_like
     context['artist_to_comment'] = artist_to_comment
     context['comments']= comments
     return context

# for posting commenting data
    @method_decorator(login_required)
    def post(self,request,slug ,**kwargs):
    #  context = super(ArtistDetailView,self).get_context_data(**kwargs)
     artist = get_object_or_404(Artist, slug=slug)
     new_comment =None
     form = CommentForm(request.POST or None )
     parent_comment = request.POST.get('comment_id')

     if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.artist = artist
            new_comment.parent=parent_comment
            new_comment.save()        

     
        
     comments = Comment.objects.filter(artist=artist).order_by('created_date')

     context={'artist': artist,'form': form,'comments': comments  ,}   
     return render (request,'artists/artist_details.html',context)

    

def CategoryView(request,slug):
    category_artists = get_object_or_404(Category, slug=slug)
    artists=Artist.objects.filter(category=category_artists,event_start_date__gte=datetime.datetime.today()).order_by('-created_date')
    page=request.GET.get('page',1)
    paginator =Paginator(artists,6)
    try:
        artists=paginator.page(page)
    except PageNotAnInteger:
        artists=paginator.page(1)
    except EmptyPage:
        artists=paginator.page(paginator.num_pages)

    return render(request,'category/artist_category.html',{"slug":slug,'artists':artists,'category_artists':category_artists})



def UserView(request,username):
    artist_user=get_object_or_404(User,username=username)
    artists=Artist.objects.filter(user=artist_user,event_start_date__gte=datetime.datetime.today()).order_by('-created_date')
    page=request.GET.get('page',1)
    paginator =Paginator(artists,4)
    try:
        artists=paginator.page(page)
    except PageNotAnInteger:
        artists=paginator.page(1)
    except EmptyPage:
        artists=paginator.page(paginator.num_pages)
    return render(request,'users/user_artist.html', {'username':username,'artists':artists,'artist_user':artist_user})

class AddArtistView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/add_artists.html'
    success_message = 'Artist Event successfully added !'
   
    

    def form_valid(self, form):
       artist = form.save(commit=False)   
       form.instance.user = self.request.user
       artist.save()
       form.save_m2m()
       return super().form_valid(form)
    # fields ='__all__'

class UpdateArtistView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Artist
    form_class =ArtistEditForm
    template_name = 'artists/update_artists.html'
    success_message = 'Artist Event Successfully Edited!'
    
    

class DeleteArtistView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Artist 
    template_name = 'artists/delete_artists.html'
    success_url = reverse_lazy('artists')

# def artist_search(request):
#     if request.method == 'GET':
#         q =request.GET['q']
#         artists=Artist.objects.filter(artist_name__icontains=q)
#         return render(request,'pages/search.html',{'q':q,'artists':artists})

#     else:
   
#      return render(request,'pages/search.html')
# class Search(ListView):
#     model = Artist
#     context_object_name = "artists  "
#     template_name = "pages/search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Artist.objects.filter(
#             Q(artist_name__icontains=query) | Q(event_name__icontains=query)
#         )
#         from django.contrib.postgres.search import SearchVector
#  results=Books.objects.annotate(search=SearchVector('title','authors'),).filter(search=q)
@login_required
def LikeView(request):
    artist =get_object_or_404(Artist,id=request.POST.get("artist_id"))
    liked=False
    if artist.likes.filter(id=request.user.id).exists():
        artist.likes.remove(request.user)
        liked=False
    else:

       artist.likes.add(request.user)
       liked=True
    context={
        'artist':artist,
        'liked':liked,
        'total_likes':artist.total_likes(),
    }
    if request.is_ajax():
        html =render_to_string('artists/like_section.html',context,request=request)
        return JsonResponse({'form':html})

    url = artist.get_absolute_url()
    return HttpResponseRedirect(url)
    # return HttpResponseRedirect(reverse('artist_detail',args=[str(slug)]) )

   
    