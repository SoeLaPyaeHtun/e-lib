from django.urls import path, include
from rest_framework import routers
from . import views
# , AuthorModelAPIViewSet, CategoryModelAPIViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('model-viewset', BookModelAPIViewSet, basename='model-viewset')

# router2 = DefaultRouter()
# router2.register('model-viewset', AuthorModelAPIViewSet,
#                  basename='model-viewset')

# router3 = DefaultRouter()
# router3.register('model-viewset', CategoryModelAPIViewSet,
#                  basename='model-viewset')


urlpatterns = [
    path('books/', views.Book_Get, name="Boook Get"),
    # path('authors/', include(router2.urls)),
    # path('category/', include(router3.urls))
]
