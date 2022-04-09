from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('activities', views.ActList.as_view(), name="act_list"),
    path('activities/new/', views.ActCreate.as_view(), name="act_create"),
    path('activities/<int:pk>/', views.ActDetail.as_view(), name="act_detail"),
    path('activities/<int:pk>/update', views.ActUpdate.as_view(), name="act_update"),
    path('activities/<int:pk>/delete', views.ActDelete.as_view(), name="act_delete"),
    path('user/<username>/', views.profile, name="profile"),
    path('reviews/', views.reviews_index, name="reviews_index"),
    path('reviews/<int:review_id>', views.reviews_show, name="reviews_show"),
    path('reviews/create/', views.ReviewCreate.as_view(), name="reviews_create"),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name="reviews_update"),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name="reviews_delete"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.signup_view, name='signup'),
    path('register/', views.register, name='register')
]