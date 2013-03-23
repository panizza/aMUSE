from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for the admin page.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        exhibit_info = modules.ModelList(
            title=_('Exhibit Information'),
            models=('basetyzer.models.Exhibit', 'basetyzer.models.Item',),
        )
        sys_info = modules.ModelList(
            title=_('System Information'),
            models=('basetyzer.models.CustomUser',)
        )

        self.children.append(modules.Group(
            title="Museum Information",
            column=1,
            collapsible=False,
            children=[
                exhibit_info,
                sys_info,
            ]
        ))

        experience_info = modules.ModelList(
            title=_('Basic Information'),
            models=('basetyzer.models.Experience',),
        )
        action_info = modules.ModelList(
            title=_('Action Information'),
            models=('basetyzer.models.Action', 'basetyzer.models.Comment',
                    'basetyzer.models.Photo', 'basetyzer.models.Scan'
            )
        )

        self.children.append(modules.Group(
            title="Experience Information",
            column=1,
            collapsible=False,
            children=[
                experience_info,
                action_info,
            ]
        ))

        self.children.append(modules.LinkList(
            collapsible=False,
            layout='inline',
            column=3,
            children=(
                ['QRCode', reverse('qr_code_generator')],
                ['Home Page', reverse('index')],
            )
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
            ))
