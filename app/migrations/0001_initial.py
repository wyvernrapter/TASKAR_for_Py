# Generated by Django 4.1.7 on 2023-05-04 01:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18)], verbose_name='年齢')),
                ('sex', models.IntegerField(choices=[(1, '男性'), (2, '女性')], default=1, verbose_name='性別')),
                ('memo', models.TextField(blank=True, max_length=6000, null=True, verbose_name='備考')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('section', models.CharField(choices=[('管理本部', '管理本部'), ('財務部', '財務部'), ('法務部', '法務部'), ('人事部', '人事部'), ('営業一部', '営業一部'), ('営業二部', '営業二部'), ('IT一部', 'IT一部'), ('IT二部', 'IT二部'), ('広報部', '広報部')], max_length=200, verbose_name='部署')),
                ('rank', models.CharField(choices=[('代表取締役社長', '代表取締役社長'), ('常務取締役', '常務取締役'), ('専務取締役', '専務取締役'), ('本部長', '本部長'), ('部長', '部長'), ('次長', '次長'), ('課長', '課長'), ('課長代理', '課長代理'), ('係長', '係長'), ('社員', '社員')], max_length=200, verbose_name='役職')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='電話番号')),
                ('email_add', models.CharField(max_length=100, verbose_name='メールアドレス')),
                ('postcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=50, verbose_name='住所')),
                ('station1', models.CharField(max_length=20, verbose_name='最寄駅１')),
                ('employee_number', models.IntegerField(verbose_name='社員番号')),
            ],
            options={
                'verbose_name': 'アイテム',
                'verbose_name_plural': 'アイテム',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='sectioninf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=200, verbose_name='部署')),
                ('rank', models.CharField(max_length=200, verbose_name='役職')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
            ],
        ),
    ]
