from django.urls import path
from blog import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:category_id>', views.CategoryView.as_view()),
    path('<int:category_id>/<int:article_id>', views.ArticleView.as_view()),
]