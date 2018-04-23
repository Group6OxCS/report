#!/bin/bash

pandoc report.md -o report.pdf -s --filter filter.py
