from django.db import models

class Publication(models.Model):
    PUB_TYPES = (
        ('Journal', 'Journal'),
        ('Conference', 'Conference'),
        ('Workshop', 'Workshop'),
    )
    title = models.CharField(max_length=300)
    publication_type = models.CharField(max_length=50, choices=PUB_TYPES)
    is_best_paper = models.BooleanField(default=False)
    abstract = models.TextField()
    bibtex_file = models.FileField(upload_to='publications/bibtex/', blank=True, null=True)
    poster_file = models.FileField(upload_to='publications/posters/', blank=True, null=True)
    date_published = models.DateField()

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Summary of the experiment or article")
    python_notebook = models.FileField(upload_to='articles/notebooks/', blank=True, null=True)
    experimental_results = models.FileField(upload_to='articles/results/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=200, help_text="e.g., Doctor of Philosophy - PhD, Computer Science")
    institution = models.CharField(max_length=200, help_text="e.g., Tezpur University, Assam")
    start_year = models.CharField(max_length=10, help_text="e.g., 2023")
    end_year = models.CharField(max_length=20, default="Present", help_text="Year or 'Present'")
    description = models.TextField(blank=True, null=True, help_text="Optional details about your thesis or coursework")

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    role = models.CharField(max_length=200, help_text="e.g., Teaching Associate")
    organization = models.CharField(max_length=200, help_text="e.g., Gauhati University")
    duration = models.CharField(max_length=100, help_text="e.g., August 2023 - November 2023")
    location = models.CharField(max_length=200, blank=True, null=True, help_text="e.g., Guwahati, Assam, India")
    description = models.TextField(blank=True, null=True, help_text="Details about your role or project")

    def __str__(self):
        return f"{self.role} at {self.organization}"

class Certification(models.Model):
    name = models.CharField(max_length=200, help_text="e.g., UGC NET Certificate")
    issue_date = models.CharField(max_length=100, help_text="e.g., December 2022")
    description = models.TextField(blank=True, null=True, help_text="Optional details about the exam or course")
    certificate_file = models.FileField(upload_to='certifications/', blank=True, null=True, help_text="Optional PDF or image of the certificate")

    def __str__(self):
        return self.name