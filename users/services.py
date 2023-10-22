from django.core.mail import send_mail


def send_new_password(email, new_password):
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email='fuckup@oscarbot.ru',
        recipient_list=[email]
    )