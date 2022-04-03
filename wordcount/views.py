import operator

from django.shortcuts import render
import operator

def home(request):
    return render(request, "word.html", {"counttext":"100"} )

def countword(request):
    words = request.GET['fulltext']
    wordlist=words.split(" ")
    worddict= {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    print(wordlist)
    print(sortedword)

    return render(request, 'count.html', {"words":words,  "worddict": sortedword, "len":len(wordlist), })

def about(request):
    return render(request, 'about.html')