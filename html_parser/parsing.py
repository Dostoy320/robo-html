#!usr/bin/env python

from collections import defaultdict


class TextParsing():

    def get_file_name_from_path(self, path):
        d = defaultdict(int)
        for i in path:
            d[i] += 1

        split_path_group = path.split('/')
        return split_path_group[d['/']].split('.')[0]
