"""Core functionality for file organization by type and date."""
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Callable

from utils.file_utils import get_file_type, create_unique_filepath

class FileOrganizer:
    """Organizes files into folders by type and modification date."""
    
    def __init__(self, progress_callback: Optional[Callable[[int, str], None]] = None):
        """Initialize with optional progress callback."""
        self.progress_callback = progress_callback or (lambda p, f: None)
    
    def organize_files(self, folder_path: str) -> None:
        """
        Organize files in the specified folder.
        
        Args:
            folder_path: Path to folder containing files to organize.
            
        Raises:
            FileNotFoundError: If folder doesn't exist.
            NotADirectoryError: If path is not a directory.
        """
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder does not exist: {folder_path}")
            
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"Path is not a directory: {folder_path}")
        
        # Get list of files (only files, not directories)
        files = [f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f))]
        
        total_files = len(files)
        if total_files == 0:
            return
        
        for index, filename in enumerate(files, 1):
            file_path = os.path.join(folder_path, filename)
            
            try:
                mod_time = os.path.getmtime(file_path)
                date_modified = datetime.fromtimestamp(mod_time)
                year_month = date_modified.strftime('%Y-%m')
                
                file_type = get_file_type(filename)
                dest_folder = os.path.join(folder_path, file_type, year_month)
                os.makedirs(dest_folder, exist_ok=True)
                
                # Move file (handles duplicates)
                dest_path, _ = create_unique_filepath(dest_folder, filename)
                os.rename(file_path, dest_path)
                
                progress = int((index / total_files) * 100)
                self.progress_callback(progress, filename)
                
            except Exception as e:
                # Continuar con el siguiente archivo si hay un error
                print(f"Error processing {filename}: {str(e)}")
                continue
