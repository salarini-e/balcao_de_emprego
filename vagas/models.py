from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from .validations import validate_CNPJ
# Create your models here.
class Vaga_Emprego(models.Model):
    
    class Meta:
        verbose_name_plural = "Vagas de Emprego"
        verbose_name = "Vaga de Emprego"
        ordering = ['empresa']

    EXPERIENCIA_CHOICES=(
                            ('Sim', 'Sim'),
                            ('Não', 'Não')
    )
    ativo=models.BooleanField(default=True)    
    user=models.ForeignKey(User, on_delete=models.PROTECT)                    
    quantidadeVagas=models.IntegerField(blank=False, null=False, verbose_name='Quantidade de vagas')
    vaga=models.CharField(max_length=60, blank=False, null=False)
    empresa=models.CharField(max_length=60, blank=False, null=False)
    cnpj=models.CharField(max_length=60, blank=False, null=False, verbose_name='CNPJ', validators=[validate_CNPJ])
    endereco=models.CharField(max_length=60, blank=False, null=False, verbose_name='Endereço')
    telefone=models.CharField(max_length=11, blank=False, null=False)
    escolaridade=models.CharField(max_length=60)
    experiencia=models.CharField(max_length=3, choices=EXPERIENCIA_CHOICES, verbose_name='Experiência')
    formaDeContato=models.CharField(max_length=60, blank=False, null=False, verbose_name='Forma de contato')
    destaque=models.BooleanField(default=False)
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    