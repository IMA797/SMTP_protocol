# Для работы с SMTP-сервером
import smtplib
# Для создания текстового письма
from email.mime.text import MIMEText
# Для получения текущей даты и времени
from datetime import datetime

# Настройки SMTP (Мои данные)
SMTP_SERVER = "smtp.mail.ru"
SMTP_PORT = 587
LOGIN = "magomed.ima797@mail.ru"
# Пароль приложений
PASSWORD = "Здесь_нужен_пароль"

# Данные письма
sender_name = "Исаев Магомед Абдурахманович"
sender_group = "М3О-111БВ-24"
recipient_email = "Почта, на которую отправляются письма"
recipient_name = "Соколов Андрей Дмитриевич"
recipient_group = "М3О-111БВ-24"

# Текст письма
subject = "Лабораторная работа №6"
message_text = f"""Отправитель: {sender_name}, {sender_group}
Получатель: {recipient_name}, {recipient_group}
Время отправки: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}"""

# Текст письма преобразуется в MIME-формат
msg = MIMEText(message_text, 'plain', 'utf-8')

# Формируем простое письмо без MIMEMultipart
msg['From'] = f"{LOGIN}"
msg['To'] = recipient_email
msg['Subject'] = subject
msg['X-Priority'] = '1'
msg['Importance'] = 'high'

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        # Подробный вывод
        server.set_debuglevel(1)
        # Шифрование
        server.starttls()
        # Авторизация
        server.login(LOGIN, PASSWORD)
        #Отправка письма
        server.sendmail(LOGIN, recipient_email, msg.as_string())
    print("Письмо отправлено!")
except Exception as e:
    print(f"Ошибка: {e}")

