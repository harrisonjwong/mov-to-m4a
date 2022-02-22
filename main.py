import os

import moviepy.editor as mp

if __name__ == '__main__':
    for entry in os.scandir('in'):
        original_path = entry.path
        if '.DS_Store' in original_path:
            continue
        split_path = original_path.split('/')  # ['in', 'IMG_9927_20210101.mov']]
        img_name = split_path[1]  # IMG_9927_20210101.mov
        img_name_split = img_name.split('.')  # ['IMG_9927_20210101', 'mov']
        img_name_no_mov = img_name_split[0]  # IMG_9927_20210101
        new_filename = 'out/%s.m4a' % img_name_no_mov  # out/IMG_9927_20210101.m4a
        # print(new_filename)
        clip = mp.VideoFileClip(original_path)
        clip.audio.write_audiofile(new_filename, codec='aac')
