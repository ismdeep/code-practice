#!/usr/bin/env python3
# coding:utf-8

import os
import sys

doc_header = "------------------------------------------------------------------------"


def main():
    doc_path = sys.argv[1]
    f = open(doc_path, 'r')
    lines = f.readlines()
    docs = []
    doc_lines = []
    for line in lines:
        if line.find(doc_header) >= 0:
            if len(doc_lines) > 0:
                docs.append(doc_lines)
            doc_lines= []
            continue
        doc_lines.append(line)
    if len(doc_lines) > 0:
        docs.append(doc_lines)
    for doc_id in range(len(docs)):
        doc_name = '%d.md' % doc_id
        doc_lines = docs[doc_id]
        if len(doc_lines) > 0 and doc_lines[0].find("Doc") >= 0:
            doc_name = "%02d-%s.md" % (doc_id, doc_lines[0].split(' ')[1].strip())
        doc_file = open(doc_name, 'w')
        for line in doc_lines[1:]:
            doc_file.write(line)
        doc_file.close()


if __name__ == '__main__':
    main()

