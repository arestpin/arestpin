# USB Reconnaissance and Hijacking Tool , Made By "arestpin"

This tool is designed to perform reconnaissance on USB devices connected to a system and facilitate the hijacking of their contents. It lists the contents of a specified directory, identifies USB volumes, and copies their contents to a designated directory for further analysis.

## Features

- **Reconnaissance:** Automatically detects USB devices connected to the system.
- **Hijacking:** Copies the contents of identified USB volumes to a designated directory.
- **Counting Stolen Items:** Counts the number of stolen items from the hijacked USB volume.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/arestpin/arestpin/tree/main/usb-recon-hijack.git
    ```

2. Navigate to the directory:

    ```bash
    cd usb-recon-hijack
    ```

3. Open the script (`hijack.py`) in a text editor.

4. Replace all occurrences of `"asd"` with your Linux username.

5. Save and close the file.

6. Execute the script:

    ```bash
    python hijack.py
    ```

## Creating a Keyboard Shortcut (Optional)

To execute the script conveniently with a keyboard shortcut:

1. Open your system settings for keyboard shortcuts.

2. Add a new custom shortcut.

3. Set the command to `python /path/to/usb-recon-hijack/hijack.py`.

   Replace `/path/to/usb-recon-hijack` with the actual path to the directory where the script is located.

4. Assign a keyboard shortcut to it.

With this setup, you can simply press the assigned keyboard shortcut to execute the script without any visible commands. This makes the execution more discreet.

## Usage

1. Connect the USB device(s) to the system.
2. Run the script to perform reconnaissance and hijack the contents.
3. Check the "loot" directory for the stolen items.

## Disclaimer

This tool is provided for educational and informational purposes only. It should only be used on devices and data for which you have proper authorization and consent. The creators of this tool are not responsible for any misuse or unauthorized use of the tool.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.
