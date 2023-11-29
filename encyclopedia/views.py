from django.shortcuts import render

from . import util

import random

from markdown import Markdown

markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entries = util.list_entries()
    if title in entries:
        page = util.get_entry(title)
        page_converted = markdowner.convert(page)
        return render(request, "encyclopedia/entry.html", {
                'body': page_converted, 'title': title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            'message': "Page not found, please try again or create new page."
        })

def search(request):
    wiki_list = []
    entries = util.list_entries()
    q = request.GET['q']
    if util.get_entry(q):
        page = util.get_entry(q)
        page_converted = markdowner.convert(page)
        return render(request, "encyclopedia/entry.html", {
            'body': page_converted, 'title': q
            })
    else:
        for entry in entries:
            if q.lower() in entry.lower():
                wiki_list.append(entry)
    if len(wiki_list) == 0:
                return render(request, "encyclopedia/error.html", {
                    'message': "No entries matched your search criteria, please try again."
                })
    return render(request, "encyclopedia/search.html", {
        'wiki_list': wiki_list, 'entry': entry
    })

def new(request):
    if request.method == 'GET':
         return render(request, "encyclopedia/new.html")
    
    if request.method == 'POST':
        title = request.POST["title"]
        textarea = request.POST["textarea"]
        entries = [entry.lower() for entry in util.list_entries()]
        if title.lower() in entries:
            return render(request, "encyclopedia/error.html", {
                'message': "Sorry, that entry already exists."
            })
        else:
            util.save_entry(title, textarea)
            page = util.get_entry(title)
            page_converted = markdowner.convert(page)
            return render(request, "encyclopedia/entry.html", {
                'body': page_converted, 'title': title
            })
    else:
        return render(request, "encyclopedia/error.html", {
            'message': "We encountered an error, please try again."
        })

def edit(request, title):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)
        page_converted = markdowner.convert(content)
        return render(request, "encyclopedia/entry.html", {
                'body': page_converted, 'title': title
        })
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            'title': title, 'content': content
        })

def randompg(request):
    entries = util.list_entries()
    selection = random.choice(entries)
    page = util.get_entry(selection)
    page_converted = markdowner.convert(page)
    return render(request, "encyclopedia/entry.html", {
                'body': page_converted, 'title': selection
        })