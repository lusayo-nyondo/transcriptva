from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from datetime import datetime, timedelta

VERBATIM = [
    [ 'N/A', 'N/A'],
    [ 'CLEAN_VERBATIM', 'CLEAN_VERBATIM' ],
    [ 'FULL_VERBATIM', 'FULL_VERBATIM' ],
    [ 'CUSTOM_VERBATIM', 'CUSTOM_VERBATIM' ]
]

TYPE = [
    [ 'HUMAN_GENERATED', 'HUMAN_GENERATED' ],
    [ 'MACHINE_GENERATED', 'MACHINE_GENERATED' ]
]

ACCENT = [
    [ 'ALL', 'ALL' ],
    [ 'AMERICAN_ENGLISH', 'AMERICAN_ENGLISH' ],
    [ 'BRITISH_ENGLISH', 'BRITISH_ENGLISH' ]
]

TIMESTAMPING = [
    [ 'NO_TIMESTAMPS', 'NO_TIMESTAMPS' ],
    [ 'EVERY_SPEAKER', 'EVERY_SPEAKER' ],
    [ 'EVERY_X_SECONDS', 'EVERY_X_SECONDS']
]

NO_OF_SPEAKERS = [
    [ 'ALL', 'ALL' ],
    [ 'BETWEEN_1_AND_2', 'BETWEEN_1_AND_2' ],
    [ 'BETWEEN_3_AND_5', 'BETWEEN_3_AND_5' ],
    [ '6_AND_ABOVE', '6_AND_ABOVE']
]

SPEAKER_IDENTIFICATION = [
    [ 'NO_SPEAKER_IDENTIFICATION', 'NO_SPEAKER_IDENTIFICATION' ],
    [ 'EVERY_SPEAKER_CHANGE', 'EVERY_SPEAKER_CHANGE' ]
]

ORDER_STATUSES = [
    [ 'SUBMITTED', 'SUBMITTED' ],
    [ 'AWAITING_PAYMENT', 'AWAITING_PAYMENT'],
    [ 'AWAITING_TRANSCRIPTION', 'AWAITING_TRANSCRIPTION'],
    [ 'AWAITING_REVIEW', 'AWAITING_REVIEW'],
    [ 'AWAITING_SIGNOFF', 'AWAITING_SIGNOFF'],
    [ 'AWAITING_DISPUTE_RESOLUTION', 'AWAITING_DISPUTE_RESOLUTION']
]

TRANSCRIPT_STATUSES = [
    [ 'QUEUED_FOR_TRANSCRIPTION', 'QUEUED_FOR_TRANSCRIPTION'],
    [ 'UNDERGOING_TRANSCRIPTION', 'UNDERGOING_TRANSCRIPTION' ],
    [ 'UNDERGOING_REVIEW', 'UNDERGOING_REVIEW'],
    [ 'COMPLETED', 'COMPLETED']
]

NOTIFICATION_TYPES = [
    [ 'INFO', 'INFO' ],
    [ 'WARNING', 'WARNING' ],
    [ 'SUCCESS', 'SUCCESS' ],
    [ 'DANGER', 'DANGER' ]
]

NOTIFICATION_ACTIONS_REQUIRED = [
    [ 'NONE', 'NONE' ],
    [ 'ACKNOWLEDGE_RECEIPT', 'ACKNOWLEDGE_RECEIPT' ]
]

NOTIFICATION_ENGAGEMENTS = [
    [ 'DISMISSED', 'DISMISSED' ],
    [ 'UNSEEN', 'UNSEEN']
]


class User(AbstractUser):
    company = models.TextField(
        null=True,
        blank=True
    )


class Order(models.Model):
    def _build_upload_path(self, filename):
        return 'orders/{}/{}'.format(
            self.owner.username,
            filename
        )

    owner = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    status = models.CharField(
        choices=ORDER_STATUSES,
        max_length=255,
        default='SUBMITTED'
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

    def __str__(self):
        return '{}-[{}]-{}'.format(
            self.owner.__str__(),
            self.created_on,
            self.file
        )

    def calculate_duration(order):
        pass

    def calculate_amount_due(order):
        pass


class Transcript(models.Model):
    order = models.OneToOneField(
        to=Order,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transcript"
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    text = models.TextField(
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

    status = models.CharField(
        choices=TRANSCRIPT_STATUSES,
        max_length=255,
        default="QUEUED_FOR_TRANSCRIPTION"
    )

    def __str__(self):
        return 'Transcript-{}'.format(
            self.order
        )


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
        url = reverse('support')
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

