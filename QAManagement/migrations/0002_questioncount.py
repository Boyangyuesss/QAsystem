

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QAManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userquestion', models.CharField(max_length=64)),
                ('questioncount', models.IntegerField()),
            ],
        ),
    ]
