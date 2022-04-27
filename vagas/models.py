from django.db import models
from django.contrib.auth.models import User
from .validations import validate_CNPJ, validate_TELEFONE
# Create your models here.

class Escolaridade(models.Model):
    
    nome=models.CharField(max_length=150, verbose_name='Nome da escolaridade', unique=True)
    user=models.ForeignKey(User, on_delete=models.PROTECT)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    def __str__(self):
        return '%s' % (self.nome)

class Empresa(models.Model):

    OCULTAR_CHOICES=(
                            (True, 'Ocultar informações da empresa ao encaminhar'),
                            (False, 'Exibir informações da empresa ao encaminhar')
    )

    FORMA_CONTATO_CHOICES=(
                            ('T', 'TELEFONE'),
                            ('E', 'EMAIL'),
                            ('P', 'PRESENCIAL')
    )

    nome=models.CharField(max_length=150, verbose_name='NOME', unique=True)
    cnpj=models.CharField(max_length=14, validators=[validate_CNPJ], verbose_name='CNPJ', unique=True)
    endereco=models.CharField(max_length=60, blank=False, null=False, verbose_name='Endereço')
    telefone=models.CharField(max_length=11, validators=[validate_TELEFONE], blank=False, null=False, verbose_name='Telefone')
    email=models.EmailField(max_length=254)
    formaDeContato=models.CharField(max_length=1, choices=FORMA_CONTATO_CHOICES, verbose_name='Forma de contato')
    ocultar=models.BooleanField(default=True, verbose_name='Informações da empresa', choices=OCULTAR_CHOICES)
    user=models.ForeignKey(User, on_delete=models.PROTECT)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    
    def __str__(self):
        return '%s' % (self.nome)

class Cargo(models.Model):

    nome=models.CharField(max_length=100, verbose_name='Nome da vaga', unique=True)
    user=models.ForeignKey(User, on_delete=models.PROTECT)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    def __str__(self):
        return '%s' % (self.nome)

class Vaga_Emprego(models.Model):

    class Meta:
        verbose_name_plural = "Vagas de Emprego"
        verbose_name = "Vaga de Emprego"
        ordering = ['empresa']

    EXPERIENCIA_CHOICES=(
                            ('Sim', 'Sim'),
                            ('Não', 'Não')
    )
    
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)        
    cargo=models.ForeignKey(Cargo, on_delete=models.CASCADE)
    quantidadeVagas=models.IntegerField(blank=False, null=False, verbose_name='Quantidade de vagas')
    escolaridade=models.ForeignKey(Escolaridade, on_delete=models.CASCADE)
    experiencia=models.CharField(max_length=3, choices=EXPERIENCIA_CHOICES, verbose_name='Experiência')    
    destaque=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.PROTECT)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    ativo=models.BooleanField(default=True)        
    def __str__(self):
        return '%s - %s' % (self.empresa, self.vaga)