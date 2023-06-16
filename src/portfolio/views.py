from django.shortcuts import render

def index(req):
    template = 'index.html'
    data = {}
    data['page_title'] = 'eusuf ahamed - portfolio'
    
    return render(req, template, data)

def about(req):
    template = 'pages/about.html'
    data = {}
    data['page_title'] = 'about - eusuf ahamed'
    
    return render(req, template, data)

def contact(req):
    template = 'pages/contact.html'
    data = {}
    data['page_title'] = 'contact - eusuf ahamed'
    
    return render(req, template, data)