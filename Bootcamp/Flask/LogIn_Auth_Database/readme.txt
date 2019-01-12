DATABASE (MySQL):

Database:  python
Tablename: user
           id       (Integer, primary_key=True)
           username (String(15), unique=True)
           email    (String(50), unique=True)
           password (String(80))