from django.shortcuts import render
from .models import Team
from django.views.generic import ListView
from artists.models import Artist
from venues.models import Venue
from events.models import Event
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector ,SearchHeadline
from django.contrib.postgres.search import SearchHeadline, SearchQuery
# Create your views here.

class HomeView(ListView):
    context_object_name ='Home'
    model = Team
    
    template_name = 'pages/home.html'
    # queryset =Artist.objects.all()
    def get_context_data(self, **kwargs):
          context =super(HomeView,self).get_context_data(**kwargs)
          context['venues']=Venue.objects.order_by('-created_date').filter(is_featured=True)
          context['events']=Event.objects.order_by('-created_date').filter(is_featured=True)
          context['teams']=Team.objects.all()
          context['artists']=Artist.objects.order_by('-created_date').filter(is_featured=True)
          return context



def search(request):
    if request.method == 'GET':
        q =request.GET['q']
        # q = form.cleaned_data['q']
        # artists=Artist.objects.filter(artist_name__search=q)
        # artists=Artist.objects.annotate(search=SearchVector('artist_name','event_name','event_description','category'),).filter(search=q)

        # search by rank 
        vector =SearchVector('artist_name', weight='A',) + SearchVector('event_name',weight='A')+ SearchVector('event_description',weight='B')
        query =SearchQuery(q)
        
        
        artists=Artist.objects.annotate(rank=SearchRank(vector,query),headline = SearchHeadline('artist_name',query)).order_by('-rank')
        # venues=Venue.objects.filter(venue_name__search=q)
        return render(request,'pages/search.html',{'q':q,'artists':artists
        # ,'venues':venues
        })

    else:
   
     return render(request,'pages/search.html')
# def home(request):
#     # featured_artists = Artist.objects.order_by('-created_date').filter(is_featured=True)
#     # featured_venues = Venue.objects.order_by('-created_date').filter(is_featured=True)
#     # featured_events = event.objects.order_by('-created_date').filter(is_featured=True)
#     # data= {
#     #
#     #    'featured_artists':featured_artists,
#     #    'featured_events':featured_events,
#     #    'featured_venues':featured_venues,
#     # }
#     return render(request,'pages/home.html'
#     # ,data
#     )

def about(request):
    teams = Team.objects.all()
    # featured_artists = Artist.objects.order_by('created_date').filter(is_featured=True)
    data= {
       'teams':teams,
       # 'featured_artists':featured_artists,
    }
    return render(request,'pages/about.html',data)
def contact(request):
    return render(request,'pages/contact.html')
