*COMPANY*: CODTECHIT SOLUTIONS

*NAME*: SHAH MEGH BHAVINKUMAR

*INTERN ID*: CT04DL906

*DOMAIN*: CYBERSECURITY AND ETHICAL HACKING

*DURATION*: 1 MONTH

*MENTOR*: NEELA SANTHOSH KUMAR

# File Integrity Checker

This project provides a simple command-line tool to check the integrity of files in a directory using SHA256 hashes.

## Features

- Scans a directory and computes SHA256 hashes for all files.
- Compares current file hashes with previously saved hashes in `hash_database.json`.
- Detects added, removed, and modified files.
- Updates the hash database after each scan.

## Usage

1. **Run the integrity checker:**

   ```sh
   python integrity_checker.py test_files
   ```

   Replace `test_files` with the path to the directory you want to scan.

2. **Output:**
   
   ![Image](https://github.com/user-attachments/assets/12aa1c78-f5a2-4266-81e5-f122c58f32fc)


## Files

- [`integrity_checker.py`](integrity_checker.py): Main script for scanning and checking file integrity.
- [`hash_database.json`](hash_database.json): Stores SHA256 hashes of files.
- [`test_files/`](test_files/): Example directory with test files.

## Requirements

- Python 3.8 or higher

## License

MIT License
