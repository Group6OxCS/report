#!/bin/bash

# for i in *.svg; do
#     inkscape -D -z --file=$i --export-pdf="${i%.svg}.pdf" --export-latex
# done;
pandoc report.md -o report.pdf -s --filter filter.py -H preamble.tex -V geometry:margin=1.25in
pandoc contrib.md -o contrib.pdf -s --filter filter.py -H preamble.tex -V geometry:margin=1.25in
for i in contribs/*.md; do
    pandoc "$i" -o "${i%.md}.pdf" -s --filter filter.py -H preamble.tex -V geometry:margin=1.25in
done;
rm contribs.zip
zip contribs.zip contribs/*.pdf
