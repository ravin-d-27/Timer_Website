 echo "BUILD START"
 python3 -m pip install -r requirements.txt
 python3 manage.py collectstatic --noinput 
 chmod 666 Timer/Data_time/timer_data.csv
 echo "BUILD END"