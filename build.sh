set -o errexit

pip install -r requiriments.txt
python manage.py collectstatic --no-input
python manage.py migrate