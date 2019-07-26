# Generated by Django 2.0.1 on 2019-07-26 19:37

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutDocsOrlan',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date_of_creation', wagtail.core.fields.RichTextField(default='Default', verbose_name='Дата создания тектс')),
                ('brief_information', wagtail.core.fields.RichTextField(default='Default', verbose_name='Информация об учреждении')),
                ('founder', wagtail.core.fields.RichTextField(default='Default', verbose_name='Учредитель')),
                ('locate', wagtail.core.fields.RichTextField(default='Default', verbose_name='Местонахождение')),
                ('driving_schedule', wagtail.core.fields.RichTextField(default='Default', verbose_name='График вождения')),
                ('schedule', wagtail.core.fields.RichTextField(default='Default', verbose_name='График работы')),
                ('numbers', wagtail.core.fields.RichTextField(default='Default', verbose_name='Контактные телефоны')),
                ('email', wagtail.core.fields.RichTextField(default='Default', verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Об автошколе',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ChildAboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body_mother', wagtail.core.fields.StreamField([('child', wagtail.core.blocks.StreamBlock([('Текст', wagtail.core.blocks.RichTextBlock()), ('документ', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='Заголовок')), ('static_name', wagtail.core.blocks.CharBlock(classname='ссылка на документ'))]))), ('мб_с_описанием', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(classname='иконка')), ('title', wagtail.core.blocks.CharBlock(classname='заголовок для блока')), ('description', wagtail.core.blocks.RichTextBlock())]))), ('мб', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(classname='иконка')), ('title', wagtail.core.blocks.CharBlock(classname='заголовок для блока'))]))), ('документ_строка', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='Заголовок')), ('static_name', wagtail.core.blocks.CharBlock(classname='ссылка на документ'))]))), ('мб_с_описанием_строка', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(classname='иконка')), ('title', wagtail.core.blocks.CharBlock(classname='заголовок для блока')), ('description', wagtail.core.blocks.RichTextBlock())]))), ('мб_строка', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(classname='иконка')), ('title', wagtail.core.blocks.CharBlock(classname='заголовок для блока'))]))), ('два_фото', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('static_name1', wagtail.core.blocks.CharBlock(classname='Название первой фото')), ('static_name2', wagtail.core.blocks.CharBlock(classname='Название второго фото')), ('static_name3', wagtail.core.blocks.CharBlock(classname='Название третьего фото'))])))]))], blank=True, default=None, null=True, verbose_name='Большой блок')),
            ],
            options={
                'verbose_name': 'Создать дочернюю страницу об автошколе',
            },
            bases=('wagtailcore.page',),
        ),
    ]
