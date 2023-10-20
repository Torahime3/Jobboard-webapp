#!/bin/bash

default='\033[0m'
red='\033[31m'
green='\033[0;32m'
blue='\033[0;34m'

abort()
{
    echo -e >&2 "${red}
**********************************************************
****************** INSTALLATION ABORTED ******************
**********************************************************
"
    echo "An error occurred. Exiting..." >&2
    exit 1
}

trap 'abort' 0

set -ex

	echo -e "${blue}*********** Install REQUIREMENTS.TXT ***********"
echo -e "${default}"
pip install -r Backend/JobBoard/requirements.txt


	echo -e "${blue}*********** Installing packages ***********"
echo -e "${default}"

sudo apt update
sudo apt-get install postgresql build-essential curl -y


  echo -e "${blue}********** Alter table POSTGRESQL **********"
echo -e "${default}"

sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'jobboard';"
echo -e "${green}Password of postgres has been changed to 'jobboard'";


	echo -e"${blue}********** Django setup **********"
echo -e "${default}"

cd Backend/JobBoard
python3 manage.py makemigrations
python3 manage.py migrate


	echo -e"{blue}********** Populate Dabatase **********"
echo -e "${default}"

python3 populate-db.py
cd ../..


	echo -e "${blue}********** Installing NVM for Svelte **********"
echo -e "${default}"

cd Frontend/jobboard
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
cd ../..

trap : 0

echo -e >&2 "${green}
**********************************************************
************* INSTALLATION DONE SUCCESSFULLY *************
**********************************************************
"
