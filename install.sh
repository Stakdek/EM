#!/bin/bash
set -e
sudo chown 777 -R $PWD
echo 'Update Repo…'
git config credential.helper store
git pull
echo 'Installing pip dependicies…'
sudo apt-get install python-pip
sudo pip install telepot --upgrade
sudo pip install multiprocessing --upgrade
sudo pip install psycopg2 --upgrade
sudo pip install psycopg2-binary --upgrade
sudo pip install psutil --upgrade
sudo pip install telegram --upgrade
sudo pip install python-telegram-bot --upgrade
sudo pip install selenium --upgrade
sudo pip install sh --upgrade
sudo pip install requests --upgrade
echo 'Make executable…'
sudo chmod -x $PWD/em.py
sudo chmod 775 $PWD/em.py
sudo rm -f /usr/bin/em
sudo ln -s $PWD/em.py /usr/bin/em
sudo chmod 777 -R $PWD
echo 'Installing Service…'
sudo cp em.service /etc/systemd/system/
echo "Done."
