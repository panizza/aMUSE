from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basetyzer.models import Experience


def reset_password_new_user(request, uidb36, token):
    if request.method == "GET":
        pass
        #TODO[panizza]:ritorna la pagina web
    pass
"""    assert uidb36 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('django.contrib.auth.views.password_reset_complete')
    try:
        uid_int = base36_to_int(uidb36)
        user = UserModel._default_manager.get(pk=uid_int)
    except (ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):"""

@login_required()
def index(request):
    visit = Experience.objects.filter(user=request.user)

    return render(request, 'webinator/user_details.html', {
        'user': request.user,
        'message': '',
        'visit_confirmed': visit.filter(confirmed=True),
        'visit_not_confirmed': visit.exclude(confirmed=True)
    })
