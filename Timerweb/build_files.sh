 echo "BUILD START"
 python -m pip install -r requirements.txt
 python manage.py collectstatic
 echo "BUILD END"