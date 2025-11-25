"""
UI Components Module
Reusable UI components and widgets for the Learning Management System
"""

import tkinter as tk
from config import COLORS, FONTS


def create_modern_button(parent, text, command, bg_color, width=20, height=2, icon=""):
    """Create a modern styled button with hover effects"""
    btn_frame = tk.Frame(parent, bg=parent['bg'])

    button_text = f"{icon} {text}" if icon else text

    btn = tk.Button(
        btn_frame,
        text=button_text,
        command=command,
        font=FONTS['button'],
        bg=bg_color,
        fg='white',
        activebackground=bg_color,
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        width=width,
        height=height,
        borderwidth=0
    )
    btn.pack(padx=2, pady=2)

    # Hover effects
    def on_enter(e):
        btn.config(bg=COLORS.get(bg_color + '_dark', bg_color))

    def on_leave(e):
        btn.config(bg=bg_color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn_frame


def create_dashboard_card(parent, icon, title, description, color, command):
    """Create a modern dashboard card"""
    card = tk.Frame(
        parent,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1,
        cursor='hand2'
    )

    card_content = tk.Frame(card, bg=COLORS['bg_primary'])
    card_content.pack(padx=30, pady=30, fill='both', expand=True)

    # Icon
    tk.Label(
        card_content,
        text=icon,
        font=('Segoe UI', 48),
        bg=COLORS['bg_primary']
    ).pack(pady=(0, 15))

    # Title
    tk.Label(
        card_content,
        text=title,
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(pady=(0, 10))

    # Description
    tk.Label(
        card_content,
        text=description,
        font=FONTS['body'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary'],
        wraplength=250
    ).pack(pady=(0, 20))

    # Button
    btn = tk.Button(
        card_content,
        text="Get Started →",
        command=command,
        font=FONTS['button'],
        bg=color,
        fg='white',
        activebackground=color,
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=10,
        borderwidth=0
    )
    btn.pack()

    # Hover effects
    def on_enter(e):
        card.config(highlightbackground=color, highlightthickness=2)
        btn.config(bg=COLORS.get(color + '_dark', color))

    def on_leave(e):
        card.config(highlightbackground=COLORS['border'], highlightthickness=1)
        btn.config(bg=color)

    card.bind("<Enter>", on_enter)
    card.bind("<Leave>", on_leave)
    card_content.bind("<Enter>", on_enter)
    card_content.bind("<Leave>", on_leave)

    return card


def create_scrollable_frame(parent, bg_color=None):
    """Create a scrollable frame with canvas and scrollbar"""
    if bg_color is None:
        bg_color = COLORS['bg_secondary']
    
    # Container
    container = tk.Frame(parent, bg=bg_color)
    
    # Canvas for scrolling
    canvas = tk.Canvas(container, bg=bg_color, highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    
    # Content frame inside canvas
    content = tk.Frame(canvas, bg=bg_color)
    
    # Configure canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack scrollbar and canvas
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    
    # Create window in canvas
    canvas_frame = canvas.create_window((0, 0), window=content, anchor="nw")
    
    # Configure scroll region when content changes
    def configure_scroll_region(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_frame, width=canvas.winfo_width())
    
    content.bind("<Configure>", configure_scroll_region)
    canvas.bind("<Configure>", configure_scroll_region)

    return container, content, canvas


def setup_mousewheel_scrolling(window, canvas):
    """Setup mousewheel scrolling for a canvas"""
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def bind_mousewheel(event=None):
        window.bind("<MouseWheel>", on_mousewheel)
        canvas.bind("<MouseWheel>", on_mousewheel)

    def unbind_mousewheel(event=None):
        window.unbind("<MouseWheel>")
        canvas.unbind("<MouseWheel>")

    # Bind when mouse enters the window
    window.bind("<Enter>", bind_mousewheel)
    window.bind("<Leave>", unbind_mousewheel)

    # Initial bind
    bind_mousewheel()


def center_window(window, width, height):
    """Center a window on the screen"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


def get_responsive_window_size(window, max_width, max_height, screen_percent=0.85):
    """Get responsive window size based on screen dimensions"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = min(max_width, int(screen_width * screen_percent))
    window_height = min(max_height, int(screen_height * screen_percent))

    return window_width, window_height

