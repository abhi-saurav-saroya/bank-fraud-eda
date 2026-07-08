from typing import Optional


def badge(text: str) -> str:
    """Returns a badge."""

    return f"""
    <div class="hero-badge">
        {text}
    </div>
    """


def button(text: str, button_type: str = "primary") -> str:
    """Returns a styled button."""

    return f"""
    <div class="btn btn-{button_type}">
        {text}
    </div>
    """


def icon_button(svg: str, button_type: str = "primary") -> str:
    """Returns an icon button."""

    return f"""
    <div class="btn btn-{button_type}">
        {svg}
    </div>
    """


def card(content: str, css_class: str = "card") -> str:
    """Returns a generic card."""

    return f"""
    <div class="{css_class}">
        {content}
    </div>
    """


def metric_card(title: str, value: str, icon: str = "") -> str:
    """Returns a KPI card."""

    return f"""
    <div class="metric-card">

        <div class="metric-icon">
            {icon}
        </div>

        <div class="metric-label">
            {title}
        </div>

        <div class="metric-value">
            {value}
        </div>

    </div>
    """


def section_title(title: str, subtitle: Optional[str] = None) -> str:
    """Returns a section heading."""

    subtitle_html = ""

    if subtitle:
        subtitle_html = f"""
        <div class="section-subtitle">
            {subtitle}
        </div>
        """

    return f"""
    <div class="section">

        <div class="section-title">
            {title}
        </div>

        {subtitle_html}

    </div>
    """


def info_card(title: str, description: str) -> str:
    """Returns an information card."""

    return f"""
    <div class="feature-card">

        <div class="card-title">
            {title}
        </div>

        <div class="card-description">
            {description}
        </div>

    </div>
    """


def tag(text: str) -> str:
    """Returns a tag."""

    return f"""
    <span class="tag">
        {text}
    </span>
    """


def chip(text: str) -> str:
    """Returns a chip."""

    return f"""
    <span class="chip">
        {text}
    </span>
    """

def divider() -> str:
    """Returns a divider."""

    return """
    <div class="divider"></div>
    """


def hero_stat(value: str, label: str) -> str:
    """Returns the floating hero statistic."""

    return f"""
    <div class="hero-card">

        <div class="hero-stat">
            {value}
        </div>

        <div class="hero-label">
            {label}
        </div>

    </div>
    """


def wrapper(content: str, css_class: str = "") -> str:
    """Wraps any HTML inside a div."""

    return f"""
    <div class="{css_class}">
        {content}
    </div>
    """