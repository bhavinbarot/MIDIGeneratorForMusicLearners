Here’s a more polished and professional README for your "MIDI Generator For Music Learners" project:

---

# MIDI Generator For Music Learners

## Overview

The **MIDI Generator For Music Learners** is a Python-based tool designed to assist music learners in practicing notes within specific scales. The project is particularly focused on Indian Classical Music and supports **10 different Thaats**, enabling learners to explore the intricacies of these traditional scales. 

By generating random melodies that adhere to a specific Thaat, this tool allows users to improve their ability to identify the Thaat by ear. Additionally, the melody generation ensures that the **1st** and **5th** notes are fixed to 'S' (Sa) and 'P' (Pa), respectively, while avoiding the Lower and Middle octaves.

This project is ideal for beginners who wish to deepen their understanding of Indian Classical Music and improve their ear training by practicing within a structured yet random framework.

## Features

- Supports **10 different Thaats** from Indian Classical Music.
- Generates **random notes** and **random melodies** adhering to the selected Thaat.
- Ensures the positioning of the **1st** and **5th** notes as 'S' (Sa) and 'P' (Pa).
- Generates **MIDI files** based on the provided notes and Thaat.
- Users can adjust the **tempo** of the generated melody.
- Simple, text-file based input for swaras (notes).

## Installation

1. Clone the repository or download the code files.
2. Ensure that you have Python installed (preferably version 3.6 or higher).
3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure you have the necessary libraries for MIDI file generation, such as `mido` or `python-rtmidi`.

## Usage

### Preparing Input

To generate a MIDI file, create a text file with the desired **swaras** (musical notes) in the format:

```text
S R G M
```

Where each letter represents a swara, such as:

- **S**: Sa (Shadja)
- **R**: Re (Rishabh)
- **G**: Ga (Gandhar)
- **M**: Ma (Madhyam)

You can also specify the **tempo** (speed) for your melody. In the input file, use the format:

```text
//Tempo//    1  1  1  1
//Notes//    S  R  G  M
```

- Adjust the tempo as needed. For example, `1 1 1 1` represents a steady tempo where each note has equal duration.

### Running the Code

After preparing the text file with your swaras and tempo, you can run the script to generate the corresponding MIDI file:

```bash
python generate_midi.py input_file.txt
```

The script will read the notes and tempo from the file and generate a MIDI file in the same directory.

### Customizing the Thaat

To generate notes based on a specific Thaat, modify the input file to include the name of the Thaat you wish to use:

```text
//Thaat//   Yaman
//Tempo//   1  1  1  1
//Notes//   S  R  G  M
```

You can choose from any of the supported Thaats, including **Yaman**, **Bhairav**, **Bageshree**, and others.

## Contributing

We welcome contributions to this project! If you'd like to contribute, please fork the repository and submit a pull request. If you find any issues or bugs, feel free to open an issue on GitHub.

