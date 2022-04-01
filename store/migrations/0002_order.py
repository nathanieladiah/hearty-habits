# Generated by Django 4.0.3 on 2022-04-01 02:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('confirmed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('proc', 'Processing'), ('ready', 'Ready'), ('del', 'Delivered')], default='proc', max_length=20)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.customer')),
                ('treat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.treat')),
            ],
        ),
    ]
