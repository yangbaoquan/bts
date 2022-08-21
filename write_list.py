import os

train_list = open("./train_list.txt", "a")

for s in ["slice4", "slice5", "slice6"]:
    for i in range(12):
        for c in ["c0", "c1"]:
            cur_folder = os.path.join(s, "env" + str(i).zfill(2), c, "images")
            depth_folder = os.path.join(s, "env" + str(i).zfill(2), c, "depth_maps")
            if os.path.exists(cur_folder):
                for img_name in sorted(os.listdir(cur_folder)):
                    assert os.path.exists(os.path.join(depth_folder, img_name.split('.')[0] + '.png'))
                    train_list.write(os.path.join(cur_folder, img_name))
                    train_list.write(' ')
                    train_list.write(os.path.join(depth_folder, img_name.split('.')[0] + '.png'))
                    train_list.write('\n')
