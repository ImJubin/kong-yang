# dump_to_file.py

import os
import django
from django.core.management import call_command

# settings.py 경로 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fin_pjt_kong_yang.settings')
django.setup()

# UTF-8로 안전하게 저장
with open('db_all.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', '--indent', '2', stdout=f)
