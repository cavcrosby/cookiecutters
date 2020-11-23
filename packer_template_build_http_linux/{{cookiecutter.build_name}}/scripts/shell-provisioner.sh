#!/bin/bash

sleep 30
echo "!!! Start of provisioner script !!!"
wget "http://$PACKER_HTTP_ADDR/packerbuild.conf"
echo $SSH_PASSWORD | sudo -S mv ./packerbuild.conf /etc/
echo "!!! End of provisioner script !!!"
