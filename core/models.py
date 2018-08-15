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


class GameDays(models.Model):
    game_day_id = models.AutoField(primary_key=True)
    season_id = models.ForeignKey('Seasons', models.DO_NOTHING)
    game_day_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'game_days'


class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_day_id = models.ForeignKey('GameDays', models.DO_NOTHING)
    game_start_time = models.TimeField()
    game_timer = models.TimeField()

    class Meta:
        managed = False
        db_table = 'games'


class Goals(models.Model):
    goals_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('TeamPlayers', models.DO_NOTHING)
    player_id = models.ForeignKey('TeamPlayers', models.DO_NOTHING)
    game_day_id = models.ForeignKey('TeamPlayers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goals'



class Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=50)
    player_birthday = models.DateField()
    player_fone = models.CharField(max_length=12, blank=True, null=True)
    player_register = models.DateField(blank=True, null=True)
    player_email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'


class Positions(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'positions'


class ReadyList(models.Model):
    game_day_id = models.ForeignKey('GameDays', models.DO_NOTHING, primary_key=True)
    player_id = models.ForeignKey('Players', models.DO_NOTHING)
    votes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ready_list'
        unique_together = (('game_day_id', 'player_id'),)


class Seasons(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_year = models.DateField()

    class Meta:
        managed = False
        db_table = 'seasons'


class TeamColors(models.Model):
    team_color_id = models.AutoField(primary_key=True)
    team_color_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'team_colors'


class TeamPlayers(models.Model):
    game_day_id = models.ForeignKey(ReadyList, models.DO_NOTHING, primary_key=True)
    team_id = models.ForeignKey('Teams', models.DO_NOTHING)
    player_id = models.ForeignKey('ReadyList', models.DO_NOTHING)
    position = models.ForeignKey('Positions', models.DO_NOTHING)
    game_day_id_fk = models.ForeignKey('self', models.DO_NOTHING, db_column='game_day')
    team_id_fk = models.ForeignKey('self', models.DO_NOTHING, db_column='game_day')
    substituted_by_player_id = models.ForeignKey('self', models.DO_NOTHING, db_column='player_id')

    class Meta:
        managed = False
        db_table = 'team_players'
        unique_together = (('game_day_id', 'team_id', 'player_id'),)


class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_color_id = models.ForeignKey('TeamColors', models.DO_NOTHING)
    game_id = models.ForeignKey(Games, models.DO_NOTHING)
    team_gols = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teams'

