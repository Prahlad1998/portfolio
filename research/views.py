from django.shortcuts import render
from .models import Publication, Article, Education, Experience, Certification

def portfolio_home(request):
    publications = Publication.objects.all().order_by('-date_published')
    articles = Article.objects.all().order_by('-created_at')
    # Order by start_year descending (newest first)
    education_history = Education.objects.all().order_by('-start_year')
    work_experience = Experience.objects.all().order_by('-id')

    return render(request, 'research/home.html', {
        'publications': publications,
        'articles': articles,
        'education_history': education_history,
        'work_experience': work_experience
    })

def portfolio_home(request):
    publications = Publication.objects.all().order_by('-date_published')
    articles = Article.objects.all().order_by('-created_at')
    education_history = Education.objects.all().order_by('-start_year')
    work_experience = Experience.objects.all().order_by('-id')
    certifications = Certification.objects.all().order_by('-id') # Fetch certs
    
    return render(request, 'research/home.html', {
        'publications': publications,
        'articles': articles,
        'education_history': education_history,
        'work_experience': work_experience,
        'certifications': certifications
    })