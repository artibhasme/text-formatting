from django.shortcuts import render
import os
from django.http import HttpResponse
from django.shortcuts import render


'''
#code for video 3 above from site https://www.youtube.com/watch?v=ES-bdt0KUZg&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=8
def index(request):
    return HttpResponse("Hello Django")

def myname(request):
    return HttpResponse("My Name - Arti")

def surname(request):
    return HttpResponse("<h1>My Surname - Bhasme</h1>")

def tfile1(request):
    f1 = open("mysite\one.txt", "r")
    s = f1.read()
    #return HttpResponse(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return HttpResponse(s)

def tfile2(request):
    f2 = open("mysite\one1.txt", "r")
    return HttpResponse("<h2> %s </h2>" % (f2.read()))
'''

#def nav(request):
#   return HttpResponse('''<h1>Arti</h1> <a href="https://docs.djangoproject.com/en/2.2/intro/"> Getting started with Django </a>''')

#def ulti(request):
#    return HttpResponse('''<h1> <a href = https://auth.ultimatix.net/utxLogin/login?TYPE=33554432&REALMOID=06-000e128c-664b-1c1a-9ba7-abcac0a8f081&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-EdbHMX6T%2bWb8DN7DVmL5sbY%2bn%2b30S7n%2fgIBptYa9dLbudResX4AYm9ObPeNozoDH&TARGET=-SM-HTTPS%3a%2f%2fwww%2eultimatix%2enet%2futxHomeApp%2fredirectToHome%3fTARGET%3dhttps-%3A-%2F-%2Fwww%2eultimatix%2enet-%2FutxHomeApp-%2F> Ultimatix TCS site <a> </h2>''')

def index(request):
    #return HttpResponse('''<h1>Hello Django</h1><br> <a href="/rmpunc">Next</a>''')
    #commenting above because below use of render doing same thing
    params = {'name' : 'Arti', 'prof' : 'stud'}
    return render(request,'index.html',params)

'''#this is comment for code with harry site till video #9
def rmpunc(request):
    print(request.GET.get('text','This is default value'))
    return HttpResponse("""remove the punc <a href="http://127.0.0.1:8000">Back</a>""")

def rmspace(request):
    return HttpResponse("""<h1>Remove Space <a href="/cap1st">Next</a></h1>""")

def cap1st(request):
    return HttpResponse("""<h1>Capitalize 1st letter <a href="/rmnewln">Next</a></h1>""")

def rmnewln(request):
    return HttpResponse("""<h1>Remove New line <a href="/countchar">Next</a></h1>""")

def countchar(request):
    return HttpResponse("""<h1>Count chars <a href="http://127.0.0.1:8000">Back</a></h1>""")

'''

#video #10 starts

def analyze(request):
    text_from_site = request.POST.get("text","this is default value")
    remove_punc = request.POST.get("rmpunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremove = request.POST.get("newlineremove", "off")
    extraspacesremove = request.POST.get("extraspacesremove", "off")
    #charcount = request.GET.get("charcount", "off")


    print(text_from_site)
    print(remove_punc)
    
    punclist = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    if remove_punc == "on":
        analyzed_text = ""
        for char in text_from_site:
            if char not in punclist:
                analyzed_text = analyzed_text + char

        params = {'purpose': "to remove punctuations", 'analyzed_text' : analyzed_text}
        #return render(request,'analyze.html', params)
        text_from_site = analyzed_text

    if fullcaps == "on":
        analyzed_text = ""
        for char in text_from_site:
            analyzed_text = analyzed_text + char.upper()

        params = {'purpose': "full capitalize string", 'analyzed_text' : analyzed_text}
        #return render(request,'analyze.html', params)
        text_from_site = analyzed_text

    if newlineremove == "on":
        analyzed_text = ""
        for char in text_from_site:
            if char not in ("\n", "\r"):
                analyzed_text = analyzed_text + char
        params = {'purpose': "New Line Remover", 'analyzed_text' : analyzed_text}
        text_from_site = analyzed_text

    if extraspacesremove == "on":
        analyzed_text = ""
        for index, char in enumerate(text_from_site):
            if not (text_from_site[index] == " " and text_from_site[index+1] == " "):
                analyzed_text = analyzed_text + char
        params = {'purpose': "Extra space remover", 'analyzed_text' : analyzed_text}
        text_from_site = analyzed_text

        '''               
        if charcount == "on":
            analyzed_text = ""
            count = len(text_from_site)
            params = {'purpose': "final formatted string With char count in string", 'analyzed_text' : analyzed_text, 'char_count' : count}
            return render(request,'analyze.html', params)
        else:
            params = {'purpose': "final formatted string", 'char_count' : count}
            return render(request,'analyze.html', params)
        '''
    if (remove_punc != "on") and (fullcaps != "on") and (newlineremove != "on") and (extraspacesremove != "on"):
        return HttpResponse("please select any of the option")
    else:
        char_count = len(text_from_site)
        params = {'purpose': "final formatted string With char count in string", 'analyzed_text' : analyzed_text, 'char_count' : char_count}
        return render(request,'analyze.html', params)
      



    