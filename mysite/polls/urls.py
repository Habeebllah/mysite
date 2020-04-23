from django.urls import path
from polls.views import * 


app_name = "polls"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', DetailsView.as_view(), name='details'),
    path('<int:pk>/results', ResultsView.as_view(), name='results'),
    path('<int:question_id>/votes', votes, name='votes'),



]