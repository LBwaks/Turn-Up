from venues.models import Category
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import VenueForm,VenueEditForm,CommentForm
from .models import Venue,Commenting
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class VenueListView(ListView):
    
       model = Venue
       paginate_by = 6
       template_name = 'venues/venues.html'
       ordering ='-created_date'
       queryset =Venue.objects.filter(event_start_date__gte=datetime.datetime.now())

class VenueDetailView(DetailView):
    model = Venue 
    template_name = 'venues/venue_details.html'

    def get_objects(self,**kwargs):
        obj = super().get_object()
        obj.venue_view +=1
        obj.save()
        return obj 
    def get_related_venue_by_tags(self):
        return Venue.objects.filter(category_slug=self.category_slug).exclude(slug=self.slug)      
        


    def get_context_data(self,*args ,**kwargs):
        context= super(VenueDetailView,self).get_context_data(**kwargs)
        
        # for like unlike
        venue_to_like = get_object_or_404(Venue,slug=self.kwargs['slug'])
        total_likes = venue_to_like.total_likes()
        liked=False
        if venue_to_like.likes.filter(id=self.request.user.id):
         liked =True

        #  for commenting
        # get commenting form
        venue_to_comment = get_object_or_404(Venue,slug=self.kwargs['slug'])
        form= CommentForm()
        comments = Commenting.objects.filter(venue=venue_to_comment).order_by('-created_date')


        context['total_likes']=total_likes
        context['liked']=liked
        context['form']=form
        context['comments']=comments
        context['venue_to_comment']=venue_to_comment
        return context

    @method_decorator(login_required)     
    def post(self,request,slug,**kwargs):
        venue= get_object_or_404(Venue,slug=slug)
        new_comment = None
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment= form.save(commit=False)
            new_comment.user = request.user
            new_comment.venue=venue
            new_comment.save()

        comments=Commenting.objects.filter(venue=venue).order_by('-created_date')
        context={'venue':venue,'form':form,'comments':comments,}
        return render(request,'venues/venue_details.html',context)

def CategoryView(request,slug):
    category_venue=get_object_or_404(Category,slug=slug)
    venues=Venue.objects.filter(category=category_venue,event_start_date__gte=datetime.datetime.now())
    page=request.GET.get('page',1)
    paginator =Paginator(venues,4)
    try:
        venues=paginator.page(page)
    except PageNotAnInteger:
        venues=paginator.page(1)
    except EmptyPage:
        venues=paginator.page(paginator.num_pages)
    return render(request,'category/venue_category.html',{'slug':slug,'venues':venues,'category_venue':category_venue})

def UserView(request,username):
    venue_user=get_object_or_404(User,username=username)
    venues=Venue.objects.filter(user=venue_user,event_start_date__gte=datetime.datetime.now()).order_by('-created_date')
    page=request.GET.get('page',1)
    paginator =Paginator(venues,4)
    try:
        venues=paginator.page(page)
    except PageNotAnInteger:
        venues=paginator.page(1)
    except EmptyPage:
        venues=paginator.page(paginator.num_pages)
    return render(request,'users/user_venue.html',{'username':username,'venue_user':venue_user,'venues':venues})
class AddVenueView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Venue
    template_name = 'venues/add_venue.html'
    form_class = VenueForm 
    success_message = 'Venue Event successfully added !'

    def form_valid(self,form):
        venue = form.save(commit=False)
        form.instance.user = self.request.user
        venue.save()
        form.save_m2m
        return super().form_valid(form)


def LikeView(request,slug):
    venue= get_object_or_404(Venue,slug=request.POST.get('venue_slug'))
    liked =False
    if venue.likes.filter(id=request.user.id).exists():
        venue.likes.remove(request.user)

    else:
        venue.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('venue_details',args=[str(slug)]))



class VenueUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model= Venue
    template_name = 'venues/update_venue.html'
    form_class = VenueEditForm
    success_message = 'Venue Event successfully Editted!'

class VenueDeleteView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model= Venue
    template_name = 'venues/delete_venue.html'
    success_url = reverse_lazy('venues')
    success_message = 'Venue Event successfully deleted !'