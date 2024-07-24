from tortoise import Model, fields
from pydantic import BaseModel
import datetime


class Business(Model):
    id = fields.IntField(pk=True, index=True)
    business_name = fields.CharField(max_length=20, null=False, unique=True)
    city = fields.CharField(max_length=100, null=False, default="Unspecified")
    region = fields.CharField(
        max_length=100, null=False, default="Unspecified")
    business_description = fields.TextField(null=True)
    logo = fields.CharField(max_length=200, null=False,
                            default="../images/logo.jpg")
    owner = fields.ForeignKeyField("models.User", related_name="business")
