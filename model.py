# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Girl(models.Model):
    create_date = models.CharField(max_length=255, blank=True, null=True)
    desc = models.CharField(max_length=255)
    pulished = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'girl'


class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    img = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    is_delete = models.IntegerField()
    is_vip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'movie'


class TClassname(models.Model):
    sub_class_id = models.CharField(max_length=255)
    sub_class_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_classname'


class TFilm(models.Model):
    fid = models.CharField(max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    cata_log_name = models.CharField(max_length=255)
    cata_log = models.ForeignKey('TLogname', models.DO_NOTHING)
    evaluation = models.FloatField()
    image = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.IntegerField()
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    loc = models.ForeignKey('TLocname', models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    on_decade = models.ForeignKey('TOndecade', models.DO_NOTHING, db_column='on_decade')
    plot = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_class_name = models.ForeignKey(TClassname, models.DO_NOTHING, db_column='sub_class_name')
    sub_class_id = models.CharField(max_length=255)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    is_vip = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_film'
        unique_together = (('id', 'cata_log', 'loc', 'on_decade', 'sub_class_id'),)


class TLocname(models.Model):
    loc_id = models.CharField(primary_key=True, max_length=255)
    loc_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 't_locname'


class TLogname(models.Model):
    cata_log_id = models.CharField(primary_key=True, max_length=255)
    cata_log_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 't_logname'


class TOndecade(models.Model):
    on_decade = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 't_ondecade'


class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    phone = models.CharField(unique=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroups(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_permissions'
        unique_together = (('user', 'permission'),)
