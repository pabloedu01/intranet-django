
echo " BUILD START"
python3.9  -m pip install -r requirements.txt
python3.9 manage.py collectstatic  --noinput --clear
python3 manage.py makemigrations cadastros
python3.9 manage.py migrate
echo " BUILD END"
