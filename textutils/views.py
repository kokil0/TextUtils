# I have created this file - kuku
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello</h1> <a
#     href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">
#     Django CodeWithHarry</a>''')
#
# def about(request):
#     return HttpResponse("About kuku bhai")

# code for video 7
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")

def abaout(request):
    return render(request,'abaout.html')

def ex1(request):
    sites=['''<h1> for Entertainment </h1><a href="https://www.youtube.com">Youtube video</a>''']
    return HttpResponse(sites)

def analyze(request):
    # Get the text
    djtext=request.POST.get('text','default')
    # Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')

    # Check which checkbox is on
    if removepunc =="on":
        # analyzed=djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_Text':analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html',params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to uppercase','analyzed_Text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'New Line Remover','analyzed_Text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(spaceremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="  ":
                analyzed=analyzed+char
        params={'purpose':'Space Remover','analyzed_Text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(charcount=="on"):
        analyzed=""
        for char in djtext:
            if char == analyzed:
                charcount += 1
        params = {'purpose': 'Char Count', 'analyzed_Text': analyzed}

    if(removepunc!="on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please select any operation.")

    return render(request, 'analyze.html', params)

# def capitalizefirst(request):
#     return HttpResponse("<a href='/'>Back</a> Capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("<a href='/'>Back</a> New line remove")
#
# def spaceremove(request):
#     return HttpResponse("<a href='/'>Back</a> Space remove")
#
# def charcount(request):
#     return HttpResponse("<a href='/'>Back</a> Char count")