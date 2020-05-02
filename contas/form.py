from django.forms import ModelForm
from .models import Transacao


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data_transacao', 'descricao', 'valor', 'categoria', 'observacoes']
