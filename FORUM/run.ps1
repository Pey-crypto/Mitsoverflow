cls
Write-Host "Just Some Random Script"
python manage.py makemigrations
python manage.py migrate
cat settings.py
python manage.py runserver 0.0.0.0:8000
