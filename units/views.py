from django.shortcuts import render

def unit_list(request):
    # Renders the app-level template (Active Asset Register)
    return render(request, 'units/unit_list.html')

def about_reit(request):
    # Renders the project-level template (Trust Overview & Metrics)
    return render(request, 'about_reit.html')