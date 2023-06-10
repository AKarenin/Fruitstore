from django.urls import path

from fruitstore.views import FruitStoreCreateView, FruitStoreListView, FruitStoreDetailView, FruitStoreUpdateView, \
    FruitStoreDeleteView, FruitStoreFindPnView, FruitStoreFilterByLoc

urlpatterns = [
    path('make/', FruitStoreCreateView.as_view()),
    path('<int:pk>/', FruitStoreDetailView.as_view()),
    path('<int:pk>/update', FruitStoreUpdateView.as_view()),
    path('<int:pk>/delete', FruitStoreDeleteView.as_view()),
    path('view_all/', FruitStoreListView.as_view()),
    path('find_by_pn/<int:phoneNumber>', FruitStoreFindPnView.as_view()),
    path('filter_by_loc/<str:location>', FruitStoreFilterByLoc.as_view()),
]