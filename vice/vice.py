# -*- coding: utf-8 -*-
"""
  /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$$$
 | $$   | $$|_  $$_/ /$$__  $$| $$_____/
 | $$   | $$  | $$  | $$  \__/| $$      
 |  $$ / $$/  | $$  | $$      | $$$$$   
  \  $$ $$/   | $$  | $$      | $$__/   
   \  $$$/    | $$  | $$    $$| $$      
    \  $/    /$$$$$$|  $$$$$$/| $$$$$$$$
     \_/    |______/ \______/ |________/
                                        
 URL: https://github.com/pedroreys/pygments-vice
 Pygments Port Author: Pedro Reys <pedro@pedroreys.com>

 Original Vice Theme:
    URL: https://github.com/bcicen/vim-vice
    Original Author: Bradley Cicenas <bradley@vektor.nyc>

 License: MIT
"""

from pygments.style import Style
from pygments.token import Token, Comment, Number, Keyword, Name, String, Operator, Generic

colors = {
    'white':          '#ffffff',
    'grey0':          '#878787',  # lightest grey
    'grey1':          '#444444',  # mid grey
    'grey2':          '#303030',  # darkest grey
    'pink':           '#ff87d7',
    'light_pink':     '#ffafd7',
    'hot_pink':       '#ff00ff',
    'red':            '#ff005f',
    'teal':           '#87ffff',
    'light_blue':     '#afffff',
    'light_yellow':   '#ffffaf',
    'mint':           '#afffd7',
    'dark_mint':      '#00ffaf',
    'lavender':       '#d7afff',
    'gray_purple':    '#afafd7',
    'dark_lavender':  '#875faf'    
}


def to_color(style=None, fg=None, bg=None):

    style = f'{style} ' if style is not None else ''
    bg = f'bg:{colors[bg]} ' if bg is not None else ''
    fg = f'{colors[fg]} ' if fg is not None else ''

    return f'{style}{fg}{bg}'


class ViceStyle(Style):
    default_styles = ''
    background_color = None
    styles = {
        Token:              to_color(style='noinherit', fg='white'),
        Generic.Inserted:   to_color(style='noinherit', fg='white', bg='dark_mint'),
        Generic.Deleted:    to_color(style='noinherit', fg='red'),
        Generic.Traceback:  to_color(style='noinherit', fg='white', bg='hot_pink'),
        Comment:            to_color(style='noinherit', fg='gray_purple'),
        Name.Constant:      to_color(style='noinherit', fg='mint'),
        Number.Float:       to_color(style='noinherit', fg='lavender'),
        Name.Function:      to_color(style='noinherit', fg='pink'),
        Name.Class:         to_color(style='noinherit bold', fg='pink'),
        Name.Attribute:     to_color(style='noinherit', fg='pink'),
        Name.Variable:      to_color(style='noinherit', fg='pink'),
        Name.Label:         to_color(style='noinherit', fg='teal'),
        Generic.Output:     to_color(style='noinherit', fg='white'),
        Number:             to_color(style='noinherit', fg='mint'),
        Operator.Word:      to_color(style='noinherit', fg='light_pink'),
        Comment.Preproc:    to_color(style='noinherit', fg='teal'),
        Name.Entity:        to_color(style='noinherit', fg='pink'),
        Keyword:            to_color(style='noinherit', fg='teal'),
        Name.Tag:           to_color(style='noinherit', fg='teal'),
        String:             to_color(style='noinherit', fg='mint'),
        String.Interpol:    to_color(style='noinherit', fg='white'),
        Generic.Heading:    to_color(style='noinherit', fg='white'),
        Generic.Subheading: to_color(style='noinherit', fg='white'),
        Keyword.Type:       to_color(style='noinherit', fg='mint'),
        Generic.Emph:       to_color(style='underline')
    }
