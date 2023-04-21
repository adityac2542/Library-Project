from django.urls import path
from .views import BooksAvailable, LibHomeView
from . import views
from .models import bookview
app_name = "library"

urlpatterns = [
        path('home/',LibHomeView.as_view(), name='homepage'),
        path('book_form/',views.BookForm_view, name='bookform'),
        path('book_list/',BooksAvailable.as_view(), name='booklist'),
        path('Create_user/',views.new_user_req, name='create_user'),
        path('login/',views.login,name='login'),
        path('loggedout/',views.log_out, name='loggedout'),
        path('home/user_profile', views.user_profile, name='userprofile'),
        path('home/user_profile_display', views.user_profile_display, name='userprofiledisplay'),
        path('book_list/request_book_panel/', views.add_in_books, name='requestpanel'),
]