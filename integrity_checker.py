import hashlib
import os
import json
import argparse

HASH_DB = "hash_database.json"

def calculate_hash(filepath):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_directory(directory):
    """Scan directory and return file:hash dictionary."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            rel_path = os.path.relpath(filepath, directory)
            file_hashes[rel_path] = calculate_hash(filepath)
    return file_hashes

def load_previous_hashes():
    if os.path.exists(HASH_DB):
        with open(HASH_DB, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_DB, "w") as f:
        json.dump(hashes, f, indent=4)

def compare_hashes(old, new):
    added = []
    removed = []
    changed = []

    for path in old:
        if path not in new:
            removed.append(path)
        elif old[path] != new[path]:
            changed.append(path)

    for path in new:
        if path not in old:
            added.append(path)

    return added, removed, changed

def main(directory):
    print(f"\n🔍 Scanning directory: {directory}")
    new_hashes = scan_directory(directory)
    old_hashes = load_previous_hashes()

    added, removed, changed = compare_hashes(old_hashes, new_hashes)

    print("\n📊 Comparison Results:")
    if added:
        print("➕ New files detected:")
        for f in added:
            print("   -", f)
    if removed:
        print("➖ Removed files:")
        for f in removed:
            print("   -", f)
    if changed:
        print("✏️ Modified files:")
        for f in changed:
            print("   -", f)

    if not (added or removed or changed):
        print("✅ No changes detected. All files are intact.")

    save_hashes(new_hashes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Integrity Checker using SHA256")
    parser.add_argument("directory", help="Directory to scan")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("❌ Error: The provided path is not a valid directory.")
    else:
        main(args.directory)
