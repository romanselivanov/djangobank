from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings


def send_email_verification(user):
    # code = email_verification_token.make_token(user)
    # url = settings.EMAIL_VERIFICATION_URL.format(code)
    # params = dict(user=user, url=url)
    # msg_txt = get_template("registration/email_verification.txt").render(params)
    # msg_html = get_template("registration/email_verification.html").render(params)
    # send_mail(
    #     subject="Незаурядный банк: Подтверждение электронной почты",
    #     message=msg_txt,
    #     from_email=settings.EMAIL_FROM,
    #     recipient_list=[user.email],
    #     fail_silently=False,
    #     html_message=msg_html
    # )
    print('email sent')
