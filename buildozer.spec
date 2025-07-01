# Buildozer Spec File
[app]
title = FaceRecognitionApp
package.name = facerecognitionapp
package.domain = org.apurv.facerecognition
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,opencv-python,numpy,requests,pillow
orientation = portrait
fullscreen = 1

# Icon and Presplash (optional)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Entry point
entrypoint = main.py

# Android Permissions
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, VIBRATE, WAKE_LOCK, RECEIVE_BOOT_COMPLETED

# Android API and SDK
android.minapi = 21
android.target = 33
android.ndk = 25b
android.ndk_api = 21

# Architecture
android.archs = armeabi-v7a, arm64-v8a

# Optimize and Strip (recommended for release)
android.strip = true
android.allow_backup = true
android.debug = 0

# Java options (increase if needed)
android.gradle_dependencies = com.google.android.material:material:1.6.1
android.java_enable_assertions = false
android.extra_jars =

# Features
android.use_android_native_api = true

# Disable fullscreen if needed
#fullscreen = 0

# Log Level
log_level = 2

# Environment Variables
# (only set if needed)
# environment = ENV_VAR=value

# Additional PyPI packages outside pip (none needed here)
# p4a.branch = master

# For OpenCV camera support (optional fix)
p4a.local_recipes = ./custom_recipes

# Copy libraries if needed
android.copy_libs = 1

# (Optional) Keystore
# android.release_keystore = /path/to/keystore
# android.release_keyalias = mykey
# android.release_keyalias_password = mypassword
# android.release_keystore_password = mykeystorepassword

# (Optional) Permissions Explanations (Android 13+)
android.permissions_explanations = CAMERA:To detect and recognize your face for attendance, WRITE_EXTERNAL_STORAGE:To save captured images, READ_EXTERNAL_STORAGE:To access saved attendance data, INTERNET:To submit attendance to Google Forms

# End of file
