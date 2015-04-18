#!/bin/bash

#"""This script is the one which would be run on boot
#It starts the controller_xmpp.py which handles the xmpp communication
#and then forwards the data to controller.py."""

SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )
python "${SCRIPTPATH}/controller.py" &
python "${SCRIPTPATH}/controller_xmpp.py" -j $1 -p $2 
