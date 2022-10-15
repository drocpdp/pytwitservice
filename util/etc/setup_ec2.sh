# linux update
### rh
#sudo yum update 
### suse - requires "y" prompt
sudo zypper -n update

# create directories
sudo mkdir /opt/services
sudo mkdir /opt/services/configs
sudo mkdir /opt/services/configs/filters
sudo mkdir /opt/services/virtualenvs
sudo mkdir /opt/services/virtualenvs/pytwitservice
sudo mkdir /opt/services/logs
sudo mkdir /opt/services/place_holder_logs
sudo mkdir /opt/services/logs/pytwitter

# set permissions
sudo chmod -R 777 /opt/services/

# install python3
### rh
#sudo yum install python36
### suse
sudo zypper -n install python3

# install and upgrade pip3
### rh
#sudo yum install python-pip
#sudo pip3 install --upgrade pip
### suse (pip3 already installed)
sudo zypper -n install python3-pip

# install/upgrade virtualenv
pip3 install virtualenv --upgrade

# create and update python virtualenv
python3 -m virtualenv /opt/services/virtualenvs/pytwitservice

# activate virtualenv
source /opt/services/virtualenvs/pytwitservice/bin/activate

# install git
### rh
#sudo yum install git
### suse - requires "y" prompt
sudo zypper -n install git

# clone git repo - requires password
git clone https://github.com/drocpdp/pytwitservice.git /opt/services/pytwitservice
sudo chmod -R 777 /opt/services/pytwitservice

# install project pip requirements
pip3 install -r /opt/services/pytwitservice/requirements.txt
