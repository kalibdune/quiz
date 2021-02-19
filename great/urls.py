from django.urls import path

from . import views
app_name = 'great'
urlpatterns = [
    # ex: /great/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /great/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /great/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /great/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
#<int:question_id>/ выделяет в строке число и обрабатывает его