from django.urls import path
from . import views

urlpatterns = [
    # Dashboard / Core
    path('', views.home, name='home'),
    path('complete/<int:id>/', views.complete_task, name='complete'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # User Profile & Settings
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/theme/', views.settings_theme_view, name='settings_theme'),

    # Checklist APIs
    path('plan/add/', views.plan_add, name='plan_add'),
    path('plan/toggle/<int:id>/', views.plan_toggle, name='plan_toggle'),
    path('plan/delete/<int:id>/', views.plan_delete, name='plan_delete'),
    path('plan/reorder/', views.plan_reorder, name='plan_reorder'),

    # Export Features
    path('export/tasks/pdf/', views.export_tasks_pdf, name='export_tasks_pdf'),
    path('export/history/pdf/', views.export_history_pdf, name='export_history_pdf'),
    path('export/stats/excel/', views.export_stats_excel, name='export_stats_excel'),
]