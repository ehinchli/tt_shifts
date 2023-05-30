import datetime

from django import template

register = template.Library()


@register.filter
def duration(td):
    if not isinstance(td, datetime.timedelta):
        return ''
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'{f"{hours}hr " if hours else ""}{f"{minutes}m " if hours or minutes else ""}{seconds:02}s '
