from django.urls import path
from . import views

urlpatterns = [
    path('financeiro/solicitacao_pagamento',views.solicitacao_pagamento,name='solicitacao_pagamento'),
    path('financeiro/solicitacao_pagamento/delete/<str:pk>/', views.deletesolicitacao_pagamento, name="deletesolicitacao_pagamento"),
]