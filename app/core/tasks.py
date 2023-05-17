from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.models import TxCurrCounter


@shared_task
def update_txcurr():
    counter = TxCurrCounter.objects.get(id=1)
    counter.increment_value()
