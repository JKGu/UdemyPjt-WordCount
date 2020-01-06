from django.http import HttpResponse
from django.shortcuts import render
import operator

def home (request):
    return render(request, 'home.html')

def count(request):
    ft = request.GET['fulltext']
    wordList = ft.split()
    dictionary = {}

    for x in wordList:
        if x in dictionary:
            dictionary[x] +=1
        else:
            dictionary[x] = 1

    sortedWords = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True);
    return render(request, 'count.html', {'enteredText': ft, 'count':len(wordList), 'dic':sortedWords})