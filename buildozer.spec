# (c) Copyright 2010-2024 The Kivy Authors. All Rights Reserved.
#
# This file is part of Kivy.
#
# Kivy is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Kivy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Kivy. If not, see <http://www.gnu.org/licenses/>.

[app]

# (str) Title of your application
title = My Face Recognition App

# (str) Package name
package.name = facerecognitionapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.nextgenbywala

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Requirements (python3, kivy, and your specific Python packages)
# - python3: Core Python interpreter.
# - kivy: Your app is built with Kivy.
# - opencv-python: Crucial for camera, face detection (Haar cascade), and face recognition (LBPH).
# - numpy: Core dependency for OpenCV and general numerical operations.
# - requests: Used for submitting data to Google Forms.
# - pillow: A common image processing library often implicitly required by Kivy and OpenCV.
requirements = python3,kivy==2.3.0,opencv-python,numpy,requests,pillow

# (str) Source code where the main.py lives
source.dir = .

# (list) List of exclusions from your application directory, usually things like
# .git, .buildozer, __pycache__ and other temporary files.
source.exclude_dirs = __pycache__, .buildozer, .git, .github, venv, .vscode

# (str) The entrypoint of your application, default is main.py
# Your provided code is the main application logic, assumed to be main.py.
main.py = main.py

# (list) Files and directories to be included directly into the APK assets.
# This is crucial for your Haar cascade XML, images, and audio file.
android.add_src = haarcascade_frontalface_default.xml, tick.png, thank_you.mp3, placeholder_no_camera.png

# (list) Pattern to include additional files not included by default.
# For example, if you have a `known_faces` directory with initial data that you want
# bundled with the APK, you can include it here.
include.patterns = known_faces/*

# (list) Extensions to use (i.e. android, ios, desktop)
extensions =

# (int) The Android SDK version to use. Setting to 33 for better stability with python-for-android.
android.api = 33

# (int) The Android NDK version to use. 25b is a stable choice compatible with many APIs.
android.ndk = 25b

# (bool) The minimum Android SDK version your app will support.
# 21 ensures compatibility with a very wide range of Android devices.
android.minapi = 21

# (str) The architecture to build for (e.g., armeabi-v7a, arm64-v8a, x86_64)
# Building for both common ARM architectures for broad device compatibility.
android.archs = arm64-v8a,armeabi-v7a

# (list) Permissions your application needs.
# - CAMERA: Explicitly required for accessing the device camera.
# - INTERNET: Required for sending data to Google Forms and sending emails (SMTP).
# - WRITE_EXTERNAL_STORAGE/READ_EXTERNAL_STORAGE: Essential for file operations on Android.
# - ACCESS_NETWORK_STATE: Recommended for checking network connectivity.
android.permissions = \
    android.permission.INTERNET,\
    android.permission.CAMERA,\
    android.permission.WRITE_EXTERNAL_STORAGE,\
    android.permission.READ_EXTERNAL_STORAGE,\
    android.permission.ACCESS_NETWORK_STATE

# (bool) Add a notification service (experimental). Essential for larger apps.
# OpenCV can make the app large enough to require multidex to avoid the 65k method limit.
android.enable_multidex = True

# (bool) Whether to use a debug build (False for release). Start with debug.
android.debug = True

# (bool) Whether to enable hardware acceleration (usually recommended)
android.hardware_acceleration = True

# (str) This filter directs logcat to show all Python logs at DEBUG level, and everything else at SILENT.
# This makes it easier to find your app's specific log messages and Python tracebacks.
android.logcat_filters = *:S python:D

[buildozer]

# (list) Arguments to pass to the python-for-android build process.
android.extra_args =

# (int) Log level (0=silent, 1=error, 2=warning, 3=info, 4=debug)
log_level = 5

# (str) Where Buildozer stores its internal files (builds, caches, etc.)
buildozer.dir = .buildozer

# (str) Path to the Buildozer config file (usually this file)
buildozer.config = buildozer.spec

# IMPORTANT NOTE FOR OPENCV BUILDS:
# Compiling 'opencv-python' for Android requires significant system resources,
# especially RAM (8GB+ recommended). If your build is failing or getting
# truncated, an "Out Of Memory" (OOM) error during compilation is a common cause.
# Ensure your build environment has sufficient resources.
# Also, try running 'buildozer clean' before attempting another build to clear
# any corrupted or incomplete build caches.
