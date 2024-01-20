from django.shortcuts import render
from pytrends.request import TrendReq

def trending_view(request):
    pytrends = TrendReq(hl='en-US', tz=360)
    trending_searches_df = pytrends.trending_searches()
    context = {
        'trending_searches': trending_searches_df.head(10).values.tolist()
    }
    return render(request, 'trending.html', context)
