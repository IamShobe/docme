"""
Usage:
    cli.py <doc_dir>... [<out_dir>]

<doc_dir> - Directory of the docs.
<out_dir> - Output directory [Default: doc].
"""
from __future__ import absolute_import
import argparse

from docme.builders.writer import DocWriter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('doc_dirs', type=str, nargs='+',
                        help='Directories of the docs')
    parser.add_argument('out_dir', type=str)
    parser.add_argument('--extra-doc', type=str, nargs='+')
    args = parser.parse_args()
    writer = DocWriter(args.doc_dirs, args.extra_doc)
    writer.generate(args.out_dir)


if __name__ == '__main__':
    main()
