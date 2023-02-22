from django.urls import path
from .views import ChatListView, ChatCreateView,ChatDetailView, ChatDeleteView, ChatUpdateView

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>/', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete/', ChatDeleteView.as_view())

]