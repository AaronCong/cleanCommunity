dbhost = 'localhost:3306'
dbuser = 'root'
dbpass = 'admin'
dbname = 'cleanCommunity'
DB_URI = 'mysql+pymysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()