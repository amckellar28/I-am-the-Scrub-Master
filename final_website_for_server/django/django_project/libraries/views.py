from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def student_group(user):
    return user.is_authenticated() and user.groups.filter(name='Student').exists()

##def search(request):
##    query_string = ''
##    found_entries = None
##    if ('q' in request.GET) and request.GET['q'].strip():
##        query_string = request.GET['q']
##
##        entry_query = get_query(query_string, ['title', 'body',])
##
##        found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')
##
##    return render_to_response('search/search_results.html',
##                          { 'query_string': query_string, 'found_entries': found_entries },
##                          context_instance=RequestContext(request))

@login_required
@user_passes_test(student_group, login_url='/advising/denied/')
def my_view(request):
    return render(request, 'libraries/test.html')


