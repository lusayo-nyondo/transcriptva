from django.db import models
from django.urls import reverse

from datetime import datetime, timedelta

from config.settings import SITE_URL

from transcriptva_clientaccount.models import User


VERBATIM = [
    [ 'N/A', 'N/A' ],
    [ 'CLEAN_VERBATIM', 'Clean Verbatim' ],
    [ 'FULL_VERBATIM', 'Full Verbatim' ],
    [ 'CUSTOM_VERBATIM', 'Custom Verbatim' ]
]

TYPE = [
    [ 'HUMAN_GENERATED', 'Human Generated' ],
    [ 'MACHINE_GENERATED', 'Machine Generated' ]
]

ACCENT = [
    [ 'ALL', 'ALL' ],
    [ 'AMERICAN_ENGLISH', 'American English' ],
    [ 'BRITISH_ENGLISH', 'British English' ]
]

TIMESTAMPING = [
    [ 'NO_TIMESTAMPS', 'No Timestamps' ],
    [ 'EVERY_SPEAKER', 'Every Change of Speaker' ],
    [ 'EVERY_X_SECONDS', 'Every X Seconds' ]
]

NO_OF_SPEAKERS = [
    [ 'ALL', 'All' ],
    [ 'BETWEEN_1_AND_2', 'Between 1 and 2' ],
    [ 'BETWEEN_3_AND_5', 'Between 3 and 5' ],
    [ '6_AND_ABOVE', '6 and above' ]
]

SPEAKER_IDENTIFICATION = [
    [ 'NO_SPEAKER_IDENTIFICATION', 'No Speaker Identification' ],
    [ 'EVERY_SPEAKER_CHANGE', 'Every Change of Speaker' ]
]

ORDER_STATUSES = [
    [ 'AWAITING_PAYMENT', 'Awaiting Payment' ],
    [ 'AWAITING_ASSIGNMENT', 'Awaiting Assignment' ],
    [ 'CURRENTLY_IN_WORK_QUEUE', 'Currently in Work Queue' ],
    [ 'COMPLETED', 'Completed'],
    [ 'CANCELED', 'Canceled']
]

TRANSCRIPT_STATUSES = [
    [ 'QUEUED_FOR_TRANSCRIPTION', 'Queued for Transcription' ],
    [ 'UNDERGOING_TRANSCRIPTION', 'Undergoing Transcription' ],
    [ 'UNDERGOING_REVIEW', 'Undergoing Review' ],
    [ 'COMPLETED', 'Completed' ]
]

NOTIFICATION_TYPES = [
    [ 'INFO', 'Info' ],
    [ 'WARNING', 'Warning' ],
    [ 'SUCCESS', 'Success' ],
    [ 'DANGER', 'Danger' ]
]

NOTIFICATION_ACTIONS_REQUIRED = [
    [ 'NONE', 'None' ],
    [ 'ACKNOWLEDGE_RECEIPT', 'Acknowledge Receipt' ]
]

NOTIFICATION_ENGAGEMENTS = [
    [ 'DISMISSED', 'Dismissed' ],
    [ 'UNSEEN', 'Unseen' ]
]


class ServicePrice(models.Model):
    verbatim = models.CharField(
        choices=VERBATIM,
        max_length=255,
        default="CLEAN_VERBATIM"
    )

    type = models.CharField(
        choices=TYPE,
        max_length=255,
        default="HUMAN_GENERATED"
    )

    timestamping = models.CharField(
        choices=TIMESTAMPING,
        max_length=255,
        default="NO_TIMESTAMPS"
    )

    speaker_identification = models.CharField(
        choices=SPEAKER_IDENTIFICATION,
        max_length=255,
        default="NO_SPEAKER_IDENTIFICATION"
    )

    number_of_speakers = models.CharField(
        choices=NO_OF_SPEAKERS,
        max_length=255,
        default="BETWEEN_3_AND_5"
    )

    price_per_minute = models.FloatField()

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return '[{}]-[{}]-[{}]-[{}]-[{}]'.format(
            self.type,
            self.verbatim,
            self.speaker_identification,
            self.timestamping,
            self.number_of_speakers
        )


class Order(models.Model):
    owner = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    status = models.CharField(
        choices=ORDER_STATUSES,
        max_length=255,
        default='AWAITING_PAYMENT'
    )

    reference = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    service = models.ForeignKey(
        to=ServicePrice,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    amount_due = models.FloatField(
        default=0.0
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

    @property
    def transcripts(self):
        transcripts = Transcript.objects.filter(
            order=self
        )

        return transcripts

    def __str__(self):
        return '{}-[{}]-{}'.format(
            self.owner.__str__(),
            self.reference,
            self.created_on,
        )


class Transcript(models.Model):
    def _build_upload_path(self, filename):
        return 'orders/{}/{}'.format(
            self.owner.username,
            filename
        )

    owner = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        choices=TRANSCRIPT_STATUSES,
        max_length=255,
        default="QUEUED_FOR_TRANSCRIPTION"
    )

    order = models.ForeignKey(
        to=Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to=_build_upload_path
    )

    duration = models.FloatField(
        default=0.0
    )

    verbatim = models.CharField(
        choices=VERBATIM,
        max_length=255,
        default="CLEAN_VERBATIM"
    )

    timestamping = models.CharField(
        choices=TIMESTAMPING,
        max_length=255,
        default="NO_TIMESTAMPS"
    )

    speaker_identification = models.CharField(
        choices=SPEAKER_IDENTIFICATION,
        max_length=255,
        default="NO_SPEAKER_IDENTIFICATION"
    )

    accent = models.CharField(
        choices=ACCENT,
        max_length=255,
        default="AMERICAN_ENGLISH"
    )

    type = models.CharField(
        choices=TYPE,
        max_length=255,
        default="HUMAN_GENERATED"
    )

    number_of_speakers = models.CharField(
        choices=NO_OF_SPEAKERS,
        max_length=255,
        default="BETWEEN_3_AND_5"
    )

    text = models.TextField(
        blank=True,
        null=True
    )

    applicable_cost = models.FloatField(
        default=0.0,
        blank=True,
        null=True
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    completed_on = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Transcript-{}'.format(
            self.order
        )


class Notification(models.Model):
    title = models.CharField(
        max_length=255
    )

    text = models.TextField(
        null=True,
        blank=True
    )

    type = models.CharField(
        choices=NOTIFICATION_TYPES,
        max_length=255,
        default="INFO"
    )

    action_required = models.CharField(
        choices=NOTIFICATION_ACTIONS_REQUIRED,
        max_length=255,
        default="NONE"
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    def _get_expiry_date():
        # Expiry defaults to 1 week from today.
        now = datetime.now()
        expiry_date = now + timedelta(days=7)

        return expiry_date

    expires_on = models.DateTimeField(
        default=_get_expiry_date
    )

    def __str__(self):
        return self.title


class NotificationEngagement(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    notification = models.ForeignKey(
        to=Notification,
        on_delete=models.CASCADE
    )

    engagement = models.CharField(
        choices=NOTIFICATION_ENGAGEMENTS,
        max_length=255,
        default='DISMISSED'
    )

    def __str__(self):
        return '[{}][{}]'.format(
            self.user.username,
            self.notification.title
        )


class DashboardPost(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    thumbnail = models.FileField(
        upload_to='dashboard_posts'
    )

    text = models.TextField()

    action_text = models.CharField(
        max_length=100,
        default="Learn More"
    )

    def _get_default_url():
        url = '{}/{}'.format(
            SITE_URL,
            'clientsupport'
        )

        return url

    action_url = models.URLField(
        default=_get_default_url
    )
    
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

