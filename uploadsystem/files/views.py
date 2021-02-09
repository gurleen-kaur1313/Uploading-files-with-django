from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError


#def upload(request):
    #context = {}
    #if request.method == 'POST':
     #   uploaded_file = request.FILES['document']
      #  if uploaded_file.size > 104857:
       #     raise ValidationError("The maximum file size that can be uploaded is 10MB")
        #fs=FileSystemStorage()
        #name = fs.save(uploaded_file.name, uploaded_file)
        #context['url'] = fs.url(name)
    #return render(request, 'files/home.html', context)

