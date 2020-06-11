from django.contrib.auth import get_user_model


class EmailOrUsernameModelBackend:
    """
    Backend that allows authentication with either a username or an email address.

    Inspired by:
    https://stackoverflow.com/questions/25316765/log-in-user-using-either-email-address-or-username-in-django/57138652
    """
    def authenticate(self, request, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
