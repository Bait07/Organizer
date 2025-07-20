"""Main window module for the file organizer application."""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import Callable

class MainWindow:
    """Main GUI window for the file organizer application."""
    
    def __init__(self, root: tk.Tk, on_organize: Callable[[str, Callable], None]):
        """Initialize the main window.
        
        Args:
            root: Tk root instance
            on_organize: Callback function for the organize button
        """
        self.root = root
        self.on_organize = on_organize
        self.setup_ui()
    
    def setup_ui(self) -> None:
        """Set up the user interface elements."""
        self.root.title("Organizador de Archivos")
        self.root.geometry("500x200")
        
        # UI variables
        self.folder_path = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(
            main_frame, 
            text="Organizador de Archivos", 
            font=('Arial', 14, 'bold')
        ).pack(pady=(0, 10))
        
        # Folder selection
        folder_frame = ttk.Frame(main_frame)
        folder_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(folder_frame, text="Carpeta a organizar:").pack(side=tk.LEFT)
        ttk.Entry(
            folder_frame, 
            textvariable=self.folder_path, 
            width=50
        ).pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        ttk.Button(
            folder_frame, 
            text="Examinar", 
            command=self.browse_folder
        ).pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame, 
            variable=self.progress_var, 
            maximum=100, 
            length=400
        )
        self.progress.pack(pady=10, fill=tk.X)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.pack(pady=(0, 10))
        
        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack()
        
        self.organize_btn = ttk.Button(
            btn_frame, 
            text="Comenzar", 
            command=self.start_organizing
        )
        self.organize_btn.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            btn_frame, 
            text="Salir", 
            command=self.root.quit
        ).pack(side=tk.LEFT, padx=5)
    
    def browse_folder(self) -> None:
        """Open a dialog to select a folder."""
        folder = tk.filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
    
    def update_progress(self, progress: int, filename: str) -> None:
        """Update progress bar and status.
        
        Args:
            progress: Progress percentage (0-100).
            filename: Current file being processed.
        """
        self.progress_var.set(progress)
        self.status_label.config(text=f"Processing: {filename}")
        self.root.update_idletasks()
    
    def start_organizing(self) -> None:
        """Start the file organization process."""
        folder_path = self.folder_path.get()
        
        if not folder_path:
            messagebox.showwarning(
                "Warning", 
                "Please select a folder first."
            )
            return
            
        if not tk.messagebox.askyesno(
            "Confirm", 
            f"Organize files in {folder_path}?"
        ):
            return
        
        # Disable button during operation
        self.organize_btn.config(state=tk.DISABLED)
        
        # Call organize function in main thread after a short delay
        self.root.after(100, lambda: self.on_organize(folder_path, self.on_organize_complete))
    
    def on_organize_complete(self, success: bool, message: str = "") -> None:
        """Called when file organization completes.
        
        Args:
            success: Whether the operation was successful.
            message: Optional message to display.
        """
        self.organize_btn.config(state=tk.NORMAL)
        
        if success:
            messagebox.showinfo("Success", "Files organized successfully!")
            self.progress_var.set(0)
            self.status_label.config(text="")
        elif message:
            messagebox.showerror("Error", message)
