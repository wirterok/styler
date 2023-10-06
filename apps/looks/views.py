from styler_utils.api.contrib.sqlalchemy.viewsets import ModelViewSet

from .models import Look

class LookViewset(ModelViewSet):
    model = Look

    async def list(self):
        data = await super().list()
        breakpoint()