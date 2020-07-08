#! /bin/bash
# Define the path
BIN=GPAsorter-THU
SRC=${BIN}.py
# Compile the src
pyinstaller -F ${SRC}
rm *.spec
rm __pycache__/*
rmdir __pycache__
# Run the execute
cd dist
rm __*
./${BIN}
cd ..