from rest_framework import serializers
from datetime import datetime
import pytz


class MatchSerializer(serializers.Serializer):
    def to_representation(self, instance):
        # Handle timezone-aware datetime serialization
        start_time = None
        if instance.timestamp:
            if isinstance(instance.timestamp, datetime):
                # Ensure timezone-aware and convert to UTC if needed
                if instance.timestamp.tzinfo is None:
                    # Naive datetime, assume UTC
                    utc_timestamp = instance.timestamp.replace(tzinfo=pytz.UTC)
                else:
                    # Convert to UTC
                    utc_timestamp = instance.timestamp.astimezone(pytz.UTC)
                start_time = utc_timestamp.isoformat()
            else:
                # Handle string timestamps
                start_time = str(instance.timestamp)

        return {
            "id": str(instance._id) if instance._id else None,
            "home_team": instance.competitor1,
            "away_team": instance.competitor2,
            "match_id": instance.match_id,
            "start_time": start_time,
            "start_time_utc": start_time,  # Explicit UTC field
            "country": instance.country,
            "tournament": instance.group,
            "sport": instance.sport,
            "status": instance.status,
            "match_url": getattr(instance, 'match_link', None),
            "is_country_match": getattr(instance, 'is_country', False),
            "odds": instance.prices or {},
            "has_odds": bool(instance.prices and len(instance.prices) > 0)
        }


class SportSerializer(serializers.Serializer):
    def to_representation(self, instance):
        if isinstance(instance, dict):
            return {
                "sport": instance.get("sport", "")
            }
        elif hasattr(instance, 'sport'):
            return {
                "sport": instance.sport
            }
        else:
            # If instance is just a string (from distinct query)
            return {
                "sport": str(instance)
            }


class MatchSummarySerializer(serializers.Serializer):
    """
    Lightweight serializer for match summaries/lists
    """

    def to_representation(self, instance):
        start_time = None
        if instance.timestamp:
            if isinstance(instance.timestamp, datetime):
                if instance.timestamp.tzinfo is None:
                    utc_timestamp = instance.timestamp.replace(tzinfo=pytz.UTC)
                else:
                    utc_timestamp = instance.timestamp.astimezone(pytz.UTC)
                start_time = utc_timestamp.isoformat()
            else:
                start_time = str(instance.timestamp)

        return {
            "match_id": instance.match_id,
            "home_team": instance.competitor1,
            "away_team": instance.competitor2,
            "start_time": start_time,
            "sport": instance.sport,
            "tournament": instance.group,
            "country": instance.country,
            "has_odds": bool(instance.prices and len(instance.prices) > 0)
        }


class OddsSerializer(serializers.Serializer):
    """
    Serializer specifically for odds/prices data
    """

    def to_representation(self, instance):
        odds_data = instance.prices or {}

        # Structure odds data for better API consumption
        structured_odds = {}
        for bookmaker, odds in odds_data.items():
            if isinstance(odds, dict):
                structured_odds[bookmaker] = odds
            else:
                # Handle simple odds values
                structured_odds[bookmaker] = {"value": odds}

        return {
            "match_id": instance.match_id,
            "home_team": instance.competitor1,
            "away_team": instance.competitor2,
            "sport": instance.sport,
            "odds": structured_odds,
            "bookmakers": list(structured_odds.keys()),
            "bookmaker_count": len(structured_odds)
        }
# from rest_framework import serializers
#
#
# class MatchSerializer(serializers.Serializer):
#     def to_representation(self, instance):
#         return {
#             "id": str(instance._id),
#             "home_team": instance.competitor1,
#             "away_team": instance.competitor2,
#             "match_id": instance.match_id,
#             "start_time": instance.timestamp.isoformat() if instance.timestamp else None,
#             "country": instance.country,
#             "tournament": instance.group,
#             "sport": instance.sport,
#             "status": instance.status,
#             "match_url": instance.match_link,
#             "odds": instance.prices or {}
#         }
#
#
# class SportSerializer(serializers.Serializer):
#     def to_representation(self, instance):
#         return {
#             "sport": instance.sport
#         }
