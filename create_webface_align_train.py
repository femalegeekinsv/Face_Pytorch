import os

with open('webface_align_train.list', 'w') as f:
    root_path = "webface_align_112"
    for index, current_dir in enumerate(os.listdir(root_path)):
        for file in os.listdir(os.path.join(root_path, current_dir)):
            f.write(os.path.join(current_dir, file) + " " + str(index) + "\n")
