"""Contact Form"""

from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from contact.models import Contact

def create(request):
    """Create forms"""
    title = 'a'

    context = {
        'title': title,
    }

    return render(
        request=request,
        template_name='contact/create.html',
        context=context,
    )
