import requests 
from xml.sax.saxutils import escape

def add_controller(name,password):
	xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<user>
	<username>{}</username>
	<password>{}</password>
</user>""".format(escape(name), escape(password))

	headers = {'Content-Type': 'application/xml','Authorization': 'Basic YWRtaW46MTIzNDU='}
	r = requests.post(
    	url='http://192.168.200.105:9090/plugins/userService/users',
    	data=xml, headers=headers, 
    	auth=('admin', 'admin')
	)
	print r 


def make_buddies(user,operator):
	xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<rosterItem>
	<jid>{}</jid>
	<subscriptionType>3</subscriptionType>	
</rosterItem>""".format(escape(user+"@ubuntu"))
	headers = {'Content-Type': 'application/xml','Authorization': 'Basic YWRtaW46MTIzNDU='}
	r = requests.post(
	url='http://192.168.200.105:9090/plugins/userService/users/' + operator + '/roster',
    	data=xml, headers=headers, 
    	auth=('admin', 'admin')
	)
	print r

def friends_with_admin(user):
	make_buddies(user,"admin")
	make_buddies("admin",user)


add_controller("leo","leo")
friends_with_admin("leo")
