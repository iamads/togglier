import requests 
from xml.sax.saxutils import escape
def add_controller(name,password):
	xml = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<user>
    <username>{}</username>
    <password>{}<password>
</user>""".format(escape(name), escape(password))
	headers = {'Content-Type': 'application/xml'}
	r = requests.post(url='http://192.168.200.115:9090/plugins/userService/users',
	headers=headers,
	data=xml,	
	auth=('admin','admin'))
	print r

add_controller("test@example.com","test")
