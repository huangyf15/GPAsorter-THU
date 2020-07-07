#! /bin/bash
# Define the path
EDITION="2.2"
BIN=GPAcalculator_v${EDITION}
SRC=${BIN}.py
# Compile the src
pyinstaller -F ${SRC}
rm *.spec
mkdir bin
cp dist/${BIN} bin/
# Run the execute
cd dist
rm __*
./${BIN}
cd ..