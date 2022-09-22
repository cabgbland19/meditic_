set -o errexit

pip install -r requeriments.txt
pippython manage.py collectstatic --no-input
python manage.py migrate