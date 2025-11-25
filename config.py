"""
Configuration and Constants for the Learning Management System
Contains all configuration settings, colors, fonts, and global constants
"""

import os

# ==================== DATABASE CONFIGURATION ====================
DB_PATH = "learning_platform.db"

# ==================== AI CONFIGURATION ====================
API_KEY = "AIzaSyDlIbDoYs5yqCTpyf-FPXuwRIWvecl5Lc0"  # Gemini API key

# Try to import AI features (optional)
try:
    import google.genai as genai
    from google.genai import types
    AI_AVAILABLE = True
    # Initialize AI client
    client = genai.Client(api_key=API_KEY)
except ImportError:
    AI_AVAILABLE = False
    client = None
    print("Warning: google-genai not installed. AI features will be disabled.")

# ==================== MODERN UI THEME ====================

# Color Palette - Modern, Professional
COLORS = {
    'primary': '#2563eb',      # Blue
    'primary_dark': '#1e40af',
    'primary_light': '#3b82f6',
    'success': '#10b981',      # Green
    'success_dark': '#059669',
    'warning': '#f59e0b',      # Orange
    'warning_dark': '#d97706',
    'danger': '#ef4444',       # Red
    'danger_dark': '#dc2626',
    'purple': '#8b5cf6',
    'purple_dark': '#7c3aed',
    'bg_primary': '#ffffff',   # White
    'bg_secondary': '#f8fafc', # Light gray
    'bg_tertiary': '#f1f5f9',
    'text_primary': '#1e293b',
    'text_secondary': '#64748b',
    'border': '#e2e8f0',
    'shadow': '#94a3b8'
}

# Fonts
FONTS = {
    'title': ('Segoe UI', 24, 'bold'),
    'heading': ('Segoe UI', 18, 'bold'),
    'subheading': ('Segoe UI', 14, 'bold'),
    'body': ('Segoe UI', 11),
    'body_bold': ('Segoe UI', 11, 'bold'),
    'small': ('Segoe UI', 9),
    'button': ('Segoe UI', 11, 'bold'),
    'button_large': ('Segoe UI', 13, 'bold')
}

# ==================== LEARNING CONFIGURATION ====================

# Learning categories
LEARNING_CATEGORIES = ["factual", "procedural", "strategic", "rational"]

# Category descriptions
CATEGORY_DESCRIPTIONS = {
    'factual': 'Basic facts and definitions',
    'procedural': 'Step-by-step problem solving',
    'strategic': 'Multi-step complex problems',
    'rational': 'Explanations and reasoning'
}

# Session configuration
MIN_PROBLEMS_FOR_MASTERY = 20
MASTERY_THRESHOLD = 0.90  # 90% accuracy

# Profile update frequency (every N problems)
PROFILE_UPDATE_FREQUENCY = 5

