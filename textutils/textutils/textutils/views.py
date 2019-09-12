from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyse(request):
    text1=request.POST.get('txt','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    if removepunc=="on":
        #analysed=text1 
        punctuations='''.,?!'":;...-–—()[]/%@#$*&'''
        analysed=""
        for i in text1:
            if i not in punctuations:
                analysed=analysed+i
        params={'purpose':'Remove Punctuations','analysed_text':analysed}
        text1=analysed
    if(fullcaps=="on"):
        analysed=""
        for i in text1:
            analysed=analysed+i.upper()    
        params={'purpose':'Change To Uppercase','analysed_text':analysed}
        text1=analysed
    if(newlineremover=="on"):
        analysed=""
        for i in text1:
            if i !="\n":
                analysed=analysed+i
        params={'purpose':'newlineremover','analysed_text':analysed}
        text1=analysed
    if(extraspaceremover=="on"):
        analysed=""
        for index, i in enumerate(text1):
            if not(text1[index]==" " and text1[index+1]==" "):
                analysed=analysed+i
        params={'purpose':'extraspaceremover','analysed_text':analysed}
        text1=analysed
    if(charcount=="on"):
        #analysed=""
        count=0
        while text1!=0:
            count=count+1
        params={'purpose':'charcount','analysed_text':count}
        text1=analysed
    return render(request,'analyse.html',params)
def about(request):
        return render(request,'about.html')