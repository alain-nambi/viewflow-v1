from django.views import generic
from viewflow import views as flow_views
from django.views.generic import TemplateView

class CreateRequestView(flow_views.StartViewMixin, generic.UpdateView):
    template_name = 'viewflow/start_detail.html'
    fields = ["text"]

    def get_object(self, queryset=None):
        return self.activation.process

class ApproveRequestView(flow_views.TaskViewMixin, generic.UpdateView):
    fields = ["approved"]

    def get_object(self, queryset=None):
        return self.activation.process

class CustomProcessListView(flow_views.ProcessListView):
    template_name = 'viewflow/process_list.html'

class CustomTaskListView(flow_views.TaskListView):
    template_name = 'viewflow/task_list.html'

class CustomQueueListView(flow_views.QueueListView):
    template_name = 'viewflow/queue_list.html'

class CustomProcessDetailView(flow_views.ProcessDetailView):
    template_name = 'viewflow/process_detail.html'

class CustomApproveDetailView(flow_views.TaskListView):
    template_name = 'viewflow/approve_detail.html'

class CustomSendDetailView(flow_views.TaskListView):
    template_name = 'viewflow/send_detail.html'

class CustomEndDetailView(flow_views.TaskListView):
    template_name = 'viewflow/end_detail.html'

class CustomStartDetailView(flow_views.StartViewMixin, generic.UpdateView):
    template_name = 'viewflow/start_detail.html'

    fields = ["text"]

    def get_object(self, queryset=None):
        return self.activation.process