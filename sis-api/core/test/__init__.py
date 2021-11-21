from os.path import dirname

from core import config

config.load_config(r"%s/config.yml" % dirname(__file__))

with open(r"%s/../../../sql/create_db.sql" % dirname(__file__)) as file:
    print(file)

# con = mysql.connect()
# con.cmd_query()