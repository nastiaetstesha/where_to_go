from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Place


def show_main_page(request):
    return render(request, 'start_page.html')


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = [image.image.url for image in place.images.all()]

    return JsonResponse({
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
    })


def places_geojson(request):
    features = []

    for place in Place.objects.all():
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.latitude, place.longitude],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"/places/{place.id}/"
            }
        })

    return JsonResponse({
        "type": "FeatureCollection",
        "features": features
    })
