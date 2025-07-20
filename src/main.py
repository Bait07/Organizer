"""Main entry point for the file organizer application."""
import tkinter as tk
import threading
from typing import Callable

from core.organizer import FileOrganizer
from gui.main_window import MainWindow

class Application:
    """Main application class coordinating UI and file organization logic."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.organizer = FileOrganizer(progress_callback=self.update_progress)
        self.setup_ui()
    
    def setup_ui(self) -> None:
        """Set up the main user interface."""
        self.main_window = MainWindow(
            root=self.root,
            on_organize=self.start_organizing
        )
    
    def start_organizing(self, folder_path: str, callback: Callable) -> None:
        """Start organization process in a separate thread."""
        def organize_thread():
            try:
                self.organizer.organize_files(folder_path)
                self.root.after(0, lambda: callback(True, ""))
            except Exception as e:
                self.root.after(0, lambda: callback(False, str(e)))
        
        thread = threading.Thread(target=organize_thread, daemon=True)
        thread.start()
    
    def update_progress(self, progress: int, filename: str) -> None:
        """Update progress in the UI."""
        self.root.after(0, self.main_window.update_progress, progress, filename)

def main():
    """Initialize and start the application."""
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
