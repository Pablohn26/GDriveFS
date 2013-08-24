#!/usr/bin/env python2.7

import logging

from argparse import ArgumentParser

from gdrivefs.gdfs.gdfuse import mount, load_mount_parser_args

def main():
    parser = ArgumentParser()
    load_mount_parser_args(parser)

    args = parser.parse_args()

    option_string = args.opt[0] if args.opt else None

    try:
        mount(auth_storage_filepath=args.auth_storage_file, 
              mountpoint=args.mountpoint, debug=args.debug, 
              nothreads=args.debug, option_string=option_string)
    except (Exception) as e:
        message = ("Could not do mount [%s]: %s" % (e.__class__.__name__, str(e)))
        logging.exception(message)
        print(message)

if __name__ == '__main__':
    main()

