
def check_email(email):
    if '@' not in email:
        return False
    white = ['.ru', '.com', '.net']
    server = email[email.rfind('.'):]
    if server not in white:
        return False
    return True


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not check_email(recipient) or not check_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return False
    if recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
        return False
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    return True


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

