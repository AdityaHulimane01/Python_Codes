import shutil
import os

# ------------------------------
# 1. shutil.copy()
# Copies a file from source to destination
# Only copies file data and permission
# ------------------------------
shutil.copy("source.txt", "copy_source.txt")


# ------------------------------
# 2. shutil.copy2()
# Copies file along with metadata
# (timestamps, permissions, etc.)
# ------------------------------
shutil.copy2("source.txt", "copy_with_metadata.txt")


# ------------------------------
# 3. shutil.copyfile()
# Copies file content only
# Source and destination must be files
# ------------------------------
shutil.copyfile("source.txt", "copyfile_example.txt")


# ------------------------------
# 4. shutil.copyfileobj()
# Copies data between file objects
# ------------------------------
with open("source.txt", "rb") as fsrc:
    with open("copy_obj.txt", "wb") as fdst:
        shutil.copyfileobj(fsrc, fdst)


# ------------------------------
# 5. shutil.copytree()
# Copies an entire directory tree
# ------------------------------
shutil.copytree("source_folder", "destination_folder")


# ------------------------------
# 6. shutil.move()
# Moves a file or directory
# ------------------------------
shutil.move("copy_source.txt", "moved_source.txt")


# ------------------------------
# 7. shutil.rmtree()
# Deletes an entire directory tree
# ------------------------------
# shutil.rmtree("destination_folder")


# ------------------------------
# 8. shutil.disk_usage()
# Shows disk usage of a path
# ------------------------------
total, used, free = shutil.disk_usage("C:\\")

print("Total:", total)
print("Used:", used)
print("Free:", free)


# ------------------------------
# 9. shutil.make_archive()
# Creates a zip archive of a folder
# ------------------------------
shutil.make_archive("backup", "zip", "source_folder")


# ------------------------------
# 10. shutil.unpack_archive()
# Extracts archive files
# ------------------------------
shutil.unpack_archive("backup.zip", "extracted_files")


# ------------------------------
# 11. shutil.which()
# Finds path of an executable program
# ------------------------------
print("Python executable path:", shutil.which("python"))