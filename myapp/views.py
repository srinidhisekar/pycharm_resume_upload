from django.shortcuts import render, redirect
from .forms import StudentForm
from docx import *
lin = []
def upload(request):
    if request.method == 'POST':
        file1=request.FILES['document']
        document = Document(file1)
        s = []
        for para in document.paragraphs:
            temp=""
            s = (para.text).split()
            s[-1] = s[-1].replace("\n", "")
            s.remove(s[0])
            s.remove(s[0])
            if len(s) == 0:
                return render(request, "error.html")
            if len(s) > 1:
                for i in s:
                    temp += i + " "
            else:
                temp = s[0]
            lin.append(temp)
        dict = {'fname': lin[0],
                'lname': lin[1],
                'mailid': lin[2],
                'city': lin[3],
                'pincode': lin[4],
                'state': lin[5],
                'country': lin[6],
                'skill': lin[7]}

        form = StudentForm(dict)
        if form.is_valid():
                form.save()
                return redirect("/upload")
    return render(request,'upload.html')
