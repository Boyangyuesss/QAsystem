

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QAManagement', '0003_usermining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermining',
            name='userlike',
            field=models.FloatField(null=True),
        ),
    ]
