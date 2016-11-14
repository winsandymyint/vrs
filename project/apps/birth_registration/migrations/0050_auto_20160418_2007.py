# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import birth_registration.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0049_f201_extra_age_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f201',
            name='AGE',
        ),
        migrations.RemoveField(
            model_name='f201',
            name='AGE_CODE',
        ),
        migrations.AddField(
            model_name='f201',
            name='AGE_GROUP',
            field=birth_registration.fields.AgeGroupField(default=99, help_text='Age group for cause of death', choices=[(0, '0 - Under 1 year'), (1, '1 - 1 year'), (2, '2 - 2 years'), (3, '3 - 3 years'), (4, '4 - 4 years'), (5, '5 - 5 years'), (6, '6 - 5-9 years'), (7, '7 - 10-14 years'), (8, '8 - 15-19 years'), (9, '9 - 20-24 years'), (10, '10 - 25-29 years'), (11, '11 - 30-34 years'), (12, '12 - 35-39 years'), (13, '13 - 40-44 years'), (14, '14 - 45-49 years'), (15, '15 - 50-54 years'), (16, '16 - 55-59 years'), (17, '17 - 60-64 years'), (18, '18 - 65-69 years'), (19, '19 - 70-74 years'), (20, '20 - 75-79 years'), (21, '21 - 80-84 years'), (22, '22 - 85 and over'), (99, '23 - No stated')]),
        ),
    ]
