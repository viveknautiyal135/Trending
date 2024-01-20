from pytrends.request import TrendReq
from django.shortcuts import render

def trending_view(request):
    selected_region = request.GET.get('region')  # Get the selected region from the request

    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["Cabernet Sauvignon", "Pinot Noir", "Chardonnay", "Merlot", "Sauvignon Blanc"]

    # Check if a region is selected, otherwise default to 'US'
    if not selected_region:
        selected_region = 'US'

    pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo=selected_region, gprop='')
    interest_over_time_df = pytrends.interest_over_time()

    # Dropping 'isPartial' column
    if 'isPartial' in interest_over_time_df.columns:
        interest_over_time_df = interest_over_time_df.drop('isPartial', axis=1)

    # Sum up and sort values to get top 3
    trending_wines = interest_over_time_df.sum().sort_values(ascending=False).head(3)

    context = {
        'selected_region': selected_region,
        'trending_wines': trending_wines.to_dict(),
    }
    return render(request, 'trending.html', context)
