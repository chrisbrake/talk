#!/bin/env python

import argparse
import pathlib
import sys
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

import falcon
from whitenoise import WhiteNoise

font_end = pathlib.Path(__file__).resolve().parents[1] / 'front_end'
talk = falcon.API()
talk = WhiteNoise(
    talk, index_file=True, autorefresh=True, root=font_end
)

def get_config():
    """ Collect a config to use """
    parser = argparse.ArgumentParser(description='Serve files.')
    parser.add_argument(
        '--port', type=int, default=7900, 
        help='What port should we run on?')
    parser.add_argument(
        '--hostname', type=str, default='0.0.0.0', 
        help='The IP or host address to use?')
    return parser.parse_args()

def main(config):
    """ Start me up! """
    with make_server(config.hostname, config.port, talk) as server:
        print(f"I'm online at: http://{config.hostname}:{config.port}")
        server.serve_forever()

if __name__ == "__main__":
    main(get_config())
