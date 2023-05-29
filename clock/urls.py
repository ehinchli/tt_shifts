from django.urls import path
from .views import ShiftCorrectionView, ClockView, ShiftListView

app_name = 'timeclock'

urlpatterns = [
    path('correction/<shift_id>/', ShiftCorrectionView.as_view(), name='correction'),
    path('clock/', ClockView.as_view(), name='clock'),
    path('sheet/', ShiftListView.as_view(), name='sheet'),
]
