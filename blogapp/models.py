from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# TO make Rich Text Field Work
# from ckeditor.fields import RichTextField # For only RichTextField
from ckeditor_uploader.fields import RichTextUploadingField # For only RichTextField
# Post Model and User Model Have a relationship of one to many
# Create your models here.

# class PostManager():

class Categories(models.Model):
	# user = models.OneToOneField(User,on_delete=models.CASCADE)
	categories = models.CharField(max_length=255) 

	def __str__(self):
		return "{}".format(self.categories)

class Post(models.Model):
	title = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	content = RichTextUploadingField(blank=True,null=True)
	category = models.ForeignKey(Categories,on_delete=models.CASCADE,blank=True,null=True)
	scheduled = models.BooleanField(default=False)
	date_posted = models.DateTimeField(default = timezone.now)
	date_updated = models.DateTimeField(auto_now=True)
	#auto_now_add=True# --> Time on Creation only 	# auto_now=True ->Current Time on modification as well.
	author = models.ForeignKey(User,on_delete=models.CASCADE)
					#			(to,on_delete)
	# slug = models.SlugField(unique=True)
	# Here author is by default given the username of the user:
	# Because,  AbstractBaseUser class in django.contrib.auth in base_user.py module 
	# is a subclass of Model.models where __str__ function returns USERNAME_FIELD
	# and then, AbstractUser in django.contrib.auth in base_user.py module is a subclass of above class where EMAIL_FIELD = 'email'
    # USERNAME_FIELD = 'username' are set  
    # So we can change __str__ to return email instead and then our author will becom equal to the
    # email of the user without using self.author.email below.

    # To use PostManager model manager.
    # objects = PostManager()


	def __str__(self):
		return "::Title:: {},::Content::{},::Date Creation::{},::Author::{}".format(self.title,self.content,self.date_posted,self.author.username)
	# redirect(redirects to the route passed) vs reverse(return the full url to the route as a string):
	# TO SLUGIFY THE LABEL AND SAVE IT INSIDE THE SLUG FIELD BEFORE SAVING.
	def save(self,*args,**kwargs):
		self.label = slugify(self.label)
		super(Post,self).save(*args,**kwargs)

	def get_absolute_url(self):
		#returning the full path of the post
		return reverse('post-detail-newhome',kwargs={'slug':self.label})
class Comment(models.Model):
	comment = models.TextField()
	# reply = 
	user =  models.ForeignKey(User,on_delete=models.CASCADE)
	post = 	models.ForeignKey(Post,on_delete=models.CASCADE)
	date_created = models.DateTimeField(default = timezone.now)
	class Meta:
		ordering = ['-date_created']
	def __str__(self):
		return "Comment on ::{}:: {}::".format(self.post.title,self.comment)


	# def get_absolute_url(self):
	# 	#returning to the heading of the Post
	# 	reach = '#'+self.label
	# 	return reverse('',kwargs={'':reach})