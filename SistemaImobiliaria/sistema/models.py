from django.db import models


class Aluguel(models.Model):
    id_aluguel = models.IntegerField()
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_imovel = models.ForeignKey('Imovel', models.DO_NOTHING, db_column='id_imovel', blank=True, null=True)
    id_corretor = models.ForeignKey('Corretor', models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    data_aluguel = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    contrato = models.CharField(max_length=100, blank=True, null=True)
    valor_aluguel = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aluguel'






class Boleto(models.Model):
    id_boleto = models.IntegerField()
    id_aluguel = models.ForeignKey(Aluguel, models.DO_NOTHING, db_column='id_aluguel', blank=True, null=True)
    id_venda = models.ForeignKey('Venda', models.DO_NOTHING, db_column='id_venda', blank=True, null=True)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    valor_boleto = models.FloatField(blank=True, null=True)
    multa_juros = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'boleto'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nome_cliente = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente'


class Contato(models.Model):
    id_contato = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='propietario', blank=True, null=True)
    id_corretor = models.ForeignKey('Corretor', models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'contato'


class Corretor(models.Model):
    id_corretor = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)
    registro = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'corretor'






class Endereco(models.Model):
    id_endereco = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_imovel = models.ForeignKey('Imovel', models.DO_NOTHING, db_column='id_imovel', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'endereco'


class Imovel(models.Model):
    id_imovel = models.IntegerField(db_column='Id_imovel')  # Field name made lowercase.
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='Id_propietario', blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    matricula = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    iptu = models.CharField(max_length=100, blank=True, null=True)
    metro_quadrado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'imovel'




class Mensagens(models.Model):
    id_mensagens = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    assunto = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_envio = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mensagens'


class Propietario(models.Model):
    id_propietario = models.IntegerField(primary_key=True)
    nome_propietario = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'propietario'


class Venda(models.Model):
    id_venda = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey(Propietario, models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_imovel = models.ForeignKey(Imovel, models.DO_NOTHING, db_column='Id_imovel', blank=True, null=True)  # Field name made lowercase.
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True)
    valor_imovel = models.FloatField(blank=True, null=True)
    valor_venda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'venda'
