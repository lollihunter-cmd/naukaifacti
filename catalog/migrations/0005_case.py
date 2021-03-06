# Generated by Django 3.0.3 on 2020-04-10 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=30)),
                ('case_preview', models.ImageField(upload_to='images/local_library_model_uml.png')),
            ],
        ),
    ]
