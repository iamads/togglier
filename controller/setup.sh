#!/bin/bash
read -p "Enter UserId : " UserId
read -p "Enter Password : " pass

FILE="/etc/init.d/superscript"

SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )

/bin/cat <<EOM >$FILE
bash ${SCRIPTPATH}/initiate.sh ${UserId} ${pass}
EOM

chmod 755 /etc/init.d/superscript
chmod 755 ${SCRIPTPATH}/controller.py
chmod 755 ${SCRIPTPATH}/controller_xmpp.py
chmod 755 ${SCRIPTPATH}/initiate.sh
update-rc.d superscript defaults

apt-get update
apt-get install -y python-zmq python-pip
pip install sleekxmpp
