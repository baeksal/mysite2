from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView): #ListView 클래스를 PostList로 상속 
    model = Post
    template_name = 'mytube/post_list.html'
    ordering = ['-pk']
    paginate_by = 40  

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['all_post_count'] = self.get_queryset().count()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return  context

class PostListByCategory(PostList):
    def get_queryset(self):
        slug = self.kwargs['slug']
        if slug == 'no_category':
            category = None
        else:
            category = Category.objects.get(slug=slug)
        return Post.objects.filter(category=category).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super(PostListByCategory, self).get_context_data()

        slug = self.kwargs['slug']
        if slug == 'no_category':
            category = '미분류'
        else:
            category = Category.objects.get(slug=slug)
        context['category'] = category
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'mytube/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return  context
