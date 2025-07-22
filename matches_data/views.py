from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
import pytz
from .models import Match
from .serializers import MatchSerializer, SportSerializer
from .auth import jwt_required


def get_utc_now():
    """
    Return current UTC time as timezone-aware datetime object
    """
    return datetime.now(pytz.UTC)


@api_view(["GET"])
@jwt_required
def get_matches(request):
    """
    Return matches from now to 7 days ahead
    Compatible with timezone-aware datetime objects from scrapers
    """
    # Use timezone-aware UTC datetime objects
    now = get_utc_now()
    seven_days_later = now + timedelta(days=7)

    # Query using timezone-aware datetimes
    matches = Match.objects.filter(
        timestamp__gte=now,
        timestamp__lt=seven_days_later,
        # prices__exists=True,
        # prices__ne={}
        # prices__ne={}
    ).order_by('timestamp')

    serializer = MatchSerializer(matches, many=True)
    return Response({
        "success": True,
        "count": len(serializer.data),
        "data": serializer.data
    })


@api_view(["GET"])
@jwt_required
def get_matches_by_sport(request):
    """
    Return matches for a specific sport from now to 7 days ahead
    """
    sport = request.GET.get('sport')

    if not sport:
        return Response({'error': 'Sport parameter is required'}, status=400)

    now = get_utc_now()
    seven_days_later = now + timedelta(days=7)

    matches = Match.objects.filter(
        sport=sport,
        timestamp__gte=now,
        timestamp__lt=seven_days_later
    ).order_by('timestamp')

    serializer = MatchSerializer(matches, many=True)
    return Response({
        "success": True,
        "sport": sport,
        "count": len(serializer.data),
        "data": serializer.data
    })

@api_view(["GET"])
@jwt_required
def get_matches_by_sport_country(request):
    """
    Return matches for a specific sport from now to 7 days ahead
    """
    sport = request.GET.get('sport')

    if not sport:
        return Response({'error': 'Sport parameter is required'}, status=400)
    country = request.GET.get('country')

    if not country:
        return Response({'error': 'Country parameter is required'}, status=400)

    now = get_utc_now()
    seven_days_later = now + timedelta(days=7)

    matches = Match.objects.filter(
        sport=sport,
        country=country,
        timestamp__gte=now,
        timestamp__lt=seven_days_later
    ).order_by('timestamp')

    serializer = MatchSerializer(matches, many=True)
    return Response({
        "success": True,
        "sport": sport,
        "count": len(serializer.data),
        "data": serializer.data
    })


@api_view(["GET"])
@jwt_required
def get_matches_by_date_range(request):
    """
    Return matches for a custom date range
    Query parameters: start_date, end_date (ISO format)
    """
    try:
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({
                "success": False,
                "error": "start_date and end_date parameters are required (ISO format)"
            }, status=400)

        # Parse ISO format dates and make them timezone-aware UTC
        start_date = datetime.fromisoformat(start_date_str.replace('Z', '+00:00'))
        end_date = datetime.fromisoformat(end_date_str.replace('Z', '+00:00'))

        # Ensure timezone-aware
        if start_date.tzinfo is None:
            start_date = start_date.replace(tzinfo=pytz.UTC)
        else:
            start_date = start_date.astimezone(pytz.UTC)

        if end_date.tzinfo is None:
            end_date = end_date.replace(tzinfo=pytz.UTC)
        else:
            end_date = end_date.astimezone(pytz.UTC)

        matches = Match.objects.filter(
            timestamp__gte=start_date,
            timestamp__lt=end_date
        ).order_by('timestamp')

        serializer = MatchSerializer(matches, many=True)
        return Response({
            "success": True,
            "date_range": {
                "start": start_date.isoformat(),
                "end": end_date.isoformat()
            },
            "count": len(serializer.data),
            "data": serializer.data
        })

    except ValueError as e:
        return Response({
            "success": False,
            "error": f"Invalid date format: {str(e)}"
        }, status=400)


@api_view(["GET"])
@jwt_required
def get_all_sports(request):
    """
    Return unique sports from matches
    """
    sports = Match.objects.distinct("sport")
    return Response({
        "success": True,
        "sports": sorted(sports) if sports else []
    })


@api_view(["GET"])
@jwt_required
def get_countries(request):
    sport = request.GET.get('sport')

    if not sport:
        return Response({'error': 'Sport parameter is required'}, status=400)

    # Get unique countries for the specified sport
    countries = Match.objects.filter(
        sport=sport
    ).distinct('country')

    return Response({
        'sport': sport,
        'countries': list(countries),
        'count': len(countries)
    })


@api_view(["GET"])
@jwt_required
def get_match_by_id(request, match_id):
    """
    Get a specific match by match_id
    """
    try:
        match = Match.objects.get(match_id=match_id)
        serializer = MatchSerializer(match)
        return Response({
            "success": True,
            "data": serializer.data
        })
    except Match.DoesNotExist:
        return Response({
            "success": False,
            "error": "Match not found"
        }, status=404)


@api_view(["GET"])
@jwt_required
def get_matches_with_odds(request):
    """
    Return matches that have odds/prices available
    """
    now = get_utc_now()
    seven_days_later = now + timedelta(days=7)

    # Filter matches that have non-empty prices dictionary
    matches = Match.objects.filter(
        timestamp__gte=now,
        timestamp__lt=seven_days_later,
        prices__exists=True,
        prices__ne={}
    ).order_by('timestamp')

    serializer = MatchSerializer(matches, many=True)
    return Response({
        "success": True,
        "count": len(serializer.data),
        "data": serializer.data
    })

