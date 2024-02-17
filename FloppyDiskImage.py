import os
import subprocess
import sys

def create_floppy_image(image_path):
    # Define the size of a standard high-density floppy disk
    size = 1440 * 1024  # 1.44 MB

    if os.name == 'nt':  # Windows
        try:
            subprocess.run(['fsutil', 'file', 'createnew', image_path, str(size)], check=True)
            print(f"Blank floppy disk image created at {image_path}")

            # print("Please use a third-party tool to format the floppy disk image.")

        except subprocess.CalledProcessError:
            print("Failed to create floppy disk image. Make sure you have the necessary permissions.")
    elif os.name == 'posix':  # Linux/macOS
        try:
            subprocess.run(['dd', 'if=/dev/zero', f'of={image_path}', 'bs=512', 'count=2880'], check=True)
            print(f"Blank floppy disk image created at {image_path}")
            format_floppy_image(image_path)  # Format the floppy disk image after creation
        except subprocess.CalledProcessError:
            print("Failed to create floppy disk image. Make sure you have the necessary permissions.")
    else:
        print("Unsupported operating system.")

def format_floppy_image(image_path):
    try:
        # Format the disk image with FAT12 file system using mkfs.fat
        subprocess.run(['mkfs.fat', '-F', '12', image_path], check=True)
        print(f"Floppy disk image formatted with FAT12 file system at {image_path}")
    except subprocess.CalledProcessError:
        print("Failed to format floppy disk image. Make sure mkfs.fat is installed and you have the necessary permissions.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_floppy.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        create_floppy_image(image_path)
