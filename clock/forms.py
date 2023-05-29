from django import forms

from .models import Shift


class ShiftCorrectionForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['corrected_punch_in', 'corrected_punch_out', 'corrected_break_start', 'corrected_break_end', 'note']

class ClockForm(forms.Form):
    ACTION_CHOICES = [
        ('clock_in', 'Clock In'),
        ('clock_out', 'Clock Out'),
        ('start_break', 'Start Break'),
        ('end_break', 'End Break')
    ]

    action = forms.ChoiceField(
        choices=ACTION_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        initial='clock_in'
    )
