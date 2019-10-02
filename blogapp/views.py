from django.shortcuts import render,get_object_or_404,redirect
from . models import Post
from .models import Categories ,Comment
from django.contrib.auth.models import User 
from django.views.generic import ListView,DetailView,CreateView
from users.forms import UserRegistrationForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# django.view has class View to create a class based view we have to inherit this class VIew.
# ListView, DetailView, CreateView, TemplateView are more specific 
from django import forms
from django.http import HttpResponse
from users import forms as user_forms
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
# Create functions That handles the logics of various Pages.

# posts=[
# {
	
# 	'author':'Manish',
# 	'title':'BLog Post 1',
# 	'content':'First post content',
# 	'date_posted' : 'August 28, 2018'		
# },
# {
# 	'author':'Ankit',
# 	'title':"BLog Post 2",
# 	'content':'Second  post content',
# 	'date_posted' : 'August 28, 2018'
# },
# {
# 	'author':'Ankit',
# 	'title':"BLog Post 3",
# 	'content':'Second  post content',
# 	'date_posted' : 'August 28, 2018'
# },
# {
# 	'author':'Ankit',
# 	'title':"BLog Post 4",
# 	'content':'Second  post content',
# 	'date_posted' : 'August 28, 2018'
# },
# {
# 	'author':'Ankit',
# 	'title':"BLog Post 5",
# 	'content':'Second  post content',
# 	'date_posted' : 'August 28, 2018'
# },
# {
# 	'author':'Ankit',
# 	'title':"BLog Post 6",
# 	'content':'Second  post content',
# 	'date_posted' : 'August 28, 2018'
# },
# {
# 	'author':'Ankit',
# 	'title':"BLog Post 7",
# 	'content':'Second  post content',
# 	'date_posted' : 'August 28, 2018'
# }
# ]
# Render function returns the HttpResponse object with the rendered text. 

#CLASS BASED VIEWS:
#BASICALLY THE HOME PAGE
class PostListView(ListView):
	model = Post # MODEL WHICH THIS CLASS GONNA USE           view_type e.g. detail,list
	# template_name attribute tells which template to render
	template_name = 'blogapp/newhome.html'# template name form by default for class based views: <app>/<model>_<view_type>.html
	context_object_name = 'posts' # THIS ATTRIBUTE IS FOR GIVING NAME TO THE CONTEXT SO THAT WE 
	# DONT NEED TO CHANGE THE posts VARIABLE USED WITHIN OUR TEMPLATE. 
	ordering = ['-date_posted']
	paginate_by = 5
	# form = UserRegistrationForm() #NOT REQUIRED AS FIELDS ARE WRITTEN IN HTML ITSELF
	# model = Categories
	# template_name = 'blogapp/side_nav.html'
	# context_object_name = 'categories'
	def get_context_data(self,**kwargs):
		 context = super(PostListView,self).get_context_data(**kwargs) # or context = super().get_context_data(**kwargs)
		 # context['posts'] = Post.objects.all()
		 context['categories'] =  Categories.objects.all()
		 # context['comments'] = Comment.objects.all()
		 # context['form'] = self.form#NOT REQUIRED AS FIELDS ARE WRITTEN IN HTML ITSELF
		 return context

class AuthorPostListView(ListView):
	model = Post
	template_name = 'blogapp/author_post.html'# template name form by default for class based views: <app>/<model>_<view_type>.html
	context_object_name = 'posts'
	# ordering = ['-date_posted']
	paginate_by = 5
	# form = UserRegistrationForm()
	def get_queryset(self): # to override the default get_query_set function that it returns.
		user = get_object_or_404(User,username=self.kwargs.get('author_name'))
		return Post.objects.all().filter(author = user).order_by('-date_posted')
	def get_context_data(self,**kwargs):
		 context = super(AuthorPostListView,self).get_context_data(**kwargs) # or context = super().get_context_data(**kwargs)
		 # context['posts'] = Post.objects.all()
		 context['categories'] =  Categories.objects.all()
		 context['comments'] = Comment.objects.all()
		 # context['form'] = self.form
		 return context
class CategoryDetailView(ListView):
	model = Post # MODEL WHICH THIS CLASS GONNA USE
	template_name = 'blogapp/Categories_Detail.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5
	def get_queryset(self):
		# return get_object_or_404(Post,category_id=self.kwargs.filter('pk'))
		# 
		return Post.objects.all().filter(category_id=self.kwargs.get('pk')).order_by('-date_posted')
	def get_context_data(self,**kwargs):
		context = super(CategoryDetailView,self).get_context_data(**kwargs)
		context['categories'] = Categories.objects.all()
		context['comments'] = Comment.objects.all()
		return context
	# def get(self, request,pk):
	# 	# pk=self.request.GET['pk']
	# 	# posts = Post.objects.all().filter(category=<pk>)
	# 	posts = Post.objects.all().filter(category_id=pk)
	# 	categories = Categories.objects.all()
	# 	comments = Comment.objects.all()

	# 	# form = UserRegistrationForm()
	# 	return render(request,'blogapp/Categories_Detail.html',{'posts':posts,'categories':categories,'comments':comments}) 



#creating get_absolute_url method is a way to tell Django to find the url of the
# model object inside the respective Model(i.e. Post in below case) that return the path
# to any specific instance of the Post
# i.e. To redirect the User to The post_detail tamplate as soon as he add the Post label.We
#have to create a get_absolute_url method inside our Post Model of blogapp models.py	
class PostCreateView(LoginRequiredMixin,CreateView):
	# Create view expect to call our form to be form inside our template.
	#template loaded by this view is named as <model>_form as it is sharing a form belonging
	# to Model.forms class
	form_class = user_forms.AddForm
	model = Post
	def form_valid(self,form): #method executed when form gets submitted
		form.instance.author=self.request.user # setting the author value of the col. to current user.
		messages.success(self.request,'Post Added Successfully.')
		return super().form_valid(form) #runs the form_valid mathod on the parent class.



# class PostDetailView(DetailView):
	# model = Post
	# The name of the field on the model that contains the slug. By default, slug_field is 'slug'
	# slug_field = "label"
	#The name of the URLConf keyword argument that contains the slug. By default, slug_url_kwarg is 'slug'.
	# pk_url_kwarg = "label" # slug_url_kwarg ="label
 	#i.e. now we can use <label> in the url instead of <pk> or <slug>

	# queryset = Post.objects.filter( ####### )

	# dispatch is called when the class instance loads
	# def dispatch(self, request, *args, **kwargs):
	# 	self.slug = kwargs.get('slug')

# OTHER WAY USING Post Detail View using get FUNCTION:
class PostDetailView(DetailView):
	# slug_field = "label"
	def get(self,request,slug):
		post = Post.objects.all().filter(label=slug).first()
		categories = Categories.objects.all()
		comments = Comment.objects.all()
		# form = UserRegistrationForm()
		return render(request,'blogapp/post_detail.html',{'post':post,'categories':categories,'comments':comments})
@login_required
def CommentView(request,pk):
	if request.method == 'POST':
		# print(request.POST)
		post = Post.objects.all().filter(id=pk).first()
		form = user_forms.AddComment(request.POST)
		form.instance.user = request.user
		form.instance.post = post
		next = request.POST.get('next','/')
		# print(next) # we get like /newhome/?page=4
		rediurl = next+"#"+post.label
		if form.is_valid():
			form.save()
			messages.success(request,f'Commeted Successfully!')
			# return HttpResponse("Commeted Successfully!")	
			# return HttpResponse("Commeted Successfully!")
			return redirect(rediurl) 
		else:
			messages.success(request,f'Comments can\'t be blank.')
			return redirect(next)

# def ReplyView(request,pk):
	
def about(request):
	# return HttpResponse('<h1>About Page</h1>')
	categories = Categories.objects.all()
	# form = UserRegistrationForm()
	return render(request,'blogapp/about.html',{'title':"About Us!",'categories':categories})

####OLD STUFF
def myblog(request):
	return render(request,'blogapp/myblog.html')
def newhome(request):
	context = {
			'posts': Post.objects.all().order_by('-date_posted'),
			'categories':Categories.objects.all()		
		}
	# print(dir(request.session))
	# print(request.session.session_key)
	return render(request,'blogapp/newhome.html',context)
def cookie_test(request):
	response=render(request,'blogapp/cookie_test.html')
	# response.delete_cookie('cook_user')
	response.set_cookie("cook_user_cookie","username",max_age=84600,path='/')
	# return HttpResponse(request.COOKIES['cook_user'])
	return response
####

####NOT IN USE TILL NOW
def search_posts(request):
	if request.method == "POST":
		search_text = request.POST['search_text']

	else:
		search_text = ''
	result_posts = Post.objects.filter(title__contains=search_text)
	return render(request,'ajax_search.html',{'result_posts':result_posts})
####

####Not USED NOW#
def home(request):
	context = {
		'title':"Home",
		'posts': Post.objects.all().order_by('-date_posted')
	} 
	# return HttpResponse('<h1>Blog Home</h1>')
	return render(request,'blogapp/home.html',context)
	#Here context will have access to posts key of context.
####