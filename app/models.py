from tortoise.models import Model
from tortoise import fields


class File(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    bucket = fields.CharField(max_length=255)

    class Meta:
        table = "files"


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    hsk_level = fields.IntField()

    class Meta:
        table = "categories"


class Hanzi(Model):
    id = fields.IntField(pk=True)
    hanzi_text = fields.CharField(max_length=10)
    pinyin = fields.CharField(max_length=100)
    meaning = fields.TextField()
    hsk_level = fields.IntField()
    image_file = fields.ForeignKeyField("models.File", related_name="hanzis", null=True)
    category = fields.ForeignKeyField(
        "models.Category", related_name="hanzis", null=True
    )

    class Meta:
        table = "hanzis"


