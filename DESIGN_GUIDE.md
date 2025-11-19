# 🎨 Design Guide - Learning Management System

## Color Palette

### Primary Colors
```
🔵 Primary Blue
   - Main:  #2563eb
   - Dark:  #1e40af
   - Light: #3b82f6
   - Use: Primary actions, links, highlights

🟢 Success Green
   - Main:  #10b981
   - Dark:  #059669
   - Use: Correct answers, success messages, positive actions

🟠 Warning Orange
   - Main:  #f59e0b
   - Dark:  #d97706
   - Use: Progress tracking, important notices

🔴 Danger Red
   - Main:  #ef4444
   - Dark:  #dc2626
   - Use: Incorrect answers, errors, delete actions

🟣 Purple
   - Main:  #8b5cf6
   - Dark:  #7c3aed
   - Use: AI features, special functionality
```

### Neutral Colors
```
⚪ Backgrounds
   - Primary:   #ffffff (White - Cards)
   - Secondary: #f8fafc (Light Gray - Page background)
   - Tertiary:  #f1f5f9 (Lighter Gray - Sections)

⚫ Text
   - Primary:   #1e293b (Dark Gray - Main text)
   - Secondary: #64748b (Medium Gray - Descriptions)

🔲 Borders
   - Border:    #e2e8f0 (Light border)
   - Shadow:    #94a3b8 (Shadow color)
```

---

## Typography

### Font Family
**Segoe UI** - Modern, clean, highly readable system font

### Font Sizes & Weights
```
Title:          24pt, Bold    - Page headers
Heading:        18pt, Bold    - Section headers
Subheading:     14pt, Bold    - Card titles
Body:           11pt, Regular - Main content
Body Bold:      11pt, Bold    - Labels
Small:          9pt, Regular  - Hints, footnotes
Button:         11pt, Bold    - Standard buttons
Button Large:   13pt, Bold    - Primary actions
```

---

## Components

### 🔘 Buttons

#### Primary Button
```
Background:  #2563eb (Primary Blue)
Text:        White
Hover:       #1e40af (Primary Dark)
Padding:     20-25px horizontal, 12px vertical
Border:      None (flat design)
Cursor:      Hand pointer
```

#### Success Button
```
Background:  #10b981 (Success Green)
Text:        White
Hover:       #059669 (Success Dark)
Use:         Practice, Create, Confirm actions
```

#### Secondary Button
```
Background:  #f1f5f9 (Tertiary Gray)
Text:        #1e293b (Text Primary)
Hover:       #e2e8f0 (Border color)
Use:         Back, Cancel, Logout
```

### 📦 Cards

```
Background:       #ffffff (White)
Border:           1px solid #e2e8f0
Border Radius:    Minimal (flat design)
Padding:          40px
Hover Effect:     Border color changes to accent color
                  Border width: 2px
```

### 📋 Input Fields

```
Background:       White
Border:           1px solid #e2e8f0
Focus Border:     2px solid #2563eb
Padding:          8px vertical
Font:             11pt Segoe UI
```

### 🎯 Headers

```
Height:           80px
Background:       White (or accent color for special pages)
Padding:          20px horizontal, 40px vertical
Content:          Title on left, action buttons on right
```

---

## Layout Principles

### Spacing System
```
Extra Large:  40px  - Card padding, page margins
Large:        30px  - Section spacing
Medium:       20px  - Element spacing
Small:        15px  - Tight spacing
Extra Small:  10px  - Minimal spacing
Tiny:         5px   - Label spacing
```

### Grid System
```
Dashboard Cards:  2 columns
Topic List:       1 column (full width)
Forms:            Single column, centered
Max Width:        900-1100px for content
```

### Padding
```
Cards:        40px all sides
Buttons:      20-25px horizontal, 12px vertical
Headers:      40px horizontal, 20px vertical
Content:      40px horizontal, 30px vertical
```

---

## Interactive States

### Hover Effects
```
Buttons:
  - Background color darkens
  - Cursor changes to pointer

Cards:
  - Border color changes to accent
  - Border width increases to 2px

Links:
  - Color changes to primary
  - Underline appears (optional)
```

### Focus States
```
Input Fields:
  - Border color: Primary blue
  - Border width: 2px
  - Outline: None (custom border instead)
```

### Active States
```
Buttons:
  - Same as hover state
  - Slight scale effect (optional)
```

---

## Icons & Emojis

### Used Throughout
```
🎓  Education/Learning
📚  Student Pick Topic
🎲  Computer Pick/Random
📊  Progress/Analytics
🤖  AI Features
📝  Practice/Problems
📖  Goals/Reading
✓   Correct/Success
✗   Incorrect/Error
←   Back/Previous
→   Next/Forward
🚪  Logout/Exit
💡  Tips/Hints
⏳  Loading
```

---

## Screen-Specific Designs

### Login Screen
```
Size:         520x700px
Background:   #f8fafc
Card:         White with border
Icon:         🎓 (48pt)
Title:        24pt bold
Subtitle:     11pt regular, gray
```

### Dashboard
```
Size:         1100x750px
Header:       White, 80px height
Cards:        2 columns, equal width
Card Size:    ~500x400px
Spacing:      15px between cards
```

### Topic Selection
```
Header:       White with title and back button
Cards:        Full width, stacked
Card Height:  ~80px each
Hover:        Blue border highlight
```

### Goals Screen
```
Header:       White with topic name
Content:      Single large card
Sections:     Title, Description, Objectives
Objectives:   Gray background section
Navigation:   3 buttons (Previous, Practice, Next)
```

### AI Feedback
```
Size:         800x700px
Header:       Colored (green/red) based on result
Cards:        Stacked (Problem, Answers, Feedback)
Feedback:     Scrollable text area
Close:        Large centered button
```

---

## Best Practices

### Do's ✅
- Use consistent spacing (multiples of 5px)
- Maintain color hierarchy
- Provide hover feedback on interactive elements
- Use icons to enhance understanding
- Keep text readable (proper contrast)
- Center important content
- Use cards for grouping related content

### Don'ts ❌
- Don't mix different font families
- Don't use too many colors
- Don't make buttons too small
- Don't forget hover states
- Don't use low contrast text
- Don't overcrowd the interface
- Don't use inconsistent spacing

---

## Accessibility

### Contrast Ratios
```
Primary Text on White:     ✅ 12.6:1 (Excellent)
Secondary Text on White:   ✅ 4.8:1 (Good)
White Text on Primary:     ✅ 8.2:1 (Excellent)
White Text on Success:     ✅ 4.1:1 (Good)
```

### Keyboard Navigation
- Tab through all interactive elements
- Enter to submit forms
- Escape to close dialogs
- Arrow keys for navigation (where applicable)

### Screen Reader Support
- Proper label associations
- Descriptive button text
- Clear heading hierarchy

---

## Future Enhancements

Potential improvements:
- Rounded corners for softer look
- Subtle shadows for depth
- Animations for transitions
- Dark mode support
- Responsive design for different screen sizes
- Custom icons instead of emojis

---

**Design System Version**: 1.0  
**Last Updated**: 2025-11-19  
**Status**: ✅ Implemented and Active

