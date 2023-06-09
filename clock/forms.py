from django import forms

from .models import ClockShift


class ShiftCorrectionForm(forms.ModelForm):
    class Meta:
        model = ClockShift
        fields = ['corrected_punch_in', 'corrected_punch_out', 'corrected_break_start', 'corrected_break_end', 'note']

        widgets = {'corrected_punch_in': forms.DateInput(attrs={'type': 'datetime-local'}),
                   'corrected_punch_out': forms.DateInput(attrs={'type': 'datetime-local'}),
                   'corrected_break_start': forms.DateInput(attrs={'type': 'datetime-local'}),
                   'corrected_break_end': forms.DateInput(attrs={'type': 'datetime-local'})}


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
