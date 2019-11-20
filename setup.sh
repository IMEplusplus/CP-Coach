#!/usr/bin/env bash

# Create database in case it doesn't exist
sqlite3 cp.db '.databases' >/dev/null
