import subprocess
import sys
import logging
from argparse import ArgumentParser

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_floppy_image(image_path, format_image=False):
    """
    Creates a blank, unformatted floppy disk image at the specified path and optionally formats it.
    """
    size = 1440 * 1024  # 1.44 MB
    os_specific_commands = {
        'win32': ['fsutil', 'file', 'createnew', image_path, str(size)],
        'unix': ['dd', 'if=/dev/zero', f'of={image_path}', 'bs=512', 'count=2880']
    }

    try:
        if sys.platform.startswith('win32'):
            subprocess.run(os_specific_commands['win32'], check=True, stderr=subprocess.PIPE)
        elif sys.platform.startswith(('darwin', 'linux')):
            subprocess.run(os_specific_commands['unix'], check=True, stderr=subprocess.PIPE)
        else:
            raise ValueError("Unsupported operating system.")
        
        logging.info(f"Blank unformatted floppy disk image created at {image_path}")
        if format_image:
            format_floppy_image(image_path)
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to create unformatted floppy disk image: {e.stderr.decode()}")
        raise RuntimeError(f"Failed to create unformatted floppy disk image: {e}")
    except ValueError as e:
        logging.error(e)
        raise


def format_floppy_image(image_path):
    """
    Formats the floppy disk image with FAT12 filesystem. Adjust as you need.
    """
    os_format_commands = {
        'win32': ['mkfs.fat', '-F', '12', image_path],
        'darwin': ['/opt/homebrew/sbin/mkfs.fat', '-F', '12','-n', 'Floppy', image_path],
        'linux': ['mkfs.fat', '-F', '12', '-n', 'Floppy', image_path]
    }

    try:
        if sys.platform.startswith('win32'):
            subprocess.run(os_format_commands['win32'], check=True)
        elif sys.platform.startswith('darwin'):
            subprocess.run(os_format_commands['darwin'], check=True)
        elif sys.platform.startswith('linux'):
            subprocess.run(os_format_commands['linux'], check=True)
        else:
            raise ValueError("Unsupported operating system.")
        logging.info(f"Formatted floppy disk image at {image_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to format floppy disk image: {e.stderr.decode()}")
        raise RuntimeError(f"Failed to format floppy disk image: {e}")


def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = ArgumentParser(description="Create and optionally format a floppy disk image.")
    parser.add_argument("image_path", help="The file path where the floppy disk image will be created.")
    parser.add_argument("--format", action="store_true", help="Format the floppy disk image after creation.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    create_floppy_image(args.image_path, args.format)


if __name__ == "__main__":
    main()

