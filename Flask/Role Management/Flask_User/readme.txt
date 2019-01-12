
#################
DATABASE (MySQL):
#################

Database:  python
Tablename: users
           id       (Integer, primary_key)
           active   (Integer, server_default='1')
           email    (String(255), unique)
           password (String(255))           
           username (String(100), unique)

Tablename: roles
           id       (Integer, primary_key)
           name     (String(50), unique)

Tablename: user_roles
           id      (Integer, primary_key)
           user_id (Integer, ForeignKey('users.id')
           role_id (Integer, ForeignKey('roles.id')