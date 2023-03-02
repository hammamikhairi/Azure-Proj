#!/bin/sh

echo =========  Deploying Azuuu  ==========
echo
echo ==== Installing Required Packages ====
python -m pip install --upgrade pip
pip install -r requirements.txt
echo
echo ==== Preparing Countries\' Names  ====
# XXX : Uncomment for prod
FILE=$(python3 "Countries_Setup.py")
echo Countries\' names saved to $FILE
echo 
echo ==== Exporting Environment variables ====
echo "exporting : "
export AZURE_DB_SECRET="*********"
echo "   > Azure DB Token"
echo
echo ==== Starting Application ====
python3 main.py




