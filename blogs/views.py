from django.http.response import HttpResponseRedirect
from .forms import CommentForm
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Blog, Blog_Comment,Tag
from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

class BlogListView(ListView):
    model = Blog
    paginate_by = 2
    template_name ='blogs/blogs.html'
    ordering='-created_date'
class BlogDetailView(DetailView):
    model =Blog
    template_name = 'blogs/blog_detail.html'

    def get_related_blogs_by_tags(self):
        return Blog.objects.filter(tag_slug=self.tag_slug).exclude(slug=self.slug)
        
    def get_context_data(self,*args,**kwargs):
        context =super(BlogDetailView,self).get_context_data(**kwargs)
       
    #    for like unlike
        blogs_to_like = get_object_or_404(Blog,slug=self.kwargs['slug'])
        total_likes = blogs_to_like.total_likes()
        liked=False
        if blogs_to_like.likes.filter(id=self.request.user.id).exists():
            like=False

        #  for commenting 
        blog_to_comment =get_object_or_404(Blog,slug=self.kwargs['slug'])
        form= CommentForm()
        comments=Blog_Comment.objects.filter(blog=blog_to_comment).order_by('-created_date',)

        context['total_likes']=total_likes
        context['liked']=liked
        context['form']=form
        context['blog_to_comment']=blog_to_comment
        context['comments']=comments
        return context

    @method_decorator(login_required)
    def post(self,request,slug,**kwargs):
        blog = get_object_or_404(Blog,slug=slug)
        new_comment =None
        form=CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user=request.user
            new_comment.blog=blog
            new_comment.save()

        comments=Blog_Comment.objects.filter(blog =blog).order_by('-created_date')
        context={'blog':blog,'form':form,'comments':comments
        }
        return render (request,'blogs/blog_detail.html',context)
def TagView(request,slug):
    tag_blog=get_object_or_404(Tag,slug=slug)
    blogs=Blog.objects.filter(tag=tag_blog)
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'category/blog_tag.html',{'page_obj': page_obj,'slug':slug,'tag_blog':tag_blog,'blogs':blogs})

@login_required
def LikeView(request,slug):
    blog=get_object_or_404(Blog,slug=request.POST.get('blog_slug'))
    liked=False
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        liked=False
    else:
        blog.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('blog_detail',args=[str(slug)]))
