from os import name
from django.urls import path, include
from core.views import upload_orgunits, upload_tx_curr_new_pvls, post_tx_curr_new_pvls, TxCurrCounterViewset
from rest_framework.routers import DefaultRouter

app_name = 'core'

router = DefaultRouter()
router.register('txcurr-counter', TxCurrCounterViewset)

urlpatterns = [
    path('', include(router.urls))
    # path('', upload_orgunits, name='upload_orgunits'),
    # path('tx-curr-new-pvls', upload_tx_curr_new_pvls,
    #      name='upload_tx_curr_new_pvls'),
    # path('post_tx_curr_new_pvls', post_tx_curr_new_pvls,
    #      name='post_tx_curr_new_pvls'),
]
