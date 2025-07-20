"""File handling utilities for the file organizer."""
import os
from pathlib import Path
from typing import Tuple

def get_file_type(file_path: str) -> str:
    """
    Determine file type based on its extension.
    
    Args:
        file_path: Path to the file or filename
        
    Returns:
        str: File category (e.g., 'Documentos/PDF', 'Imágenes', etc.)
    """
    extension = Path(file_path).suffix.lower()
    file_types = {
        # Documents
        '.pdf': 'Documentos/PDF',
        '.doc': 'Documentos/Word',
        '.docx': 'Documentos/Word',
        '.xls': 'Documentos/Excel',
        '.xlsx': 'Documentos/Excel',
        '.ppt': 'Documentos/PowerPoint',
        '.pptx': 'Documentos/PowerPoint',
        '.txt': 'Documentos/Texto',
        # Images
        '.jpg': 'Imágenes',
        '.jpeg': 'Imágenes',
        '.png': 'Imágenes',
        '.gif': 'Imágenes',
        '.bmp': 'Imágenes',
        # Music
        '.mp3': 'Música',
        '.wav': 'Música',
        '.flac': 'Música',
        # Videos
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mov': 'Videos',
        '.mkv': 'Videos',
        # Archives
        '.zip': 'Comprimidos',
        '.rar': 'Comprimidos',
        '.7z': 'Comprimidos',
        # Programs
        '.exe': 'Programas',
        '.msi': 'Programas',
    }
    return file_types.get(extension, 'Otros')

def create_unique_filepath(directory: str, filename: str) -> Tuple[str, str]:
    """
    Create a unique filename in the specified directory.
    
    Args:
        directory: Directory where file will be created
        filename: Original filename
        
    Returns:
        Tuple of (full_path, new_filename)
    """
    base_name = Path(filename).stem
    extension = Path(filename).suffix
    counter = 1
    
    os.makedirs(directory, exist_ok=True)
    
    new_path = os.path.join(directory, filename)
    if not os.path.exists(new_path):
        return new_path, filename
    
    # Add number suffix if file exists
    while True:
        new_filename = f"{base_name}_{counter}{extension}"
        new_path = os.path.join(directory, new_filename)
        if not os.path.exists(new_path):
            return new_path, new_filename
        counter += 1
