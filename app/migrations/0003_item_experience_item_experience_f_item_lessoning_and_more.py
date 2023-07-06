# Generated by Django 4.1.7 on 2023-05-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_sectioninf'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Experience',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript/jQuery', 'JavaScript/jQuery'), ('PHP', 'PHP'), ('Python', 'Python'), ('SQL(MySQL)', 'SQL(MySQL)'), ('Java', 'Java'), ('C', 'C'), ('C#', 'C#'), ('C++', 'C++'), ('Ruby', 'Ruby'), ('VBA', 'VBA'), ('GAS', 'GAS')], default=None, max_length=200, verbose_name='業務経験プログラミング言語'),
        ),
        migrations.AddField(
            model_name='item',
            name='Experience_F',
            field=models.CharField(choices=[('Laravel', 'Laravel'), ('Ruby on rails', 'Ruby on rails'), ('Django', 'Django'), ('React', 'React'), ('Next.js', 'Next.js'), ('Vue.js', 'Vue.js'), ('Angular', 'Angular')], default=None, max_length=200, verbose_name='業務経験Webフレームワーク'),
        ),
        migrations.AddField(
            model_name='item',
            name='Lessoning',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript/jQuery', 'JavaScript/jQuery'), ('PHP', 'PHP'), ('Python', 'Python'), ('SQL(MySQL)', 'SQL(MySQL)'), ('Java', 'Java'), ('C', 'C'), ('C#', 'C#'), ('C++', 'C++'), ('Ruby', 'Ruby'), ('VBA', 'VBA'), ('GAS', 'GAS')], default=None, max_length=200, verbose_name='勉強中プログラミング言語'),
        ),
        migrations.AddField(
            model_name='item',
            name='Lessoning_F',
            field=models.CharField(choices=[('Laravel', 'Laravel'), ('Ruby on rails', 'Ruby on rails'), ('Django', 'Django'), ('React', 'React'), ('Next.js', 'Next.js'), ('Vue.js', 'Vue.js'), ('Angular', 'Angular')], default=None, max_length=200, verbose_name='勉強中Webフレームワーク'),
        ),
        migrations.AddField(
            model_name='item',
            name='Tecnic',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript/jQuery', 'JavaScript/jQuery'), ('PHP', 'PHP'), ('Python', 'Python'), ('SQL(MySQL)', 'SQL(MySQL)'), ('Java', 'Java'), ('C', 'C'), ('C#', 'C#'), ('C++', 'C++'), ('Ruby', 'Ruby'), ('VBA', 'VBA'), ('GAS', 'GAS')], default=None, max_length=200, verbose_name='使用可能プログラミング言語'),
        ),
        migrations.AddField(
            model_name='item',
            name='Tecnic_F',
            field=models.CharField(choices=[('Laravel', 'Laravel'), ('Ruby on rails', 'Ruby on rails'), ('Django', 'Django'), ('React', 'React'), ('Next.js', 'Next.js'), ('Vue.js', 'Vue.js'), ('Angular', 'Angular')], default=None, max_length=200, verbose_name='使用可能Webフレームワーク'),
        ),
        migrations.AddField(
            model_name='item',
            name='officePC_L',
            field=models.CharField(choices=[('Excel', 'Excel'), ('Word', 'Word'), ('PowerPoint', 'PowerPoint'), ('Access', 'Access'), ('Google SpreadSheet', 'Google SpreadSheet'), ('GoogleDocs', 'GoogleDocs')], default=None, max_length=200, verbose_name='勉強'),
        ),
    ]
