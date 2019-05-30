# Generated by Django 2.0.1 on 2019-05-30 08:35

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutDocsOrlan',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('first_image', models.ForeignKey(blank=True, help_text='Изображение должно быть в разрешении ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Первая картинка в селекции основные сведения')),
                ('second_image', models.ForeignKey(blank=True, help_text='Изображение должно быть в разрешении ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Вторая картинка в селекции основные сведения')),
            ],
            options={
                'verbose_name': 'информация об оброзавательной организации (не трогать!)',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Star_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(default='Заголовок', max_length=50, verbose_name='Заголовок селекции которую вы хотите описание')),
                ('description', wagtail.core.fields.RichTextField(default='Text', verbose_name='Описание селекции')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_info', to='about_orlan_docs.AboutDocsOrlan')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
