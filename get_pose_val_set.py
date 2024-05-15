# %%
import os
import pandas as pd
from glob import glob

url_base = "http://localhost:8888"
csv_file_name = "/home/yinzi/yinzi_home/workspace/babyview_pose/to_sample_for_whisper.csv"
df = pd.read_csv(csv_file_name)

# %% extract val dataset
dataset_root_path = "/ccn2a/u/yinzi/babyview_20240507/"
val_set_save_path = "/ccn2a/u/yinzi/babyview_20240507/babyview_main_pose_val_set"
all_videos_file_path = list(df["full_paths"])
for i, video_file_path in enumerate(all_videos_file_path):
    filename = df.iloc[i]["filename"]
    # basename = filename.replace(".MP4", "")
    if not os.path.exists(dataset_root_path+video_file_path):
        print(f"not exist: {dataset_root_path+video_file_path}")
    start_time = df.iloc[i]['start_time']
    end_time = df.iloc[i]['end_time']
    frames_save_path = os.path.join(val_set_save_path, filename)
    # extract frames from video between start_time and end_time
    os.system(f"ffmpeg -y -i {dataset_root_path+video_file_path} -ss {start_time} -to {end_time} -r 30 -q:v 2 {frames_save_path}/%04d.jpg")

# %%
