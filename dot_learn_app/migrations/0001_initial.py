# Generated by Django 4.1.4 on 2022-12-30 08:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created", models.DateField(auto_now=True)),
                ("updated", models.DateField(auto_now=True)),
                ("branch", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Chapter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chapter", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic", models.CharField(max_length=100)),
                (
                    "chapter_var",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapter_foreign",
                        to="dot_learn_app.chapter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=100)),
                (
                    "branch_var",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="branch_foreign",
                        to="dot_learn_app.branch",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=100)),
                (
                    "topic_var",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topic_foreign",
                        to="dot_learn_app.topic",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="chapter",
            name="subject_var",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subject_foreign",
                to="dot_learn_app.subject",
            ),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(default=0)),
                ("related", models.CharField(max_length=100)),
                (
                    "answer_var",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_foreign",
                        to="dot_learn_app.answer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="answer",
            name="question_var",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question_foreign",
                to="dot_learn_app.question",
            ),
        ),
    ]
