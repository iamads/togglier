#!/bin/bash
read -p "Enter UserId : " UserId
read -p "Enter Password : " pass
SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )
crontab -l > mynewcron
echo "@reboot ${SCRIPTPATH}/initiate.sh ${UserId} ${pass}" >> mynewcron
crontab mynewcron
rm mynewcron

apt-get update
apt-get install -y python-zmq python-pip
pip install sleekxmpp
