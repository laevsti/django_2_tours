import random

from django.shortcuts import render
from django.views import View

from tours.data import title, subtitle, description, departures, tours


class MainView(View):
    def get(self, request, *args, **kwargs):
        rand_list = random.sample(range(1, len(tours)), 6)
        content = {'title': title,
                   'subtitle': subtitle,
                   'description': description,
                   'departures': departures,
                   'tours_data': list(map(lambda x: [tours[x]['title'],
                                      tours[x]['description'],
                                      tours[x]['departure'],
                                      tours[x]['picture'],
                                      tours[x]['price'],
                                      tours[x]['stars'],
                                      tours[x]['country'],
                                      tours[x]['nights'],
                                      tours[x]['date'],
                                      x], rand_list))
                   }
        return render(request, 'index.html', {'content': content})


class TourView(View):
    def get(self, request, tour_id):
        content = {'title': title,
                   'subtitle': subtitle,
                   'description': description,
                   'departures': departures,
                   'tours_title': tours[tour_id]['title'] + ' ' + int(tours[tour_id]['stars']) * '★',
                   'tours_description': tours[tour_id]['description'],
                   'tours_departure': tours[tour_id]['departure'],
                   'tours_picture': tours[tour_id]['picture'],
                   'tours_price': tours[tour_id]['price'],
                   'tours_stars': tours[tour_id]['stars'],
                   'tours_country': tours[tour_id]['country'],
                   'tours_nights': tours[tour_id]['nights'],
                   'tours_date': tours[tour_id]['date'],
                   'tours_departure_rus': departures[tours[tour_id]['departure']],
                   }
        return render(request, 'tour.html', {'content': content})


class DepartureView(View):
    def get(self, request, departure):
        # tours counter:
        c = 0
        # min/max tour price:
        price_list = []
        # min/max nights qty:
        nights_list = []
        # tours_data_list:
        tours_data_list = []
        for i in tours:
            if tours[i]['departure'] == departure:
                price_list.append(tours[i]['price'])
                nights_list.append(tours[i]['nights'])
                tours_data_list.append([tours[i]['title'],
                                       tours[i]['description'],
                                       tours[i]['picture'], i])
                c += 1
        # min, max price:
        min_price = min(price_list)
        max_price = max(price_list)
        # min, max nights:
        min_nights = min(nights_list)
        max_nights = max(nights_list)

        content = {'title': title,
                   'subtitle': subtitle,
                   'description': description,
                   'departures': departures,
                   'departure_rus': departures[departure],
                   'avail_tours_qty': c,
                   'min_price': min_price,
                   'max_price': max_price,
                   'min_nights': min_nights,
                   'max_nights': max_nights,
                   'tours_data_list': tours_data_list
                   }
        return render(request, 'departure.html', {'content': content})
