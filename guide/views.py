from django.shortcuts import render

def home(request):
    destinations = [
        {'name': 'Goa', 'description': 'A beautiful beach destination in India.', 'image': 'guide/images/goa.png'},
        {'name': 'Paris', 'description': 'The city of lights and love.', 'image': 'guide/images/paris.jpg'},
        {'name': 'Tokyo', 'description': 'A bustling metropolis with rich culture.', 'image': 'guide/images/tokyo.jpg'},
    ]
    return render(request, 'guide/home.html', {'destinations': destinations})

def about(request):
    return render(request, 'guide/about.html')

def tips(request):
    travel_tips = [
        {"title": "Carry a Power Bank", "desc": "Always carry a power bank for your devices."},
        {"title": "Learn Local Language", "desc": "Learn a few phrases in the local language."},
        {"title": "Keep Valuables Secure", "desc": "Keep your valuables safe and secure."},
        {"title": "Stay Hydrated", "desc": "Drink plenty of water and take breaks."},
        {"title": "Research Destination", "desc": "Know your destination before traveling."},
        {"title": "Use Public Transport", "desc": "Explore the city using public transport."},
        {"title": "Try Local Cuisine", "desc": "Enjoy authentic local food."},
        {"title": "Respect Customs", "desc": "Respect local customs and traditions."},
        {"title": "Keep Document Copies", "desc": "Have copies of important documents."},
        {"title": "Stay Connected", "desc": "Keep in touch with family or friends."},
        {"title": "Pack Light", "desc": "Pack smart and light for convenience."},
        {"title": "Be Aware", "desc": "Stay aware of your surroundings."},
        {"title": "Use Travel Apps", "desc": "Use apps for navigation and recommendations."},
        {"title": "Have a Backup Plan", "desc": "Always have a backup plan."},
        {"title": "Carry First-Aid", "desc": "Carry a first-aid kit for emergencies."},
        {"title": "Be Patient", "desc": "Enjoy the journey and be patient."},
        {"title": "Take Photos", "desc": "Capture memories, but enjoy the moment."},
        {"title": "Engage Locals", "desc": "Learn from locals about the culture."},
        {"title": "Stay Safe", "desc": "Trust your instincts and stay safe."},
        {"title": "Research Etiquette", "desc": "Know local etiquette and customs."},
        {"title": "Be Flexible", "desc": "Keep an open mind and be flexible."}
    ]
    return render(request, 'guide/tips.html', {'tips': travel_tips})

def destination(request):
    destinations = [
        {
            'name': 'Goa, India',
            'image': 'guide/images/goa.png',
            'points': [
                "Golden beaches and vibrant nightlife.",
                "Portuguese heritage and colonial architecture.",
                "Best time to visit: November to February.",
                "Try water sports like parasailing and jet skiing.",
                "Enjoy authentic Goan seafood cuisine.",
                "Visit historic churches and forts.",
                "Attend lively beach festivals and parties."
            ]
        },
        {
            'name': 'Paris, France',
            'image': 'guide/images/paris.jpg',
            'points': [
                "Iconic Eiffel Tower and romantic ambiance.",
                "Explore world-class museums like the Louvre.",
                "Stroll through charming neighborhoods like Montmartre.",
                "Enjoy French pastries and gourmet cuisine.",
                "Cruise on the Seine River for scenic views.",
                "Visit Notre-Dame Cathedral and historic sites.",
                "Best time to visit: April to June, September to October."
            ]
        },
        {
            'name': 'Tokyo, Japan',
            'image': 'guide/images/tokiyo.jpg',
            'points': [
                "Blend of tradition and modernity.",
                "Experience cherry blossoms in spring.",
                "Visit ancient temples and shrines.",
                "Explore vibrant districts like Shibuya and Akihabara.",
                "Try sushi, ramen, and street food.",
                "Efficient public transport with JR Pass.",
                "Shop for electronics and fashion."
            ]
        },
        {
            'name': 'Sydney, Australia',
            'image': 'guide/images/sydney.jpg',
            'points': [
                "Iconic Sydney Opera House and Harbour Bridge.",
                "Relax at Bondi and Manly beaches.",
                "Explore The Rocks historic district.",
                "Take a ferry for stunning harbor views.",
                "Enjoy multicultural cuisine and seafood.",
                "Visit Taronga Zoo and Royal Botanic Garden.",
                "Best time to visit: September to November."
            ]
        },
        {
            'name': 'Cape Town, South Africa',
            'image': 'guide/images/capetown.jpeg',
            'points': [
                "Spectacular Table Mountain and cable car rides.",
                "Tour the Cape Winelands for wine tasting.",
                "Visit Robben Island and learn history.",
                "Relax at Camps Bay and Clifton beaches.",
                "Explore the V&A Waterfront for shopping.",
                "See penguins at Boulders Beach.",
                "Best time to visit: March to May."
            ]
        },
        {
            'name': 'New York, USA',
            'image': 'guide/images/newyork.jpg',
            'points': [
                "See the Statue of Liberty and Central Park.",
                "Visit world-class museums and galleries.",
                "Experience Broadway shows and nightlife.",
                "Explore diverse neighborhoods like Brooklyn.",
                "Try classic New York pizza and bagels.",
                "Shop on Fifth Avenue and SoHo.",
                "Best time to visit: Spring and Fall."
            ]
        },
        {
            'name': 'Rome, Italy',
            'image': 'guide/images/rome.jpg',
            'points': [
                "Marvel at the Colosseum and Roman Forum.",
                "Visit Vatican City and St. Peter's Basilica.",
                "Enjoy authentic Italian gelato and pasta.",
                "Stroll through picturesque piazzas.",
                "See ancient ruins and Renaissance art.",
                "Throw a coin in Trevi Fountain.",
                "Best time to visit: April to June, September to October."
            ]
        },
        {
            'name': 'Bangkok, Thailand',
            'image': 'guide/images/bangkok.jpg',
            'points': [
                "Explore ornate temples and palaces.",
                "Shop at vibrant street markets.",
                "Enjoy Thai street food and floating markets.",
                "Cruise the Chao Phraya River.",
                "Experience lively nightlife and rooftop bars.",
                "Visit the Grand Palace and Wat Pho.",
                "Best time to visit: November to February."
            ]
        },
        {
            'name': 'Rio de Janeiro, Brazil',
            'image': 'guide/images/rio.jpg',
            'points': [
                "See Christ the Redeemer statue.",
                "Relax on Copacabana and Ipanema beaches.",
                "Enjoy samba music and Carnival festivities.",
                "Take a cable car to Sugarloaf Mountain.",
                "Explore Tijuca National Park.",
                "Try Brazilian barbecue and street snacks.",
                "Best time to visit: December to March."
            ]
        },
        {
            'name': 'Istanbul, Turkey',
            'image': 'guide/images/istanbul.jpg',
            'points': [
                "Visit Hagia Sophia and Blue Mosque.",
                "Shop at the Grand Bazaar and Spice Market.",
                "Cruise the Bosphorus for city views.",
                "Enjoy Turkish tea and baklava.",
                "Explore historic palaces and museums.",
                "Experience vibrant street life.",
                "Best time to visit: April to June, September to November."
            ]
        },
        {
            'name': 'Dubai, UAE',
            'image': 'guide/images/dubai.jpg',
            'points': [
                "See Burj Khalifa and Dubai Fountain.",
                "Shop at luxury malls and souks.",
                "Relax on Jumeirah Beach.",
                "Go on a desert safari adventure.",
                "Visit Palm Jumeirah and Atlantis.",
                "Enjoy global cuisine and fine dining.",
                "Best time to visit: November to March."
            ]
        },
        {
            'name': 'London, UK',
            'image': 'guide/images/london.jpg',
            'points': [
                "See Big Ben and Buckingham Palace.",
                "Explore world-class museums and galleries.",
                "Enjoy afternoon tea and British cuisine.",
                "Stroll through Hyde Park and gardens.",
                "Shop at Oxford Street and Camden Market.",
                "Experience West End theatre shows.",
                "Best time to visit: May to September."
            ]
        }
    ]
    return render(request, 'guide/destination.html', {'destinations': destinations})

def contact(request):
    return render(request, 'guide/contact.html')

def guides(request):
    return render(request, 'guide/guides.html')