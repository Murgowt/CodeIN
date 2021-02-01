from django.urls import path,include
from . import views 
urlpatterns = [
    path('add-Tag',views.CreateTag,name='CreateTag'),
    path('add-Question',views.CreateQuestions,name="CreateQuestions"),
    path('problems',views.Problems,name="Problems"),
    path('problems/<TAG>',views.TagProblems,name="TagProblems")
]
