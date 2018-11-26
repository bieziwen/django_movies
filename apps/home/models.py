# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


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


# class TFilm(models.Model):
#     fid = models.CharField(max_length=255)
#     actor = models.CharField(max_length=255, blank=True, null=True)
#     cata_log_name = models.CharField(max_length=255)
#     cata_log_id = models.CharField(max_length=255, blank=True, null=True)
#     evaluation = models.FloatField()
#     image = models.CharField(max_length=255, blank=True, null=True)
#     is_use = models.IntegerField()
#     loc_name = models.CharField(max_length=255, blank=True, null=True)
#     loc_id = models.CharField(max_length=255, blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     on_decade = models.CharField(max_length=255, blank=True, null=True)
#     plot = models.TextField(blank=True, null=True)
#     resolution = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     sub_class_name = models.CharField(max_length=255, blank=True, null=True)
#     sub_class_id = models.CharField(max_length=255, blank=True, null=True)
#     type_name = models.CharField(max_length=255, blank=True, null=True)
#     type_id = models.CharField(max_length=255, blank=True, null=True)
#     update_time = models.CharField(max_length=255, blank=True, null=True)
#     is_vip = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         # managed = False
#         db_table = 't_film'


class TClassname(models.Model):
    sub_class_id = models.CharField(max_length=255)
    sub_class_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        # managed = False
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
        # managed = False
        db_table = 't_film'
        unique_together = (('id', 'cata_log', 'loc', 'on_decade', 'sub_class_id'),)


class TLocname(models.Model):
    loc_id = models.CharField(primary_key=True, max_length=255)
    loc_name = models.CharField(max_length=255)

    class Meta:
        # managed = False
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
        # managed = False
        db_table = 't_ondecade'


