import os
import shutil


def backup_folders(source_root, backup_dir):
    for root, dirs, files in os.walk(source_root):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            # Getting relative path of the folder
            relative_path_fold = root.replace(source_root, '') + os.sep + dir
            relative_path_backup = backup_dir + relative_path_fold

            # boolean check if relative path exists
            is_relative = os.path.exists(relative_path_backup)

            if is_relative:
                pass
            else:
                shutil.copytree(dir_path, relative_path_backup)


def backup_files(source_root, backup_dir):
    for root, dirs, files in os.walk(source_root):
        for filename in files:
            relative_path_file = root.replace(source_root, '') + os.sep + filename
            file_path_backup = backup_dir + relative_path_file

            file_path_real = os.path.join(root, filename)
            file_path_back = os.path.join(file_path_real, file_path_backup)

            # time of modification of the original file
            mod_time_orig = os.stat(file_path_real).st_mtime
            # time of modification of backup file
            mod_time_backup = os.stat(file_path_back).st_mtime

            if filename not in os.listdir(backup_dir):
                new_path = shutil.copy(file_path_real, file_path_backup)
                os.utime(new_path, (mod_time_orig, mod_time_orig))

            elif mod_time_orig != mod_time_backup:
                new_path = shutil.copy(file_path_real, file_path_backup)
                os.utime(new_path, (mod_time_orig, mod_time_orig))
            else:
                print('everything is ok, time set correctly')


origin = r'/home/driver220/Documents/'
backup_dir = r'/home/driver220/Downloads/'
backup_folders(origin, backup_dir)
backup_files(origin, backup_dir)
print('backup complete sucessfully')
