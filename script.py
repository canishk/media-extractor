import os
import shutil

class FileManager:
    def __init__(self):
        self.source_dir = r"C:\Users\user\Downloads\Photos_Backup\Takeout\Google Photos"
        self.destination_dir = r"C:\Users\user\OneDrive\Documents\photos"
        self.image_extensions = ('.png', '.jpg', '.jpeg', '.gif')
        self.video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
    

    def copy_files(self):
        allowed_extensions = self.image_extensions + self.video_extensions
        print(f"Copying files from {self.source_dir} to {self.destination_dir}")
        media_files = []
        for root, dirs, files in os.walk(self.source_dir):
            print(f"Checking directory: {root}")
            if not files:
                print("No files found in this directory.")
                continue
            print(f"Files found: {files}")
            # Filter files based on allowed extensions
            for f in files:
                print(f.lower().endswith(allowed_extensions))
                if f.lower().endswith(allowed_extensions):
                    print(f"File {f} is a media file.")
                    media_files.append(f)
            if media_files:
                relative_path = os.path.relpath(root, self.source_dir)
                dest_path = os.path.join(self.destination_dir, relative_path)
                os.makedirs(dest_path, exist_ok=True)
                print(f"Found {len(media_files)} media files to copy.")
                for file in media_files:
                    print(f"Processing file: {file}")
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_path, file)
                    
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dest_file):
                        dest_file = os.path.join(dest_path, f"{base}_{counter}{ext}")
                        counter += 1
                    if not os.path.exists(src_file):
                        print(f"Source file does not exist, skipping: {src_file}")
                        continue
                    try:
                        shutil.copy2(src_file, dest_file)
                        print(f"Copied: {src_file} to {dest_file}")
                    except Exception as e:
                        print(f"Failed to copy {src_file} to {dest_file}: {e}")

    def run(self):
        if not os.path.exists(self.source_dir):
            print(f"Source directory does not exist: {self.source_dir}")
            return
        if not os.path.exists(self.destination_dir):
            print(f"Destination directory does not exist, creating: {self.destination_dir}")
            os.makedirs(self.destination_dir)
        self.copy_files()
        print("File copying completed.")


if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.run()
        