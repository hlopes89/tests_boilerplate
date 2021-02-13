#!/bin/bash

TMP_DIR_PATH=$(PWD)
rm -rf $TMP_DIR_PATH/tmp
mkdir $TMP_DIR_PATH/tmp
cd $TMP_DIR_PATH/tmp
LATEST_CHROME_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) 
curl -LO https://chromedriver.storage.googleapis.com/$LATEST_CHROME_VERSION/chromedriver_mac64.zip 
unzip chromedriver_mac64.zip -d $TMP_DIR_PATH/tmp/chromedriver/ 


# Move to lib/chromedriver folder
cd ..
cd lib
WORKING_DIR=$(PWD)
mv $TMP_DIR_PATH/tmp/chromedriver/ $WORKING_DIR/chromedriver
chmod 755 $WORKING_DIR/chromedriver

rm -rf $TMP_DIR_PATH/tmp/