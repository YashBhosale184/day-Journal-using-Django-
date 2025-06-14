from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import JournalEntry # Import your JournalEntry model

def journal_page(request):
    """
    Fetches all journal entries and displays them on a single page.
    """
    all_entries = JournalEntry.objects.all()
    context = {
        'entries': all_entries
    }

    return render(request, 'journal_app/journal.html', context)

