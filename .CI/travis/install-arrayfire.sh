#!/bin/bash

###################
# Install Arrayfire
###################

wget http://arrayfire.s3.amazonaws.com/3.6.0/ArrayFire-no-gl-v3.6.0_Linux_x86_84.sh

chmod +x ArrayFire-no-gl-v3.6.0_Linux_x86_84.sh
sudo ./ArrayFire-no-gl-v3.6.0_Linux_x86_84.sh --prefix=/usr/local --skip-license
rm ArrayFire-no-gl-v3.6.0_Linux_x86_84.sh
