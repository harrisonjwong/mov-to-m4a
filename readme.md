# mov-to-m4a


A short python script to convert movie files to audio files.

### Story

I had taken some videos on my iPhone that I only needed for the audio. They should have been voice memos instead. 
Curiously, there is no way to turn videos into voice memos in iOS.

The manual way to do this process was to "export" a .mov from Photos.app on Mac,
then drag it into iMovie, 
then export it to an audio file with the name of my choosing.
Unfortunately, this took 2-3 minutes per movie.

So, I wrote this script to partially automate this process.

This readme is for my memory in case I need to use it again.

### Directions

It assumes a directory in the project level called `in` that contains files in the pattern of `IMG_0000.mov`. 

It assumes a directory in the project level called `out` that will contain the finished audio files, which will be named `IMG_0000.m4a`.

The program will scan all the files in the `/in` directory and then dump them with the same name in the `/out` folder.

### Notes

* Had to solve some error with encoding - the `codec='aac'` portion seemed to solve it.
* Had a DS_Store ruin my day - there is an if that avoids it now.

### Dependencies

* Python 3.9
* moviepy
* Stack Overflow post that actually does all the magic:
  * https://stackoverflow.com/questions/33448759/python-converting-video-to-audio

### Future

* I couldn't figure out how to grab the metadata to get the date/time from the video file. Oh well.