#!/bin/bash

ffmpeg -y -i FPS_test_1080p50_L4.2.mkv -ac 2 -ab 128k -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 2000k -maxrate 2000k -bufsize 1500k -vf "scale=-1:1080" outputfile1080.mp4
ffmpeg -y -i FPS_test_1080p50_L4.2.mkv -ac 2 -ab 128k -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 1500k -maxrate 1500k -bufsize 1000k -vf "scale=-1:720" outputfile720.mp4

ffmpeg -y -i FPS_test_1080p50_L4.2.mkv -ac 2 -ab 128k -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 800k -maxrate 800k -bufsize 500k -vf "scale=-1:540" outputfile540.mp4

ffmpeg -y -i FPS_test_1080p50_L4.2.mkv -ac 2 -ab 128k -c:v libx264 -x264opts 'keyint=24:min-keyint=24:no-scenecut' -b:v 400k -maxrate 400k -bufsize 400k -vf "scale=-1:360" outputfile360.mp4

MP4Box -dash 5000 -rap -frag-rap -profile dashavc264:live -out dashed outputfile360.mp4#video outputfile1080.mp4#video

#MP4Box -dash 5000 -rap -frag-rap -profile dashavc264:live -out dashed outputfile360.mp4#video outputfile540.mp4#video outputfile720.mp4#video outputfile1080.mp4#video
