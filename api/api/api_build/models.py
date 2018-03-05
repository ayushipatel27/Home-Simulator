# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appliances(models.Model):
    applianceid = models.IntegerField(primary_key=True)
    sensorid = models.ForeignKey('Sensors', models.DO_NOTHING, db_column='sensorid')
    powerusage = models.IntegerField()
    powerrate = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'appliances'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dailyusage(models.Model):
    date = models.DateField(primary_key=True)
    totalwaterusage = models.FloatField()
    totalpowerusage = models.IntegerField()
    totalpowercost = models.TextField()  # This field type is a guess.
    totalwatercost = models.TextField()  # This field type is a guess.
    totalhvacusage = models.FloatField()
    totalhvaccost = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dailyusage'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Energyusage(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    sensorid = models.IntegerField()
    endtimestamp = models.DateTimeField(blank=True, null=True)
    usage = models.IntegerField()
    cost = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'energyusage'
        unique_together = (('timestamp', 'sensorid'),)


class Hvacusage(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    sensorid = models.IntegerField()
    endtimestamp = models.DateTimeField(blank=True, null=True)
    usage = models.FloatField()
    cost = models.TextField()  # This field type is a guess.
    temperature = models.FloatField()

    class Meta:
        managed = False
        db_table = 'hvacusage'
        unique_together = (('timestamp', 'sensorid'),)


class Rooms(models.Model):
    roomid = models.IntegerField(primary_key=True)
    roomname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rooms'


class Sensors(models.Model):
    sensorid = models.IntegerField(primary_key=True)
    sensorname = models.CharField(max_length=50)
    sensorstate = models.IntegerField()
    roomid = models.ForeignKey(Rooms, models.DO_NOTHING, db_column='roomid')

    class Meta:
        managed = False
        db_table = 'sensors'


class Waterusage(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    sensorid = models.IntegerField()
    endtimestamp = models.DateTimeField(blank=True, null=True)
    usage = models.FloatField()
    cost = models.TextField() # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'waterusage'
        unique_together = (('timestamp', 'sensorid'),)


class Weather(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    temperature = models.FloatField()
    precipitation = models.FloatField()
    chanceofprecipitation = models.FloatField()
    state = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'weather'