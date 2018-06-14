#!/bin/bash

# Installing conan
sudo pip3 install conan sphinx sphinx_rtd_theme breathe

# Installing Coveralls
sudo pip3 install cpp-coveralls

# Installing library dependencies with conan
conan remote add -f conan-mpusz https://api.bintray.com/conan/mpusz/conan-mpusz
conan remote add -f boost_math https://api.bintray.com/conan/bincrafters/public-conan
conan install . --build missing