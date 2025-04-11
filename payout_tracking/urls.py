from django.urls import path

from . import views
from .views import FeedbackView

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_delivery, name='add_delivery'),
    path('delivery/<int:delivery_id>/', views.delivery_details, name='delivery_details'),
    path('courier_details/<str:courier>/', views.courier_details, name='courier_details'),
    path('feedback/', FeedbackView.as_view()),
    path('done/', views.DoneView.as_view()),
    path('feedback/<int:feedback_id>/', views.update_feedback, name='update_feedback'),
    path('list_feedback/', views.ListFeedback.as_view(), name='feedbacks_list'),
    path('/detail/<int:pk>', views.DetailFeedback.as_view(), name='detail_feedback')
]
