from japronto import Application
from ircalevents import get_day_events, get_month_events, get_year_events
import json
app = Application()

async def get_events_year(request):
    result = await get_year_events(request.match_dict['year'])
    return request.Response(text=json.dumps(result, ensure_ascii=False),
                                encoding='utf-8', mime_type='application/json')

async def get_events_month(request):
    result = await get_month_events(request.match_dict['year'], request.match_dict['month'])
    return request.Response(text=json.dumps(result, ensure_ascii=False),
                                encoding='utf-8', mime_type='application/json')

async def get_events_day(request):
    result = await get_day_events(request.match_dict['year'], request.match_dict['month'],
                                    request.match_dict['day'])
    return request.Response(text=json.dumps(result, ensure_ascii=False),
                                encoding='utf-8', mime_type='application/json')

routes = app.router
routes.add_route('/events/{year}', get_events_year, 'GET')
routes.add_route('/events/{year}/{month}', get_events_month, 'GET')
routes.add_route('/events/{year}/{month}/{day}', get_events_day, 'GET')

app.run(host='127.0.0.1', port=5000)
