from sendgrid import Mail
from sendgrid.sendgrid import SendGridAPIClient
import os


sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
admin_email = "julio@galtec.pro"


def email_to_client_contact_form(client):
    email = client.email
    name = client.name
    msg = client.msg
    from_email_admin = 'julio@galtec.pro'
    message = Mail(
        from_email=from_email_admin,
        to_emails=email
    )

    message.dynamic_template_data = {
        'clientName': name.title(),
        'clientMsg': msg,
    }
    message.template_id = 'd-f02e463e230443a0a9b1641ce966c4f2'
    sendgrid_client.send(message)


def email_to_admin_client_contact_form(client):
    from_email_admin = 'julio@galtec.pro'
    message = Mail(
        from_email=from_email_admin,
        to_emails=admin_email
    )

    message.dynamic_template_data = {
        'clientName': client.name.title(),
        'clientEmail': client.email,
        'clientMsg': client.msg,
        'clientPhone': client.phone,
        'created': client.created.strftime('%H:%M %d/%m/%Y'),
        'leadOrigin': client.lead_origin
    }
    message.template_id = 'd-46027ee0e7dc4f4c8d114e32ba6f069b'
    sendgrid_client.send(message)