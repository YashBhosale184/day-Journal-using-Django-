from django.urls import path
from . import views # Import your view function from this app

urlpatterns = [
    path('', views.journal_page, name='journal_page'),
]


# username: yash
# password: yashcancook