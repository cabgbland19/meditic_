set -o errexit

pip install -r requiriments.txt
pippython manage.py collectstatic --no-input
python manage.py migrate