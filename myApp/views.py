from django.shortcuts import render
from django.http import Http404

# Placeholder imagery — swap for real /static/ assets later.
IMG_OAK = "https://www.mepkinapp.org/static/MEPKING/oak-allee4.jpeg"
IMG_HERO = "https://www.mepkinapp.org/static/MEPKING/9.jpeg"
IMG_PORTRAIT = "https://www.mepkinapp.org/static/MEPKING/Homilies.jpg"

# Real grounds map + per-site thumbnails on the live CDN.
MAP_IMAGE = "https://www.mepkinapp.org/static/map/map2.png"
_THUMB = "https://www.mepkinapp.org/static/virtual-tour-images/"


# ── About-hub articles (shown as cards on /home/) ──
ARTICLES = [
    {
        "slug": "who-we-are",
        "title": "Who We Are",
        "icon": "fa-solid fa-people-group",
        "image": IMG_OAK,
        "eyebrow": "Our community",
        "blurb": "A community of Trappist monks in the Cistercian tradition.",
        "body": [
            "Mepkin Abbey is a community of Roman Catholic monks belonging to the Order of Cistercians of the Strict Observance, known as Trappists.",
            "We follow the Rule of Saint Benedict, ordering our days around prayer, sacred reading, and manual labor on land that has been a place of welcome for centuries.",
            "Our 3,200 acres along the Cooper River were once a plantation; today they are held as a sanctuary of beauty, silence, and reconciliation.",
        ],
    },
    {
        "slug": "our-daily-life",
        "title": "Our Daily Life",
        "icon": "fa-solid fa-sun",
        "image": IMG_HERO,
        "eyebrow": "A day at Mepkin",
        "blurb": "Seven times a day we gather to chant the Psalms.",
        "body": [
            "The monastic day begins at 3:00 a.m. with Vigils, the first of seven times the community gathers in the church to pray the Liturgy of the Hours.",
            "Between the hours of prayer, the brothers give themselves to work — tending the gardens, keeping bees, and caring for guests who come seeking quiet.",
            "Meals are taken in silence, often accompanied by reading, so that even the table becomes a place of listening.",
        ],
    },
    {
        "slug": "the-brothers",
        "title": "The Brothers",
        "icon": "fa-solid fa-user",
        "image": IMG_PORTRAIT,
        "eyebrow": "Our monks",
        "blurb": "The men who give their lives to prayer here.",
        "body": [
            "The brothers of Mepkin come from many walks of life, drawn together by a shared desire to seek God in community.",
            "Some are priests, others are not; all are monks, equal in the common life of the cloister.",
            "Through stability — the vow to remain with this community for life — they witness to a faithfulness that the world rarely sees.",
        ],
    },
    {
        "slug": "the-gardens",
        "title": "The Gardens",
        "icon": "fa-solid fa-leaf",
        "image": IMG_OAK,
        "eyebrow": "Sacred ground",
        "blurb": "Botanical gardens that draw visitors from across the South.",
        "body": [
            "The Nancy Bryan Luce Gardens are considered the heart of Mepkin, a landscape of camellias, live oaks, and reflecting ponds overlooking the river.",
            "Designed in the 1930s, the gardens remain a place of contemplation open to all who visit.",
        ],
    },
    {
        "slug": "news-updates",
        "title": "News & Updates",
        "icon": "fa-solid fa-newspaper",
        "image": IMG_HERO,
        "eyebrow": "From the abbey",
        "blurb": "Retreats, liturgies, and seasonal happenings.",
        "body": [
            "Stay connected with the rhythm of life at Mepkin — upcoming retreats, feast-day liturgies, and news from the community.",
            "This is placeholder content; live updates will appear here.",
        ],
    },
    {
        "slug": "support",
        "title": "Support Mepkin",
        "icon": "fa-solid fa-hand-holding-heart",
        "image": IMG_PORTRAIT,
        "eyebrow": "Give",
        "blurb": "Help sustain our life of prayer and hospitality.",
        "body": [
            "Mepkin Abbey is sustained by the work of the brothers and the generosity of friends.",
            "Your support helps preserve this place of prayer, beauty, and welcome for generations to come.",
        ],
    },
]


# ── Virtual-tour sites ──
# `order` = position along the storybook trail; `top`/`left` = percent coords on map2.png.
SITES = [
    {
        "slug": "john-laurens-grave-or-cemetery",
        "title": "John Laurens Cemetery",
        "order": 1, "top": 41.4, "left": 8.0,
        "image": _THUMB + "LaurensCemetery.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "Resting place tied to the Laurens family and Revolutionary history.",
        "body": [
            "This historic cemetery holds the memory of the Laurens family, whose story is woven into the founding of the nation.",
            "John Laurens, an aide to General Washington and an early advocate for emancipation, is remembered among these grounds.",
        ],
    },
    {
        "slug": "meditation-garden-of-truth-and-reconciliation",
        "title": "Meditation Garden",
        "order": 2, "top": 32.2, "left": 8.8,
        "image": _THUMB + "MeditationGarden.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "A quiet garden dedicated to truth and reconciliation.",
        "body": [
            "The Meditation Garden of Truth and Reconciliation invites visitors to sit with the fuller history of this land.",
            "It is a place to remember, to grieve, and to hope for healing across generations.",
        ],
    },
    {
        "slug": "mepkin-abbey-columbarium",
        "title": "Columbarium",
        "order": 3, "top": 52.7, "left": 10.7,
        "image": _THUMB + "Comlumbarium.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "A resting place among the live oaks.",
        "body": [
            "The Columbarium offers a place of rest for the brothers and for friends of the abbey.",
            "Set among ancient live oaks, it is a quiet reminder of the communion of saints that the monastic life keeps before its eyes.",
        ],
    },
    {
        "slug": "luce-gardens",
        "title": "Luce Gardens",
        "order": 4, "top": 49.7, "left": 22.7,
        "image": _THUMB + "LuceCemetery.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "The heart of Mepkin — camellias, oaks, and river views.",
        "body": [
            "The Nancy Bryan Luce Gardens are considered the heart of Mepkin.",
            "Clare Boothe Luce — journalist, playwright, and the first female U.S. Ambassador to Italy — and her husband Henry Luce, founder of Time and Life magazines, purchased Mepkin Plantation in 1936.",
            "They gifted much of the land to found the monastery in 1949, and the gardens remain their living legacy.",
        ],
    },
    {
        "slug": "labyrinth",
        "title": "The Labyrinth",
        "order": 5, "top": 40.3, "left": 47.6,
        "image": _THUMB + "Labyrinth.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "A walking path for prayer and reflection.",
        "body": [
            "The labyrinth invites a slow, meditative walk — a single winding path to a center and back again.",
            "Pilgrims have used such paths for centuries as a way of praying with the body as well as the mind.",
        ],
    },
    {
        "slug": "retreat-center",
        "title": "Retreat Center",
        "order": 6, "top": 48.3, "left": 45.7,
        "image": _THUMB + "Retreat%20Center.jpeg",
        "eyebrow": "Virtual Tour",
        "blurb": "Where guests come to share our silence.",
        "body": [
            "The Retreat Center welcomes individuals and groups seeking a few days of quiet within the monastic rhythm.",
            "Guests are invited to join the brothers in prayer and to rest in the stillness of the grounds.",
        ],
    },
    {
        "slug": "charleston-firefighters-memorial",
        "title": "Firefighters Memorial",
        "order": 7, "top": 45.7, "left": 55.1,
        "image": _THUMB + "Firemans%20Memorial.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "Honoring the Charleston Sofa Super Store nine.",
        "body": [
            "This memorial honors the nine Charleston firefighters who gave their lives in the line of duty in 2007.",
            "It stands as a place of gratitude for all who serve and protect their neighbors.",
        ],
    },
    {
        "slug": "crossroads-or-sacred-heart-of-jesus-statue",
        "title": "Sacred Heart Statue",
        "order": 8, "top": 31.0, "left": 63.7,
        "image": _THUMB + "Crossroads1.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "A crossroads marked by the Sacred Heart of Jesus.",
        "body": [
            "At a quiet crossroads on the grounds stands a statue of the Sacred Heart of Jesus.",
            "It marks a moment to pause, to choose a direction, and to remember the love at the center of the monastic life.",
        ],
    },
    {
        "slug": "reception-center-or-gift-shop",
        "title": "Reception & Gift Shop",
        "order": 9, "top": 61.5, "left": 45.0,
        "image": _THUMB + "Gift%20Shop.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "Begin your visit — and find a memento to take home.",
        "body": [
            "The Reception Center welcomes every visitor to Mepkin and is the best place to begin your tour.",
            "The gift shop offers books, the brothers' garden products, and mementos of your visit.",
        ],
    },
    {
        "slug": "st-claire-walkway",
        "title": "St. Clare Walkway",
        "order": 10, "top": 70.5, "left": 45.0,
        "image": _THUMB + "St%20Clare%20Walkway.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "A shaded path toward the river bluff.",
        "body": [
            "The St. Clare Walkway leads gently through the grounds toward the bluff overlooking the Cooper River.",
            "Named for the companion of St. Francis, it is a favorite route for unhurried prayer.",
        ],
    },
    {
        "slug": "memorial-garden",
        "title": "Memorial Garden",
        "order": 11, "top": 59.3, "left": 70.7,
        "image": _THUMB + "Memorial%20Garden.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "Memorial bricks honoring friends of the abbey.",
        "body": [
            "The Memorial Garden gathers engraved bricks and quiet plantings in honor of those who have loved and supported Mepkin.",
            "It is a place to remember, to give thanks, and to pray.",
        ],
    },
    {
        "slug": "sacred-corridor",
        "title": "Sacred Corridor",
        "order": 12, "top": 49.1, "left": 95.0,
        "image": _THUMB + "Sacred%20Corridor.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "A passage that draws the eye toward prayer.",
        "body": [
            "The Sacred Corridor frames a contemplative passage through the heart of the grounds.",
            "Its lines and light gently lead visitors from the everyday toward the sacred.",
        ],
    },
    {
        "slug": "mepkin-abbey-church",
        "title": "Abbey Church",
        "order": 13, "top": 86.7, "left": 40.9,
        "image": _THUMB + "Mepkin%20Abbey%20Church.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "Where the community gathers seven times each day.",
        "body": [
            "The Abbey Church is the spiritual center of Mepkin, where the brothers gather to chant the Liturgy of the Hours.",
            "Its spare, light-filled design draws the eye upward and the heart inward — architecture in the service of prayer.",
        ],
    },
    {
        "slug": "african-american-cemetery",
        "title": "African-American Cemetery",
        "order": 14, "top": 94.5, "left": 57.0,
        "image": _THUMB + "African%20-%20American%20Cemetery.jpg",
        "eyebrow": "Virtual Tour",
        "blurb": "Remembering the enslaved who lived and labored here.",
        "body": [
            "This cemetery honors the African Americans who lived, labored, and were buried on this land long before the monastery.",
            "Mepkin keeps their memory as part of the fuller, truthful story of these grounds.",
        ],
    },
]

# Lookup for the generic detail page, with each entry tagged by hub.
_PAGES = {}
for _a in ARTICLES:
    _PAGES[_a["slug"]] = {**_a, "back_url": "/home/"}
for _s in SITES:
    _PAGES[_s["slug"]] = {**_s, "back_url": "/virtual-tour/"}


def home(request):
    """Landing page: Mepkin Daily Word."""
    return render(request, 'mepkin-daily-word.html')


def about(request):
    """About-Mepkin hub (reached from the welcome modal 'NO' option)."""
    return render(request, 'about.html', {'articles': ARTICLES})


def virtual_tour(request):
    """Self-guided virtual-tour — storybook game map."""
    sites = sorted(SITES, key=lambda s: s["order"])
    return render(request, 'virtual-tour.html', {'sites': sites, 'map_image': MAP_IMAGE})


def page_detail(request, slug):
    """Generic detail page for any tour site or About article."""
    page = _PAGES.get(slug)
    if page is None:
        raise Http404("Page not found")
    return render(request, 'article.html', {'page': page})


def pray(request):
    """Prayer-request form (dummy — accepts POST and shows a thank-you)."""
    return render(request, 'pray.html', {'submitted': request.method == 'POST'})


def psalter(request):
    """Welcome / Get Started page (reached from the 'proceed' button)."""
    return render(request, 'welcome.html')


def vocation(request):
    """The contemplative-life / calling page."""
    return render(request, 'vocation.html')
