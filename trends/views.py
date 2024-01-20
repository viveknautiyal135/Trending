from pytrends.request import TrendReq
from django.shortcuts import render

def trending_view(request):
    pytrends = TrendReq(hl='en-US', tz=360)

    # List of wine types
    kw_list = ["Cabernet Sauvignon", "Pinot Noir", "Chardonnay", "Merlot", "Sauvignon Blanc"]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')

    # Interest over time
    interest_over_time_df = pytrends.interest_over_time()

    # Drop the 'isPartial' column
    interest_over_time_df = interest_over_time_df.drop(labels=['isPartial'], axis='columns')

    # Find the top three trending wines
    trending_wines = interest_over_time_df.sum().sort_values(ascending=False).head(3)

    context = {
        'trending_wines': trending_wines,
    }
    return render(request, 'trending.html', context)
