from django import template
register = template.Library()
from ..models import Comment

@register.simple_tag
def useful_comments(post_id):
	cnt=0
	comments=[]
	for comment in Comment.objects.all():
		if comment.post.id == post_id:
			comments.append(comment)
	if len(comments)==0:
		return 0
	else:
		return comments