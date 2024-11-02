import smtplib

from email.message import EmailMessage

from app.core.celery_worker import celery_app
from app.core.config import settings
from app.core.logging import logging

logger = logging.getLogger(__name__)

_my_email = settings.smtp_user_email
_my_pwd = settings.smtp_user_password._secret_value

@celery_app.task
def confirm_email(to_name:str, token:str, email):
    msg = EmailMessage()
    msg.set_content(f"""
    Hola {to_name}, 
    Para confirmar tu correo, por favor haz click en el siguiente enlace:
    {settings.API_V1_STR}/auth/activate_account/{token}
    """)
    msg['Subject'] = 'Confirmar correo'
    msg['From'] = _my_email
    msg['To'] = email

    with smtplib.SMTP("172.19.0.101", port=25) as smtp:
       smtp.send_message(msg=msg, from_addr=_my_email, to_addrs= email)


