#!/usr/bin/env bash
export LOGGER_CONFIG=$(cd .. && pwd)/data_platform/cfg/logging.json


export DATA_PLATFORM_HOME=`pwd ..`


export IBM_CATEGORIES=$DATA_PLATFORM_HOME/data/IBM_Categories.txt


#Elasticsearch evironment variable
export ES_INDEX=etl_10_18
export ES_USER_YELP=user_yelp
export ES_USER_FB=user_fb
export ES_USER_TW=user_tw
export ES_POI=poi
