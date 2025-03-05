import timeit
start = timeit.default_timer()
import json
import os
import scene_split
import text_to_img
import shutil

with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read()

def clear_story_folder(folder_path="story"):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

clear_story_folder()
scenes = scene_split.main(story,0.7)
print("Scenes splitted successfully!")
# print(scenes)
# for i in scenes:
#     print(i[0])

# Scenes to prompt
# print(scenes)
number_of_scenes = len(scenes)
print(f"Number of scenes: {number_of_scenes}")

print("\n")
image_type = input("Enter the type of image you want to generate (realistic, cartoon, abstract): ")
print("\n")

for i, scene in enumerate(scenes, 1):
    prompt = f"Make a {image_type} image of" + scene
    # print(prompt)
    text_to_img.main(prompt, f"story/image-{i}")

# Folder and File name generation
story_dict = {f"story/image-{i}.png": line for i, line in enumerate(scenes, 1)}

with open("story.json", "w") as f:
    json.dump(story_dict, f, indent=4)

end = timeit.default_timer()
print(f"Time taken: {end-start} seconds")

import slideshow