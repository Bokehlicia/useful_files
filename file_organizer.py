import os
import shutil

def organize_files_by_type():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all files in the current directory
    files = os.listdir(current_directory)

    # Create directories for each file type
    image_dir = os.path.join(current_directory, "images")
    video_dir = os.path.join(current_directory, "videos")
    document_dir = os.path.join(current_directory, "documents")
    music_dir = os.path.join(current_directory, "music")
    program_dir = os.path.join(current_directory, "programs")
    font_dir = os.path.join(current_directory, "fonts")

    for dir_path in [image_dir, video_dir, document_dir, music_dir, program_dir, font_dir]:
        os.makedirs(dir_path, exist_ok=True)

    # Define file extensions for each category
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg"]
    video_extensions = [".mp4", ".avi", ".mkv", ".mov", ".wmv"]
    document_extensions = [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".zip"]
    music_extensions = [".mp3", ".wav", ".flac", ".aac", ".ogg"]
    program_extensions = [".exe", ".msi", ".app", ".deb"]
    font_extensions = [".ttf", ".otf", ".woff", ".woff2", ".eot", ".pfb", ".pfm", ".svg", ".bdf", ".pcf", ".afm", ".crf"]

    # Organize files based on their extensions
    for file in files:
        _, extension = os.path.splitext(file.lower())

        if extension in image_extensions:
            shutil.move(file, os.path.join(image_dir, file))
        elif extension in video_extensions:
            shutil.move(file, os.path.join(video_dir, file))
        elif extension in document_extensions:
            shutil.move(file, os.path.join(document_dir, file))
        elif extension in music_extensions:
            shutil.move(file, os.path.join(music_dir, file))
        elif extension in program_extensions:
            shutil.move(file, os.path.join(program_dir, file))
        elif extension in font_extensions:
            shutil.move(file, os.path.join(font_dir, file))

    print("Organized files in the current directory.")

# Example usage:
organize_files_by_type()