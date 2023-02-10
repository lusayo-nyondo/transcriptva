from django.db import models

from transcriptva_clientaccount.models import User

ISSUE_CATEGORIES = [
    [ 'OTHER', 'Other' ],
    [ 'GENERAL_INQUIRY', 'General Inquiry' ],
    [ 'FEATURE_REQUEST', 'Feature Request'],
    [ 'DMCA_COMPLAINT', 'DMCA Content Complaint' ],
    [ 'WEBSITE_ERROR', 'Client Experienced Error with the Website' ],
    [ 'GENERAL_COMPLAINT', 'General Complaint'],

    [ 'BAD_TRANSCRIPT', 'Client Got a Bad Transcript' ],
    [ 'WRONG_FILE_ORDER', 'Client Submitted Wrong File on Order']
]

ISSUE_MODES = [
    [ 'GENERAL', 'General Issue' ],
    [ 'ORDER_RELATED', 'Order Related Issue']
]

ISSUE_STATUSES = [
    [ 'OPEN', 'Open' ],
    [ 'CLOSED', 'Closed' ]
]


class ClientIssue(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        choices=ISSUE_STATUSES,
        max_length=100,
        default="OPEN"
    )

    mode = models.CharField(
        choices=ISSUE_MODES,
        max_length=100,
        default='GENERAL'
    )

    category = models.CharField(
        choices=ISSUE_CATEGORIES,
        max_length=100,
        default='GENERAL_INQUIRY'
    )

    # Issue reference can be anything such as order id, page url, transcript id, account id, etc.
    reference = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return '[{}][{}][{}]'.format(
            self.user,
            self.category,
            self.reference
        )


class IssueAttachment(models.Model):
    issue = models.ForeignKey(
        to=ClientIssue,
        on_delete=models.CASCADE,
        related_name='attachments'
    )

    def _build_upload_path(self, filename):
        return 'issues/{}/{}/{}'.format(
            self.issue.user,
            self.issue.pk,
            filename
        )

    file = models.FileField(
        upload_to=_build_upload_path
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.file.path

