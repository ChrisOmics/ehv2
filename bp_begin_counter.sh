#!/bin/bash

grep qb $1 | cut -d" "  -f1 | sort | uniq -c | awk '{print $2, $1}' | cut -d: -f2 | awk '{print $1","$2}'
