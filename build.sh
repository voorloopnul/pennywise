#!/bin/bash
rm -rf build
rm -rf dist
rm -rf pennywise.egg-info

python setup.py bdist_wheel
twine upload dist/*
