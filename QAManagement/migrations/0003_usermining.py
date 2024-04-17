

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QAManagement', '0002_questioncount'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userip', models.CharField(max_length=100)),
                ('userquestion', models.CharField(max_length=500)),
                ('usersub', models.CharField(max_length=64)),
                ('userattention', models.CharField(max_length=64)),
                ('userlike', models.IntegerField(null=True)),
                ('usercollect', models.CharField(max_length=64, blank=True, null=True)),
                ('times', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
