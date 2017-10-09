from django.shortcuts import render
from .models import Module, Element

def modules(request):
    modules = Module.objects.all()
    return render(request, 'modules.html', {'modules': modules})

def module(request, slug):
    module = Module.objects.filter(slug=slug)[0]
    elements = Element.objects.filter(module=module).order_by('id')
    for element in elements:
        if element.github_link:
            element.github_link = element.github_link.strip('https://').replace('github.com', 'github')
            element.github_link = 'https://nbviewer.jupyter.org/' + element.github_link

        if element.video_link:
            element.video_link = element.video_link.split('/')[-1]

    return render(request, 'module.html', {'module': module, 'elements': elements})


def element(request, module_slug, element_slug):
    module = Module.objects.filter(slug=module_slug)[0]
    element = Element.objects.filter(slug=element_slug)[0]
    if element.github_link:
        element.github_link = element.github_link.strip('https://').replace('github.com', 'github')
        element.github_link = 'https://nbviewer.jupyter.org/' + element.github_link

    if element.video_link:
        element.video_link = element.video_link.split('/')[-1]
    return render(request, 'element.html', {'module': module, 'element': element})
