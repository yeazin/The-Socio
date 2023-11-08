"""
This file is responsible for 
    creating Log folders,

"""

import os
_log_folder_ = "logs"

# Check if folder does not already exist
if not os.path.exists(_log_folder_):
    os.mkdir(_log_folder_)
    print(f"Created folder '{_log_folder_}'.")
else:
    print(f"Folder '{_log_folder_}' already exists.")