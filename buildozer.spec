[app]
title = FacialRecognitionApp
package.name = facialrecognition
package.domain = org.example
source.dir = .
version = 1.0
requirements = python3,kivy,opencv-python,numpy,requests,certifi,idna,urllib3,chardet
orientation = portrait
fullscreen = 1
android.permissions = CAMERA,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,FOREGROUND_SERVICE,RECEIVE_BOOT_COMPLETED,VIBRATE,RECORD_AUDIO
android.minapi = 21
android.target = 33
android.ndk = 25b
android.api = 33
android.archs = arm64-v8a,armeabi-v7a
android.enable_androidx = 1
android.useandroidx = 1
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.1,androidx.swiperefreshlayout:swiperefreshlayout:1.1.0
android.compile_options = sourceCompatibility=1.8 targetCompatibility=1.8
android.allow_backup = 1
android.logcat_filters = *:S python:D

# Java classes or jars to add to the classpath (comma separated)
# android.add_jars =

# Android services to add (comma separated)
# android.services =

# Presplash background color (hex format, eg #FFFFFF)
# presplash.color = #FFFFFF

# Presplash image
# presplash.filename = %(source.dir)s/data/presplash.png

# Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# Supported orientations (portrait, landscape, sensor)
# orientation = portrait

# Entry point of the application
entrypoint = main.py

# (str) Application theme, supported themes are: "@android:style/Theme.NoTitleBar", "@android:style/Theme.NoTitleBar.Fullscreen", "@android:style/Theme.Black", "@android:style/Theme.Light"
# android.theme = @android:style/Theme.NoTitleBar.Fullscreen

# Additional Java .jar files to add to the build (comma-separated)
# android.add_jars =

# Android add source folders
# android.add_src =

# (list) List of Gradle dependencies to add to gradle.build
# android.gradle_dependencies =

# (list) Permissions to be requested on install (will be automatically added if android.permissions is not empty)
# android.permissions =

# (list) List of permissions to require only when the app is used in foreground (Android 10+)
android.foreground_permissions = CAMERA,RECORD_AUDIO

# Set this to True if using android.newer_sdk (API 30+)
android.newer_sdk = True

# Android extra manifests
# android.add_manifest_xml = ./templates/manifest.xml

# Don't compress these file extensions
android.keep_extensions = .jpg,.png,.xml,.mp3,.wav,.ogg

# Include *.so libraries
android.include_exts = so

# Android services to be declared in AndroidManifest.xml
# android.services =

# Environment variables passed to python-for-android
# android.environment =

# Workaround to avoid app crash with OpenCV or large camera features
android.extra_args = --copy-libs

# Do not strip debug symbols
android.strip_debug = False

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (str) Custom source folders for code
# source.include_exts = py,png,jpg,kv,atlas,json,ttf,ttc,otf,xml,mp3,wav,ogg
