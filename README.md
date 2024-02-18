README for Floppy Image

This Python script provides a simple command-line interface for creating and optionally formatting a floppy disk image. It supports both Unix-like (Linux, macOS) and Windows operating systems. The tool creates a blank, unformatted floppy disk image of size 1.44 MB, which can then be optionally formatted with a FAT12 filesystem.

Features
    Create a Blank Floppy Disk Image: Creates an unformatted floppy disk image file.
    Optional Formatting: Formats the created floppy disk image with a FAT12 filesystem.
    Cross-Platform Compatibility: Works on Windows, macOS, and Linux.

Requirements
    Python 3.x installed on your system.
    Appropriate permissions to execute file system commands.
    macOS Users: Installation of Homebrew and dosfstools is required. Follow the instructions below to set up your environment.

Additional Setup for macOS
  Before running the script on macOS, you need to install Homebrew (a package manager for macOS) and dosfstools (to enable FAT12 filesystem formatting). Use the following commands in the terminal:

    Install Command Line Tools for Xcode
    sudo xcode-select --install

    Install Homebrew:
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    Install dosfstools:
    brew install dosfstools

    Setting up your Path:
    sudo echo 'export PATH="/opt/homebrew/sbin:$PATH"' >> ~/.zshrc 
    sudo echo 'export PATH="/opt/homebrew/sbin:$PATH"' >> ~/.bash_profile
    Close terminal and reopen

    Check your system is ready to brew:
    brew doctor

Installation
    No installation is required. Simply download the script and run it with Python. Ensure you have Python 3.x installed on your system.

Usage
  To use this script, navigate to the directory where the script is located and run it from the command line. The script accepts the following arguments:
    image_path: The file path where the floppy disk image will be created. This argument is required.
    --format: An optional flag that, when included, formats the floppy disk image after creation.

Examples
  Creating an Unformatted Floppy Disk Image:
  python <script_name>.py /path/to/floppy.img

  Creating and Formatting a Floppy Disk Image:
  python <script_name>.py /path/to/floppy.img --format

    Replace <script_name> with the name of the script file and /path/to/floppy.img with your desired path and filename for the floppy disk image.

Logging
  The script provides informative log messages about the process, including success messages and error diagnostics in case of failures.

Error Handling
  Errors during the creation or formatting process will terminate the script with an error message detailing the cause of the failure.

Support
  For issues, questions, or contributions, please refer to the repository's issues section or submit a pull request.

License
  This script is provided "as is", without warranty of any kind, express or implied. Please review the source code for license details if applicable.

This README provides an overview of how to use the script. Make sure to adjust the usage instructions based on the actual name of the script file when you download or clone it to your local machine.