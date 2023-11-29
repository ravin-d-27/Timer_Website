echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput 
echo Y | icacls Timer\Data_time\timer_data.csv /grant:r Everyone:(R,W)
echo "BUILD END"
