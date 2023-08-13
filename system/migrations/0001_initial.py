# Generated by Django 4.1.7 on 2023-08-13 21:27

from django.db import migrations, models
import django.db.models.deletion
import system.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('alt_contact_number', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='JobCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_or_query', models.CharField(blank=True, max_length=100, null=True)),
                ('error_code', models.CharField(blank=True, max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_of_query', models.DateField(blank=True, null=True)),
                ('date_of_purchase', models.DateField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_technician_assessment', models.DateField(blank=True, null=True)),
                ('technician_assessment', models.CharField(blank=True, max_length=100, null=True)),
                ('technician_notes', models.CharField(blank=True, max_length=500, null=True)),
                ('additional_notes', models.CharField(blank=True, max_length=500, null=True)),
                ('fault_code', models.CharField(blank=True, max_length=5, null=True)),
                ('repair_type', models.CharField(blank=True, max_length=50, null=True)),
                ('assigned_technician', models.CharField(blank=True, max_length=50, null=True)),
                ('job_status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('In Progress', 'In Progress')], default='Open', max_length=20)),
                ('resolution', models.CharField(blank=True, max_length=500, null=True)),
                ('last_modified_by', models.CharField(blank=True, max_length=50, null=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('closed_by', models.CharField(blank=True, max_length=50, null=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('job_number', system.models.job_numberField(max_length=7, unique=True)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Medium', max_length=10)),
                ('job_type', models.CharField(choices=[('Maintenance', 'Maintenance'), ('Repair', 'Repair'), ('Installation', 'Installation')], default='Repair', max_length=15)),
                ('service_location', models.CharField(blank=True, max_length=50, null=True)),
                ('follow_up_required', models.BooleanField(default=False)),
                ('survey_completed', models.BooleanField(default=False)),
                ('customer_satisfaction', models.IntegerField(blank=True, null=True)),
                ('customer_comment', models.CharField(blank=True, max_length=50, null=True)),
                ('assigned_date', models.DateTimeField(blank=True, null=True)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('pdf_file_1', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('pdf_file_2', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=system.models.job_card_directory)),
                ('job_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='system.jobcard')),
            ],
        ),
    ]
