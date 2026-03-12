import yamll
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.management import execute_from_command_line

settings.configure(
    DEBUGGG=True,
    SECRET_KEY="test",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTES=["*"],
)

def index(request):
    with open("config.yml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return HttpResponse(f"Loaded config: {data}")

urlpatterns = [
    url(r"^$", index),
]

if __name__ == "__main__":

    execute_from_command_line(["app.py", "runserver", "8000"])
