from django.urls import path
# from polls.views import hello_world
from polls import views

urlpatterns = [
    # /polls/
    path('', views.ques_list, name="no_link"),  # This is for 'null path' function is passed NOT called hence no ().
    path('<int:ques_id>/', views.ques_detail, name="ques_detail"),
    path('<int:ques_id>/result/', views.result_detail, name="ques_result"),
    path('<int:ques_id>/vote/', views.vote_detail, name="ques_vote"),
]

