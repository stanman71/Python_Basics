
#################
DATABASE (MySQL):
#################

Database:  python
Tablename: user
           id       (Integer, primary_key)
           username (String(15), unique)
           email    (String(50), unique)
           password (String(80))