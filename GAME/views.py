from django.http import HttpResponse



def index(request):
    line1 = '<h1 style="text-align:center">DanceSystem</h1>'
    line4 = '<a href="/play/" style="text-align:center">A NEW STYLE OF LIFE...</a>'
    line3 = '<hr>'
    line2 = '<img src="https://images.pexels.com/photos/8976260/pexels-photo-8976260.jpeg?cs=srgb&dl=pexels-mbardo-8976260.jpg&fm=jpg" height=800>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<img src=https://burst.shopify.com/photos/stackable-chips-in-lines?c=wallpapers=auto>'
    return HttpResponse(line1 + line2)
