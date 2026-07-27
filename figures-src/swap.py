def replace_fig(s, marker, new):
    """Replace the alt-text + caption + brief block that follows `marker`."""
    i = s.index(marker)
    a = s.index("![", i)
    open_fence = s.index("```\nFIGURE BRIEF", a)
    close = s.index("\n```", open_fence + 3) + len("\n```")
    return s[:a] + new + s[close:]
