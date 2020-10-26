from django.urls import path
from . views import (list_todos,detail_view,create_todo,update_todo,delete_todo)

urlpatterns = [
    path('', list_todos),
    path('create/', create_todo),
    path('<id>/', detail_view),
    path('<id>/update/', update_todo),
    path('<id>/delete/', delete_todo),
]