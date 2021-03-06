from __future__ import unicode_literals

import uuid
from django.db import models


class DeepLink(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
