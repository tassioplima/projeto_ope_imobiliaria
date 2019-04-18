# Generated by Django 2.0.7 on 2019-04-18 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_aluguel', models.DateField(blank=True, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('contrato', models.CharField(blank=True, max_length=100, null=True)),
                ('valor_aluguel', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aluguel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emissao', models.DateField(blank=True, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('valor_boleto', models.FloatField(blank=True, null=True)),
                ('multa_juros', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('id_aluguel', models.ForeignKey(blank=True, db_column='id_aluguel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Aluguel')),
            ],
            options={
                'db_table': 'boleto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf_cnpj', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
            options={
                'db_table': 'contato',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf_cnpj', models.CharField(blank=True, max_length=100, null=True)),
                ('registro', models.CharField(blank=True, max_length=100, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Cliente')),
            ],
            options={
                'db_table': 'corretor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('cep', models.CharField(blank=True, max_length=100, null=True)),
                ('uf', models.CharField(blank=True, max_length=100, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
                ('id_corretor', models.ForeignKey(blank=True, db_column='id_corretor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Corretor')),
            ],
            options={
                'db_table': 'endereco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('iptu', models.CharField(blank=True, max_length=100, null=True)),
                ('metro_quadrado', models.FloatField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Cliente')),
            ],
            options={
                'db_table': 'imovel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mensagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('data_envio', models.DateField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Cliente')),
                ('id_corretor', models.ForeignKey(blank=True, db_column='id_corretor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Corretor')),
            ],
            options={
                'db_table': 'mensagens',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_proprietario', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'proprietario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField(blank=True, null=True)),
                ('valor_imovel', models.FloatField(blank=True, null=True)),
                ('valor_venda', models.FloatField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Cliente')),
                ('id_corretor', models.ForeignKey(blank=True, db_column='id_corretor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Corretor')),
                ('id_imovel', models.ForeignKey(blank=True, db_column='Id_imovel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Imovel')),
                ('id_propietario', models.ForeignKey(blank=True, db_column='id_propietario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario')),
            ],
            options={
                'db_table': 'venda',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='mensagens',
            name='id_proprietario',
            field=models.ForeignKey(blank=True, db_column='id_proprietario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='id_proprietario',
            field=models.ForeignKey(blank=True, db_column='id_proprietario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='id_imovel',
            field=models.ForeignKey(blank=True, db_column='id_imovel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Imovel'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='id_proprietario',
            field=models.ForeignKey(blank=True, db_column='id_proprietario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario'),
        ),
        migrations.AddField(
            model_name='contato',
            name='id_corretor',
            field=models.ForeignKey(blank=True, db_column='id_corretor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Corretor'),
        ),
        migrations.AddField(
            model_name='contato',
            name='id_proprietario',
            field=models.ForeignKey(blank=True, db_column='id_proprietario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='id_cliente',
            field=models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Cliente'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='id_proprietario',
            field=models.ForeignKey(blank=True, db_column='id_proprietario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='id_venda',
            field=models.ForeignKey(blank=True, db_column='id_venda', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Venda'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='id_cliente',
            field=models.ForeignKey(blank=True, db_column='id_cliente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Cliente'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='id_corretor',
            field=models.ForeignKey(blank=True, db_column='id_corretor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Corretor'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='id_imovel',
            field=models.ForeignKey(blank=True, db_column='id_imovel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Imovel'),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='id_proprietario',
            field=models.ForeignKey(blank=True, db_column='id_proprietario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario'),
        ),
    ]
