# Helper functions for formatting output.

def create_page_header(title, description):
    """Create HTML for the page header."""
    return f"<div class='page-header'><h1>{title}</h1><p style='font-size:1.1rem;line-height:1.8rem;margin-top:10px;'>{description}</p></div>"

def create_section_card(title, content=None, hint=None):
    """Create HTML for a section card."""
    hint_html = f"<p class='hint'>{hint}</p>" if hint else ""
    content_html = content if content else ""
    return f"<div class='section-card'><h2>{title}</h2>{hint_html}{content_html}</div>"

def create_info_panel(title, content):
    """Create HTML for an info panel."""
    return f"<div class='info-panel'><h3>{title}</h3>{content}</div>"

def format_list_items(items):
    """Format a list of items as HTML list items."""
    return "\n".join(f"<li>{item}</li>" for item in items)

def format_paragraph(text, class_name=None):
    """Format text as a paragraph with optional class."""
    class_attr = f" class='{class_name}'" if class_name else ""
    return f"<p{class_attr}>{text}</p>"