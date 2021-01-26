from django.urls import path,include
from . import views 
urlpatterns = [
    path('add-Tag',views.CreateTag,name='CreateTag'),
    path('add-Question',views.CreateQuestions,name="CreateQuestions"),
    path('problems',views.problems,name="Problems")
]