echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput 
echo Y | icacls Timer\Data_time\timer_data.csv /grant:r Everyone:(R,W)
echo "BUILD END"
