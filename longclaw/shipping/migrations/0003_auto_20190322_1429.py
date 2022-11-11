# Generated by Django 2.1.7 on 2019-03-22 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("longclaw_shipping", "0002_auto_20190318_1237"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingRateProcessor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("countries", models.ManyToManyField(to="longclaw_shipping.Country")),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_shipping.shippingrateprocessor_set+",
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
            options={
                "base_manager_name": "objects",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="shippingrate",
            name="processor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="longclaw_shipping.ShippingRateProcessor",
            ),
        ),
    ]
