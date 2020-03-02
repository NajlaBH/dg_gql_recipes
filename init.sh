#! /bin/sh
  
file=db.sqlite3
if [ -e "$file" ]; then
  # Control will enter here if $file exists
  rm $file
fi


python3 manage.py migrate
python3 manage.py test
