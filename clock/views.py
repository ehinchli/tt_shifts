from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import ClockForm, ShiftCorrectionForm
from .models import Shift


class ClockView(FormView):
    template_name = 'clock.html'
    form_class = ClockForm
    success_url = '/clock/clock/'

    def get_initial(self):
        current_shift = Shift.objects.filter(user=self.request.user, punch_out__isnull=True).first()
        if current_shift:
            return {'action': 'clock_out'}
        else:
            return {'action': 'clock_in'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_shift = Shift.objects.filter(user=self.request.user, punch_out__isnull=True).first()
        if current_shift:
            context['clocked_in'] = True
            context['shift_start_time'] = current_shift.punch_in
            context['break_start_time'] = current_shift.break_start
            context['break_end_time'] = current_shift.break_end
            context['shift_length'] = timezone.now() - current_shift.punch_in
            if current_shift.break_start and not current_shift.break_end:
                context['break_length'] = timezone.now() - current_shift.break_start
            else:
                context['break_length'] = None
        else:
            context['clocked_in'] = False
        return context

    def form_valid(self, form):
        action = form.cleaned_data['action']
        current_shift = Shift.objects.filter(user=self.request.user, punch_out__isnull=True).first()
        if action == 'clock_in':
            if not current_shift:
                Shift.objects.create(user=self.request.user, punch_in=timezone.now())
        elif action == 'clock_out':
            if current_shift:
                current_shift.punch_out = timezone.now()
                current_shift.save()
        return super().form_valid(form)


class ShiftListView(ListView):
    model = Shift
    template_name = 'sheet.html'
    context_object_name = 'shift_list'

    def get_queryset(self):
        user = self.request.user
        shifts = Shift.objects.filter(user=user)
        return shifts


class ShiftCorrectionView(FormView):
    template_name = 'correction.html'
    form_class = ShiftCorrectionForm
    success_url = '/clock/sheet/'

    def get_initial(self):
        shift_id = self.kwargs['shift_id']
        shift = get_object_or_404(Shift, pk=shift_id)
        return {
            'punch_in': shift.punch_in,
            'punch_out': shift.punch_out,
            'break_start': shift.break_start,
            'break_end': shift.break_end,
            'note': shift.note
        }

    def form_valid(self, form):
        shift_id = self.kwargs['shift_id']
        shift = get_object_or_404(Shift, pk=shift_id)
        shift.corrected_punch_in = form.cleaned_data['corrected_punch_in']
        shift.corrected_punch_out = form.cleaned_data['corrected_punch_out']
        shift.corrected_break_start = form.cleaned_data['corrected_break_start']
        shift.corrected_break_end = form.cleaned_data['corrected_break_end']
        shift.note = form.cleaned_data['note']
        shift.save()
        return super().form_valid(form)