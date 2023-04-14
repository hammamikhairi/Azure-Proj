#!/bin/sh

echo =========  Deploying Azuuu  ==========
echo
echo ==== Installing Required Packages ====
echo "All pip Packages Installed !"
python -m pip install --upgrade pip
pip install -r requirements.txt
echo
echo ==== Exporting Environment variables ====
echo "exporting : "
export AZURE_DB_SECRET="YOUR_SQL_SERVER_PASSWORD"
echo "   > Azure DB Token"
echo
echo ==== Starting Application ====
python3 main.py

