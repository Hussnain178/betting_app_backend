# matches_data/models.py
from django_mongoengine import Document, fields
from datetime import datetime, timedelta
import pytz


class Match(Document):
    _id = fields.StringField()
    competitor1 = fields.StringField(required=True)
    competitor2 = fields.StringField(required=True)
    match_id = fields.StringField(required=True, unique=True)
    timestamp = fields.DateTimeField(required=True)  # Stores timezone-aware datetime
    country = fields.StringField()
    group = fields.StringField()  # Tournament/league name
    is_country = fields.BooleanField(default=False)
    match_link = fields.URLField()
    prices = fields.DictField(default=dict)  # Odds from different bookmakers
    sport = fields.StringField(required=True)
    status = fields.StringField(default="sched")  # scheduled, live, finished

    # Additional fields for better data management
    created_at = fields.DateTimeField(default=lambda: datetime.now(pytz.UTC))
    updated_at = fields.DateTimeField(default=lambda: datetime.now(pytz.UTC))
    website_source = fields.StringField()  # Track which scraper added this match
    currentScore_competitor1 = fields.StringField()
    currentScore_competitor2 = fields.StringField()
    meta = {
        'collection': 'matches_data',
        'db_alias': 'default',
        'indexes': [
            'match_id',
            'sport',
            'timestamp',
            ('sport', 'timestamp'),
            ('country', 'sport'),
            'status'
        ]
    }

    def save(self, *args, **kwargs):
        """
        Override save to ensure timestamp is timezone-aware and update updated_at
        """
        # Ensure timestamp is timezone-aware UTC
        if self.timestamp and isinstance(self.timestamp, datetime):
            if self.timestamp.tzinfo is None:
                self.timestamp = self.timestamp.replace(tzinfo=pytz.UTC)
            else:
                self.timestamp = self.timestamp.astimezone(pytz.UTC)

        # Update the updated_at field
        self.updated_at = datetime.now(pytz.UTC)

        # If this is a new document, set created_at
        if not self.pk:
            self.created_at = datetime.now(pytz.UTC)

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.competitor1} vs {self.competitor2} ({self.sport}) - {self.timestamp}"

    @property
    def match_title(self):
        """Return a formatted match title"""
        return f"{self.competitor1} vs {self.competitor2}"

    @property
    def has_odds(self):
        """Check if match has any odds available"""
        return bool(self.prices and len(self.prices) > 0)

    @property
    def bookmaker_count(self):
        """Return number of bookmakers with odds for this match"""
        return len(self.prices) if self.prices else 0

    def get_odds_for_bookmaker(self, bookmaker_name):
        """Get odds for a specific bookmaker"""
        return self.prices.get(bookmaker_name, {}) if self.prices else {}

    @classmethod
    def get_upcoming_matches(cls, days=7):
        """Get matches for the next N days"""
        now = datetime.now(pytz.UTC)
        future_date = now + timedelta(days=days)
        return cls.objects.filter(
            timestamp__gte=now,
            timestamp__lt=future_date
        ).order_by('timestamp')

    @classmethod
    def get_matches_by_sport(cls, sport_name, days=7):
        """Get upcoming matches for a specific sport"""
        now = datetime.now(pytz.UTC)
        future_date = now + timedelta(days=days)
        return cls.objects.filter(
            sport=sport_name,
            timestamp__gte=now,
            timestamp__lt=future_date
        ).order_by('timestamp')


class WebsiteData(Document):
    """
    Separate model for storing raw website data before matching
    """
    website = fields.StringField(required=True)
    sport = fields.StringField(required=True)
    country = fields.StringField()
    group = fields.StringField()
    timestamp = fields.DateTimeField(required=True)
    match_id = fields.StringField(required=True)
    competitor1 = fields.StringField(required=True)
    competitor2 = fields.StringField(required=True)
    status = fields.StringField(default="sched")
    prices = fields.DictField(default=dict)
    is_country = fields.BooleanField(default=False)

    # Matching info
    matched_to_flashscore = fields.BooleanField(default=False)
    flashscore_match_id = fields.StringField()

    created_at = fields.DateTimeField(default=lambda: datetime.now(pytz.UTC))

    meta = {
        'collection': 'website_data',
        'db_alias': 'default',
        'indexes': [
            'website',
            'sport',
            'timestamp',
            ('website', 'sport'),
            'matched_to_flashscore'
        ]
    }

    def save(self, *args, **kwargs):
        """Ensure timestamp is timezone-aware UTC"""
        if self.timestamp and isinstance(self.timestamp, datetime):
            if self.timestamp.tzinfo is None:
                self.timestamp = self.timestamp.replace(tzinfo=pytz.UTC)
            else:
                self.timestamp = self.timestamp.astimezone(pytz.UTC)

        return super().save(*args, **kwargs)

# # matches_data/models.py
# from django_mongoengine import Document, fields
#
#
# class Match(Document):
#     _id = fields.StringField()
#     competitor1 = fields.StringField()
#     competitor2 = fields.StringField()
#     match_id = fields.StringField()
#     timestamp = fields.DateTimeField()  # Ensure this is DateTimeField
#     country = fields.StringField()
#     group = fields.StringField()
#     is_country = fields.BooleanField()
#     match_link = fields.URLField()
#     prices = fields.DictField()
#     sport = fields.StringField()
#     status = fields.StringField()
#
#     meta = {
#         'collection': 'matches_data',
#         'db_alias': 'default'
#     }
