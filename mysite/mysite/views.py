# I have created this file -arvind

from django.http import HttpResponse
from django.shortcuts import render 

def index2(request):
    return HttpResponse('''Hello Arvind''')

def about(request):
    return HttpResponse("<h1>About me</h1>") # we can give html code

def href(request):
    return HttpResponse('''<a href="https://www.google.com">Google</a>''')

def example(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("Get/Post")

def index(request):
    params = {'name':'Arvind','place':'Thane'}
    return render(request, 'index.html', params)

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        i= 0
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                i=i+1
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params,i)
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params ,i)
    else:
        # return HttpResponse("Error")
        params = {'purpose':'Unremoved Punctuations', 'analyzed_text': djtext}
        return render(request, 'analyze.html', params)