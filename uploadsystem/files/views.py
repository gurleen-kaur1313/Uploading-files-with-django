from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'files/home.html', context)

