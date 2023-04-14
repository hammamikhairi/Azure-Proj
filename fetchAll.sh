#!/bin/sh

echo ==========  Fetching Data  ===========
echo
echo ==== Exporting Environment variables ====
echo "exporting : "
export AZURE_DB_SECRET="YOUR_SQL_SERVER_PASSWORD"
echo "   > Azure DB Token"
echo
echo ==== Starting Application ====
python3 GetAll.py

