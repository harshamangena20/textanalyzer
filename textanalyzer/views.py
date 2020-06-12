from django.http import HttpResponse
from django.shortcuts import render 
def home(request):
    return render(request,'home.html') 

def analyze(request):
    t=request.GET.get('text')
    ch=""
    c=0
    punc='''<>,?/;:"'{]}[+=_-)(*&^%$#@!~`'''
    if t[0].islower():
        ch+=t[0].upper()
    #if as_text[-1]!='.':
    #    as_text+='.'
    for i in range(1,len(t)-1):
        if t[i]in punc:
            c+=1
        elif t[i]=='.' and t[i+1]!=' ':
            ch+=t[i]
            ch+=' '
        else:
            if t[i-1]=='.' and t[i].islower():
                ch+=t[i].upper()
            else:
                ch+=t[i]
    if ch[-2]!='.':
        ch+='.'        
    params={'counted':c,'chars':ch}
    return render(request,'out.html',params)