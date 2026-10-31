from django.shortcuts import render


def frontier_view(request):
    return render(request, "frontier/frontier.html")
