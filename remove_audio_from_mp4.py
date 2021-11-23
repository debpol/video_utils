# -*- coding: utf-8 -*-
"""

FFREPORT=file="/path/input_file-%p-%t.log" ffmpeg -i input_file.MP4 -map_metadata 0 -map 0:0 -c:a copy output_video_file_sinAudio.mp4 -report

FFREPORT sets up path directory to save .log file

ffmpeg -i shows the info

-map_metadata 0 keeps metadata: date and hour of creation from original file 

-map 0:0 -c:a copy makes the copy from input_file to output_video_file

"""
"""
You must to have intalled ffmpeg (https://www.ffmpeg.org/) tool in your OS (operating system)

You must to set up path: input_directory , output_directory

It version works only for .mp4 file extension videos
"""
import time
import os
import shutil
#os.getcwd()

folder_name_to_process= "namefolder"

input_directory='/.../videos_con_audio/' + folder_name_to_process
output_directory='/.../videos_sin_audio/'+ folder_name_to_process
output_info_file= folder_name_to_process +"_info.txt"

if (not os.path.exists(output_directory)):
    os.mkdir(output_directory)

files_list = os.listdir(input_directory)
os.chdir(input_directory)

for file in files_list:
    
    if (file.lower().endswith('.mp4')):
        print(file)
        
        orginal_lower_filename_whitout_ext = file.lower().split(".mp4")[0]
        new_filename =  output_directory + "/" + orginal_lower_filename_whitout_ext +"_withoutAudio.mp4"
        log_file = output_directory + "/" +  "{output_video_file}-%p-%t.log".format(output_video_file=orginal_lower_filename_whitout_ext)
        ffmpeg_command= "FFREPORT=file={log_file} ffmpeg -i {input_file} -map_metadata 0 -map 0:0 -c:a copy {output_video_file} -report".format(log_file= log_file, input_file = file, output_video_file=new_filename)
        #print(ffmpeg_command)
        os.system(ffmpeg_command)
        ffmpeg_info_command ="ffmpeg -i {video_file} 2>&1 | tee -a {output_info_file}".format(video_file= input_directory + "/" + file, output_info_file = output_directory +"/"+output_info_file)
        #print(ffmpeg_info_command)
        os.system(ffmpeg_info_command)
        ffmpeg_info_command ="ffmpeg -i {video_file} 2>&1 | tee -a {output_info_file}".format(video_file= new_filename, output_info_file = output_directory +"/"+output_info_file)
        #print(ffmpeg_info_command)
        os.system(ffmpeg_info_command)
        #duerme 4 minutos para darle descanso al CPU
        time.sleep(300)
        
    else:
        print(file + " it isnt a .mp4 file... copiying without modifications ")
        shutil.copy2(input_directory + "/" +  file, output_directory + "/" +  file)
        
