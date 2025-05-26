#!/bin/bash

# Connect to the local MongoDB server and list the collections
mongo --eval "db.getCollectionNames()"