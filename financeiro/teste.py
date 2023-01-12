from financeiro.models import *
from cadastros.models import *
from django.db.models.aggregates import *

# solicitacoes = Solicitacao_Pagamento.objects.all().select_related('beneficiario','beneficiario__empresa','beneficiario__empresa__grupo')
solicitacoes = Beneficiario.objects.raw("select fsp.beneficiario_id \
            , fsp.value \
            , cb.id \
            , cb.name name_beneficiario \
            , cb.empresa_id \
            , ce.name name_empresa \
            , ce.grupo_id \
            , cg.name name_grupo \
            from financeiro_solicitacao_pagamento fsp \
            left join cadastros_beneficiario cb on cb.id = fsp.beneficiario_id \
            left join cadastros_empresa ce on ce.id = cb.empresa_id \
            left join cadastros_grupo cg on cg.id = ce.grupo_id ")
# tipo_pagamento = solicitacoes.aggregate(tipo_pagamento = Count('tipo_pagamento_id',distinct=True))
# tipo_pagamento = solicitacoes.annotate(Count('tipo_pagamento',distinct=True))
# tipo_pagamento = solicitacoes.filter(owner=2).values('tipo_pagamento__pk','tipo_pagamento__nome').annotate(count=Count('pk', distinct=True)).order_by()
# print(tipo_pagamento)
for i in solicitacoes:
    print(i.__dict__)