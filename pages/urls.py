from django.urls import path
from .views import (
    PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView
)

urlpatterns = [
    path('', PageListView.as_view(), name='pages_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('create/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/edit/', PageUpdateView.as_view(), name='page_edit'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
]
