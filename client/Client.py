#!/usr/bin/env python


from clientVars import *
from GUI import *
from Messages import *
from ConfigurationParser import Parser

print APP_NAME, APP_VERSION, "started...\n"


p = Parser(
	{
		"default_host" : "localhost",
		"default_port" : "2727",
		"alias" : "",
		"RSAkeysize" : "2048",
	
	}, "=")


options = p.parse_file("client.conf")
if options != False:
	msg = Messages();
	startGUI(msg, options)
else:
	print "Failed on a configuration error in client.conf"


