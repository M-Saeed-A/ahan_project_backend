from django.urls import path
from . import views
urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name="articles"),
    path('allarticles/', views.AllArticleList.as_view(), name="all-articles"),
    path('lastarticles/', views.LastArticleList.as_view(), name="last-articles"),
    path('articles/<str:slug>/', views.ArticleDetail.as_view(), name="articles-detail"),
    path('comments/', views.ArticleComment.as_view(), name="comments"),
    path('categories/', views.ArticleCategory.as_view(), name="categories"),
    path('categories/<str:url_title>/',
         views.CategoryDetail.as_view(), name="categories-detail"),
    path('redirects/', views.RedirectList.as_view(), name="redirects"),

]