from django.urls import path

from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/about/
# http://127.0.0.1:8000/contacts/
urlpatterns = [
    # path('', views.home_view, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('categories/<int:category_id>', views.category_articles, name='category_articles'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/create/', views.create_article_view, name='create'),
    path('articles/<int:pk>/update/', views.UpdateArticle.as_view(), name='update'),
    path('articles/<int:pk>/delete/', views.DeleteArticle.as_view(), name='delete'),

    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.user_logout, name='logout'),

    path('users/<str:username>/articles/', views.author_articles, name='author_articles'),

    path('<str:obj_type>/<int:obj_id>/<str:action>', views.add_vote, name='add_vote'),
    path('search/', views.SearchResultView.as_view(), name='search')

]
