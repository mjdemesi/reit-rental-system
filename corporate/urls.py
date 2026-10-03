from django.urls import path
from . import views

app_name = 'corporate'

urlpatterns = [
    path('investor-relations/', views.investor_relations, name='investor_relations'),
    path('filings/cma/', views.cma_filings, name='cma_filings'),
    path('filings/nse/', views.nse_disclosures, name='nse_disclosures'),
    path('reports/annual/', views.annual_reports, name='annual_reports'),
    path('valuations/', views.independent_valuations, name='independent_valuations'),
]