
############
Basic Roles:
############

-----------------------------------------------
But isn't putting passwords in code a bad idea?
-----------------------------------------------

Yes! This is only supported in the API for demonstration and testing purposes. Users and their roles can (and should!) 
instead be specified in a file loaded via auth.load_from_file("file path here") or auth = BasicRoleAuth(user_file="file path here").

This file defines each user one line at a time in the following format:

<user>:<password>:<role_1>,<role_2>,...<role_n>`

In the case of the above example, this would look like:

bob:secret123:producer
alice:drowssap:producer,consumer
bill:54321:
steve:12345:admin



---------------------------------------
What if I'm too lazy to make that file?
---------------------------------------

This file can also be generated from a configured BasicRoleAuth object via the auth.save_to_file("file path here") function.
What happens if a user fails to authenticate or has no authorization?

If a user fails to authenticate, then BasicRoleAuth.no_authentication is executed to generate the response.

If a user authenticates (i.e. they provide a matching username and password), but their "account" has no authorization to perform 
the action (e.g. in the example above, bob attempting to do DELETE on /tasks), then BasicRoleAuth.no_authorization is executed to 
generate the response.

These methods can be overridden as follows:

def no_authentication():
    return Response("My custom response here", 401)

auth = BasicRoleAuth()
auth.no_authentication = no_authentication



-----------------------------------------------------------------
Anything else I should know before using this in my own projects?
-----------------------------------------------------------------

flask-basic-roles is intended for small projects ideally without user registration (i.e. not a forum website or store) 
and for a small predefined number of users. If you are building something intended for a big audience, don't use this library!

flask-basic-rolesdoes not provide transport level security. If you are building something for use outside of your LAN, 
secure it with HTTPS via a reverse proxy like NGINX.

Passwords are in plain text. Support may be added later for digest access authentication. You should not use passwords you 
tend to use in a lot of different places with this library.
