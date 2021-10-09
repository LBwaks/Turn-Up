from django.urls.base import reverse_lazy ,reverse
from django.views.generic import ListView,DeleteView, DetailView,CreateView,UpdateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EventForm,EditEventForm,CommentForm
from .models import Category, Event , Comment
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from events.models import Category
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class EventView(ListView):
    paginate_by=4
    model = Event 
    template_name = 'events/events.html'
    ordering =['-created_date']
    queryset = Event.objects.filter(event_start_date__gte=datetime.datetime.now())

class EventDetailView(DetailView):
    model = Event
    template_name ='events/event_details.html'

#for counting number of page visitors
    def get_objects(self,**kwargs):
        obj = super().get_objects()
        obj.event_view +=1
        obj.save()
        return obj
   #for getting similar events 
        
    def get_related_event_by_tags(self):
        return Event.objects.filter(category_slug=self.category_slug).exclude(slug=self.slug) 

    def  get_context_data(self, *args, **kwargs):
     context = super(EventDetailView,self).get_context_data(**kwargs)

# # for like unlike
     events_to_like=get_object_or_404(Event, slug=self.kwargs['slug'])     
     total_likes = events_to_like.total_likes()
     liked=False
     if events_to_like.likes.filter(id=self.request.user.id).exists():
         liked=True

# for getting  commenting form
    
     event_to_comment = get_object_or_404(Event, slug=self.kwargs['slug'])
     form = CommentForm()
     comments = Comment.objects.filter( event = event_to_comment).order_by('-created_date')

# # for posting commenting data
     




     context["total_likes"] =total_likes
     context["liked"] =liked
     context['form']= form
     context['event_to_comment'] = event_to_comment
     context['comments']= comments
     return context

    @method_decorator(login_required)
    def post(self,request,slug ,**kwargs):    
        event = get_object_or_404(Event, slug=slug)
        new_comment =None
        form = CommentForm(request.POST)

        if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.event = event
                new_comment.save()        

     
        
        comments = Comment.objects.filter(event=event).order_by('-created_date')

        context={'event': event,'form': form,'comments': comments,}   
        return render (request,'events/event_details.html',context)


def CategoryView(request,slug):
    category_event=get_object_or_404(Category,slug=slug)
    events=Event.objects.filter(category=category_event,event_start_date__gte=datetime.datetime.now()).order_by('-created_date')
   
    page=request.GET.get('page',1)
    paginator =Paginator(events,4)
    try:
        events=paginator.page(page)
    except PageNotAnInteger:
        events=paginator.page(1)
    except EmptyPage:
        events=paginator.page(paginator.num_pages)

    return render(request,'category/event_category.html',{
        
        'slug':slug,'events':events,'category_event':category_event})

def UserView(request,username):
    event_user=get_object_or_404(User,username=username)
    events=Event.objects.filter(user=event_user,event_start_date__gte=datetime.datetime.now()).order_by('-created_date')
    page=request.GET.get('page',1)
    paginator =Paginator(events,4)
    try:
        events=paginator.page(page)
    except PageNotAnInteger:
        events=paginator.page(1)
    except EmptyPage:
        events=paginator.page(paginator.num_pages)

    return render(request,'users/event_user.html',{'username':username,'events':events,'event_user':event_user})
class AddEventView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model =Event
    form_class = EventForm
    template_name = 'events/add_events.html'
    success_message = 'Event successfully added !'

    def form_valid(self, form):
       event = form.save(commit=False)
       form.instance.user = self.request.user
       event.save()
       form.save_m2m()
       return super().form_valid(form)
    # fields ='__all__'

class UpdateEventView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model=Event
    form_class= EditEventForm
    template_name= 'events/update_events.html'
    success_message = 'Event successfully Updated !'

class DeleteEventView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('events')
    success_message = 'Event successfully Deleted!'

@login_required
def LikeView(request,slug):
    event =get_object_or_404(Event,slug=request.POST.get("event_slug"))
    liked=False
    if event.likes.filter(id=request.user.id).exists():
        event.likes.remove(request.user)
        liked=False
    else:

       event.likes.add(request.user)
       liked=True
    return HttpResponseRedirect(reverse('event_details',args=[str(slug)]) )



