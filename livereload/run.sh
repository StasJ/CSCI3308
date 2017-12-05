#!/bin/bash

cd ..
find . -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.py' | entr touch /tmp/reload
