# StartUp Voice Script

## Overview

This project provides a simple script (`start_voice.py`) that plays a startup voice message based on the time of day. The script is designed to run at system startup.

## Features

- **Regular Voice:** Plays a predefined voice message based on the time of day (morning, afternoon, night).

- **Custom Voice:** Users can provide their own voice recording to be played at startup.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Additional Python packages (`pyttsx3` and `pydub`)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/InemesitMatthew/startup-voice.git
   cd startup-voice
   ```

2. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create Executable (Optional):**
   If you prefer to use an executable, create it using `pyinstaller`:
   ```bash
   pyinstaller --onefile start_voice.py
   ```

4. **Task Scheduler Setup (Windows):**
   - Open Task Scheduler.
   - Create a new task.
   - Set the trigger to "At startup."
   - In the Actions tab, specify the path to either `start_voice.py` or the generated executable (if used).

5. **Startup Entry (Linux/macOS):**
   - For Linux, create a desktop entry or use a tool like `gnome-session-properties` to add the script to startup applications.
   - For macOS, use Automator to create an application that runs the script and add it to login items.

## Usage

### StartUp Voice Script:

```bash
python start_voice.py
```

## Troubleshooting

If the script is not working as expected, refer to the troubleshooting section in the README for guidance.

## Contributing

Feel free to contribute by opening issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---
