from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.ModelList(
            collapsible=False,
            title=_('Exhibit Information'),
            column=1,
            models=('basetyzer.models.Exhibit', 'basetyzer.models.Item',),
        ))

        self.children.append(modules.ModelList(
            collapsible=False,
            title=_('System Information'),
            column=1,
            models=('basetyzer.models.CustomUser',
                    'basetyzer.models.SuperQRCode'),
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))

        self.children.append(modules.LinkList(
            collapsible=False,
            layout='inline',
            column=2,
            children=(
                ['QRCode', reverse('qr_code_generator')],
                ['Home Page', reverse('index')],
            )
        ))
