from goods.models import Products
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline
)


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    search_columns = ("name", "description")
    vector = SearchVector(*search_columns)
    query = SearchQuery(query)

    data = Products.objects.annotate(
        rank=SearchRank(vector, query)
    ).filter(rank__gt=0).order_by('-rank')

    span_style = '"background-color: yellow;"'
    for search_table in search_columns:
        kwargs = {search_table + '_line':
                  SearchHeadline(
                      search_table,
                      query,
                      start_sel=f"<span style={span_style}>",
                      stop_sel="</span>",
                  )}

        data = data.annotate(**kwargs)

    return data
