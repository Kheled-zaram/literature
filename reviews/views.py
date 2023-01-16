from django.shortcuts import render

posts = [
    {
        'author': 'Brandon Sanderson',
        'title': 'Mistborn',
        'content': 'Mistborn is the name of Brandon’s epic fantasy trilogy. The first book is technically Mistborn: The Final Empire, though people just tend to call it Mistborn or Mistborn 1. The entire trilogy consists of The Final Empire (2006), The Well of Ascension (2007), and The Hero of Ages (2008). It’s a hybrid epic fantasy heist story with a focus on political intrigue and powerful action scenes.',
        'date_published': '2006'
    },
    {
        'author': 'Brandon Sanderson',
        'title': 'Elantris',
        'content': 'Elantris was the capital of Arelon: gigantic, beautiful, literally radiant, filled with benevolent beings who used their powerful magical abilities for the benefit of all. Yet each of these demigods was once an ordinary person until touched by the mysterious transforming power of the Shaod. Ten years ago, without warning, the magic failed. Elantrians became wizened, leper-like, powerless creatures, and Elantris itself dark, filthy, and crumbling.',
        'date_published': '2005'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'reviews/home.html', context)


def about(request):
    return render(request, 'reviews/about.html', {'title': 'About'})
