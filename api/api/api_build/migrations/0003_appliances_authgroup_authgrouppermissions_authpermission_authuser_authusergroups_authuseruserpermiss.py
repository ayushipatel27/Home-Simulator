# Generated by Django 2.0.2 on 2018-03-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_build', '0002_auto_20180228_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('applianceid', models.IntegerField(primary_key=True, serialize=False)),
                ('powerusage', models.IntegerField()),
                ('powerrate', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'appliances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dailyusage',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('totalwaterusage', models.FloatField()),
                ('totalpowerusage', models.IntegerField()),
                ('totalpowercost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('totalwatercost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('totalhvacusage', models.FloatField()),
                ('totalhvaccost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'dailyusage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Energyusage',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('sensorid', models.IntegerField()),
                ('endtimestamp', models.DateTimeField(blank=True, null=True)),
                ('usage', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'energyusage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hvacusage',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('sensorid', models.IntegerField()),
                ('endtimestamp', models.DateTimeField(blank=True, null=True)),
                ('usage', models.FloatField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('temperature', models.FloatField()),
            ],
            options={
                'db_table': 'hvacusage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('roomid', models.IntegerField(primary_key=True, serialize=False)),
                ('roomname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rooms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('sensorid', models.IntegerField(primary_key=True, serialize=False)),
                ('sensorname', models.CharField(max_length=50)),
                ('sensorstate', models.IntegerField()),
            ],
            options={
                'db_table': 'sensors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Waterusage',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('sensorid', models.IntegerField()),
                ('endtimestamp', models.DateTimeField(blank=True, null=True)),
                ('usage', models.FloatField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'waterusage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('temperature', models.FloatField()),
                ('precipitation', models.FloatField()),
                ('chanceofprecipitation', models.FloatField()),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'weather',
                'managed': False,
            },
        ),
    ]