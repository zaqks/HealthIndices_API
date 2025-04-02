#!/bin/bash
git clone --recursive <url-of-parent-repo>
git submodule init
git submodule update --recursive --remote

