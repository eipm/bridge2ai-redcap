"""Heading anchors that match GitHub's, so links written for GitHub keep working on the site.

GitHub lowercases the heading, drops punctuation and symbols (emoji included) but keeps letters,
digits, combining marks (such as the emoji variation selector U+FE0F), '-' and '_', and turns each
space into '-'. For example "## 🗄️ Retired Questionnaires" becomes "️-retired-questionnaires".
"""
import unicodedata


def slugify(value, separator='-'):
    out = []
    for ch in value.strip().lower():
        if ch in '-_':
            out.append(ch)
        elif ch == ' ':
            out.append(separator)
        elif unicodedata.category(ch)[0] in 'LNM':
            out.append(ch)
    return ''.join(out)
