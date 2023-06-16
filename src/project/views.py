from django.shortcuts import render

def projects(req):
    template = 'pages/projects.html'
    data = {}
    data['page_title'] = 'projects - eusuf ahamed'

    return render(req, template, data)
def details(req):
    template = 'pages/project_details.html'
    data = {}
    data['page_title'] = 'daynamic'

    return render(req, template, data)
