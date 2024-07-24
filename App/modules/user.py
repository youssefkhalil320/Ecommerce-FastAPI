from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
import datetime


class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=50, null=False, unique=True)
    email = fields.CharField(max_length=200, null=False, unique=True)
    password = fields.CharField(max_length=100, null=False)
    is_verified = fields.BooleanField(default=False)
    join_data = fields.DatetimeField(default=datetime.utcnow)
