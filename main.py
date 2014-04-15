import sys
import os

from django.conf import settings
from django.conf.urls import patterns
from django.template.response import TemplateResponse
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY='randomsecretkey',
    TEMPLATE_DIRS = (BASE_DIR,),
    ROOT_URLCONF=sys.modules[__name__],
    TWILIO_ACCOUNT_SID='',
    TWILIO_AUTH_TOKEN='',
    TWILIO_APPLICATION_SID='',
)

def index(request):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    application_sid = settings.TWILIO_APPLICATION_SID

    capability = TwilioCapability(account_sid, auth_token)
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming(request.user.username)
    twilio_token = capability.generate()
    return TemplateResponse(request, 'browser-phone.html', locals())

urlpatterns = patterns('', 
    (r'^$', index),
)

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
 