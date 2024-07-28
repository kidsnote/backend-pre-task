#!/usr/bin/env bash

# 에러가 발생하면 즉시 종료
set -e
echo "Running entrypoint.django.sh"

function mysql_ready(){
python << END
import sys
import os
import MySQLdb

try:
    dbname = os.environ.get('MYSQL_DATABASE')
    user = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')
    host = os.environ.get('MYSQL_HOST')
    port = int(os.environ.get('MYSQL_PORT'))
    conn = MySQLdb.connect(db=dbname, user=user, passwd=password, host=host, port=port)
except MySQLdb.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until mysql_ready; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - continuing..."

python ./backend/manage.py collectstatic --noinput --verbosity 0

whoami=${WHOAMI:-local}

echo "Current environment: $whoami"

# for local debugpy settings
#if [ "$whoami" = "local" ]; then
python ./backend/manage.py runserver 0.0.0.0:8000
#else
#  gunicorn -c ./backend/conf/gunicorn.conf.py wsgi:application --chdir ./backend
#fi