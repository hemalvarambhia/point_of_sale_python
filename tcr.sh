#!/bin/sh
pytest && git commit -am 'Tests passed' || git restore src