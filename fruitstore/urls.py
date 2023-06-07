from django.urls import path

from fruitstore.views import FruitStoreCreateView, FruitStoreListView, FruitStoreDetailView, FruitStoreUpdateView, \
    FruitStoreDeleteView

urlpatterns = [
    path('make/', FruitStoreCreateView.as_view()),
    path('<int:pk>/', FruitStoreDetailView.as_view()),
    path('<int:pk>/update', FruitStoreUpdateView.as_view()),
    path('<int:pk>/delete', FruitStoreDeleteView.as_view()),
    path('view_all/', FruitStoreListView.as_view()),
]