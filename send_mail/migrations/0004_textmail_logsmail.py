# Generated by Django 4.2.4 on 2023-08-29 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0003_alter_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200, verbose_name='тема письма')),
                ('body', models.TextField(verbose_name='тело письма')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send_mail.mail', verbose_name='письмо')),
            ],
            options={
                'verbose_name': 'Сообщение для рассылки',
                'verbose_name_plural': 'Сообщения для рассылки',
            },
        ),
        migrations.CreateModel(
            name='LogsMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_last_try', models.DateTimeField(verbose_name='дата и время последней попытки')),
                ('status_try', models.CharField(max_length=10, verbose_name='статус последней попытки')),
                ('answer_mail_server', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send_mail.mail', verbose_name='письмо')),
            ],
            options={
                'verbose_name': 'Логи сообщения',
                'verbose_name_plural': 'Логи сообщения',
            },
        ),
    ]
