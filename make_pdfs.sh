#!/usr/bin/bash

for i in *.md ; do md2pdf --theme=github $i ; done
