import streamlit as st
import random
import os

# Page Configuration - Premium Layout
st.set_page_config(page_title="India Travel Explorer", page_icon="✈️", layout="wide")

# ----------------- SESSION STATE RESET LOGIC -----------------
def reset_app():
    st.session_state["user_name"] = ""
    st.session_state["travel_mode"] = "🚂 Train"
    st.session_state["trip_duration"] = 5
    st.session_state["budget"] = 25000
    st.session_state["destination_type"] = "Mountains / Hill Stations"
    st.session_state["hotel_pref"] = "🎒 Pocket-Friendly Backpackers Hostel / Homestay"
    st.session_state["companion"] = "Solo"
    
    if "active_mode" in st.session_state:
        del st.session_state["active_mode"]

# ----------------- CUSTOM CSS FOR MODERN PREMIUM UI -----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(8px);
        margin-bottom: 16px;
        transition: all 0.3s ease-in-out;
    }
    
    div[data-testid="stExpander"]:hover {
        border-color: #00B4D8;
        transform: translateY(-2px);
        box-shadow: 0 12px 40px 0 rgba(0, 180, 216, 0.2);
    }

    .stButton>button {
        border-radius: 12px !important;
        font-weight: 600 !important;
        border: none !important;
        background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%) !important;
        color: white !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0, 180, 216, 0.4);
    }

    div[data-testid="stMetricValue"] {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: #00B4D8 !important;
    }

    .stTextInput>div>div>input, .stSelectbox>div>div {
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }
    
    h1 {
        background: linear-gradient(90deg, #00B4D8, #90E0EF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
    }

    .stAlert {
        border-radius: 12px !important;
        backdrop-filter: blur(5px);
    }
    </style>
""", unsafe_allow_html=True)

# --- BANNER IMAGE AUTOMATIC DISPLAY ---
if os.path.exists("banner.jpg"):
    st.image("banner.jpg", use_container_width=True)

# Header Section
st.title("✈️ India Travel Explorer")
st.caption("✨ Discover handpicked top-rated destinations tailored perfectly to your taste and budget.")
st.write("---")

# ----------------- TRAVEL DATABASE (UPDATED WITH 10 NEW DESTINATIONS) -----------------
destinations = [
    # --- MOUNTAINS / HILL STATIONS ---
    {
        "name": "Manali (Himachal Pradesh)", "type": "Mountains / Hill Stations", "budget": 15000, 
        "highlight": "Snow-capped peaks, Solang Valley adventure, and Rohtang Pass.",
        "food": "🍲 Siddu (local steamed dish), Thukpa, and Trout Fish.",
        "map": "https://www.google.com/maps/search/?api=1&query=Manali+Himachal+Pradesh",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Manali, Alt Life, Local Wooden Homestays (~₹600 - ₹1,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Mountain Top, The Beas River Edge (~₹2,000 - ₹4,000/night)",
            "👑 Premium Luxury Resort / Hotel": "The Himalayan Castle, Manu Allaya Resort (~₹7,000+ /night)"
        }
    },
    {
        "name": "Leh Ladakh (J&K)", "type": "Mountains / Hill Stations", "budget": 45000, 
        "highlight": "Pangong Lake, Magnetic Hill, and stunning mountain passes.",
        "food": "🥟 Momos, Skyu (traditional pasta stew), and Butter Tea.",
        "map": "https://www.google.com/maps/search/?api=1&query=Leh+Ladakh",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Leh, Jimmy's Homestay (~₹800 - ₹2,000/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Singge Palace, Hotel City Heart (~₹3,500 - ₹6,000/night)",
            "👑 Premium Luxury Resort / Hotel": "The Grand Dragon Ladakh (~₹12,000+ /night)"
        }
    },
    {
        "name": "Shimla (Himachal Pradesh)", "type": "Mountains / Hill Stations", "budget": 12000, 
        "highlight": "The Ridge, Mall Road, and historic toy train ride.",
        "food": "🍲 Madra (chana cooked in yogurt), Chha Gosht, and Apple Jams.",
        "map": "https://www.google.com/maps/search/?api=1&query=Shimla+Himachal+Pradesh",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Thira Shimla, Abuzz Backpackers (~₹700 - ₹1,800/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Willow Banks, Bridge View Regency (~₹2,500 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Wildflower Hall, The Oberoi Cecil (~₹15,000+ /night)"
        }
    },
    {
        "name": "Ooty (Tamil Nadu)", "type": "Mountains / Hill Stations", "budget": 18000, 
        "highlight": "Beautiful tea gardens, Nilgiri toy train, and botanical gardens.",
        "food": "🍫 Homemade Chocolates, Ooty Varkey (biscuit), and Fresh Nilgiri Tea.",
        "map": "https://www.google.com/maps/search/?api=1&query=Ooty+Tamil+Nadu",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Ooty, Reflections Guest House (~₹600 - ₹1,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Lakeview, Accord Highland (~₹3,000 - ₹5,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Savoy - IHCL SeleQtions (~₹9,000+ /night)"
        }
    },
    {
        "name": "Munnar (Kerala)", "type": "Mountains / Hill Stations", "budget": 22000, 
        "highlight": "Eravikulam National Park, mist-covered tea estates, and waterfalls.",
        "food": "🍌 Banana Chips, Kerala Puttu with Kadala Curry, and Spices.",
        "map": "https://www.google.com/maps/search/?api=1&query=Munnar+Kerala",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "The Lost Hostel, Tea Garden Homestays (~₹700 - ₹1,600/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Green Spaces, Westwood Riverside (~₹2,800 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Blanket Hotel & Spa, Elixir Hills Suites (~₹8,000+ /night)"
        }
    },
    {
        "name": "Darjeeling (West Bengal)", "type": "Mountains / Hill Stations", "budget": 16000, 
        "highlight": "Tiger Hill sunrise, tea plantations, and views of Mt. Kanchenjunga.",
        "food": "☕ World-famous Darjeeling Tea, Churpee (local cheese), and Thukpa.",
        "map": "https://www.google.com/maps/search/?api=1&query=Darjeeling+West+Bengal",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Hideout Travel Backpackers Hostel, Local Heritage Homestays (~₹600 - ₹1,400/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Central Nirvana, Hotel Dekeling (~₹2,500 - ₹4,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Mayfair Darjeeling (~₹10,000+ /night)"
        }
    },
    {
        "name": "Gulmarg (Kashmir)", "type": "Mountains / Hill Stations", "budget": 35000, 
        "highlight": "Famous Gondola cable car ride, skiing, and snow valleys.",
        "food": "☕ Kashmiri Kahwa Tea, Rogan Josh, and Rista.",
        "map": "https://www.google.com/maps/search/?api=1&query=Gulmarg+Kashmir",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Local Kashmiri Cottage Stays (~₹1,200 - ₹2,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Alpine Ridge, Grand Mumtaz Resorts (~₹4,000 - ₹7,000/night)",
            "👑 Premium Luxury Resort / Hotel": "The Khyber Himalayan Resort & Spa (~₹25,000+ /night)"
        }
    },
    {
        "name": "Nainital (Uttarakhand)", "type": "Mountains / Hill Stations", "budget": 10000, 
        "highlight": "Naini Lake boating, Mall road shopping, and viewpoints.",
        "food": "🍪 Baal Mithai (local sweet), Bhatt ki Churkani, and Aloo ke Gutke.",
        "map": "https://www.google.com/maps/search/?api=1&query=Nainital+Uttarakhand",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Homes Nainital, Lake View Homestays (~₹700 - ₹1,800/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "The Pavilion, Hotel Elphinstone (~₹2,000 - ₹4,000/night)",
            "👑 Premium Luxury Resort / Hotel": "The Manu Maharani, Shervani Hilltop (~₹8,000+ /night)"
        }
    },
    # NEW 1: Shillong
    {
        "name": "Shillong (Meghalaya)", "type": "Mountains / Hill Stations", "budget": 20000, 
        "highlight": "Scotland of the East, Elephant Falls, Shillong Peak, and Umiam Lake.",
        "food": "🥣 Jadoh (rice & meat dish), Dohneiiong, and Bamboo Shoot Pork.",
        "map": "https://www.google.com/maps/search/?api=1&query=Shillong+Meghalaya",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Shillong, The Habitat Shillong (~₹700 - ₹1,600/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Polo Towers, Highwinds (~₹3,000 - ₹5,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Ri Kynjai - Serenity By The Lake (~₹12,000+ /night)"
        }
    },
    # NEW 2: Kodaikanal
    {
        "name": "Kodaikanal (Tamil Nadu)", "type": "Mountains / Hill Stations", "budget": 16000, 
        "highlight": "Kodai Lake, Pillar Rocks, Coaker's Walk, and pine forests.",
        "food": "🍫 Homemade Chocolates, Cheese Pastries, and South Indian Filter Coffee.",
        "map": "https://www.google.com/maps/search/?api=1&query=Kodaikanal+Tamil+Nadu",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Kodaikanal, The Backpackers Cave (~₹650 - ₹1,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Valley View, Villa Retreat (~₹2,800 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "The Carlton Kodaikanal, Tamara Kodai (~₹10,000+ /night)"
        }
    },
    # NEW 3: Gangtok
    {
        "name": "Gangtok (Sikkim)", "type": "Mountains / Hill Stations", "budget": 22000, 
        "highlight": "Nathula Pass, Tsomgo Lake, MG Marg shopping, and Rumtek Monastery.",
        "food": "🥟 Sikkimese Momos, Thukpa, Phagshapa, and Tongba (local drink).",
        "map": "https://www.google.com/maps/search/?api=1&query=Gangtok+Sikkim",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Tag Along Backpackers, Zostel Gangtok (~₹700 - ₹1,800/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Summit Denzong, Golden Crest (~₹3,000 - ₹6,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Mayfair Spa Resort & Casino (~₹12,000+ /night)"
        }
    },

    # --- BEACHES / COASTAL AREAS ---
    {
        "name": "North Goa (Goa)", "type": "Beaches / Coastal Areas", "budget": 20000, 
        "highlight": "Baga & Calangute beaches, thrilling nightlife, water sports, and seafood.",
        "food": "🐟 Goan Fish Curry Rice, Bebinca (layered sweet dessert), and Prawn Balchao.",
        "map": "https://www.google.com/maps/search/?api=1&query=North+Goa",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Happy Panda Hostel, Woke Hostel Arpora (~₹500 - ₹1,200/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Ibis Styles, Calangute Towers (~₹2,500 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "W Goa, Taj Holiday Village Resort (~₹14,000+ /night)"
        }
    },
    {
        "name": "South Goa (Goa)", "type": "Beaches / Coastal Areas", "budget": 22000, 
        "highlight": "Palolem & Colva beaches, peaceful luxury resorts, and historic churches.",
        "food": "🥘 Feni (local drink), Pork Vindaloo, and Grilled Kingfish.",
        "map": "https://www.google.com/maps/search/?api=1&query=South+Goa",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Summer Hostel Palolem, Sea Front Beach Huts (~₹800 - ₹2,000/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Beleza By The Beach, Fairfield by Marriott (~₹4,000 - ₹7,000/night)",
            "👑 Premium Luxury Resort / Hotel": "The Leela Goa, Taj Exotica Resort & Spa (~₹18,000+ /night)"
        }
    },
    {
        "name": "Andaman Islands", "type": "Beaches / Coastal Areas", "budget": 55000, 
        "highlight": "Scuba diving in Havelock, Radhanagar beach, and cellular jail history.",
        "food": "🦞 Fresh Lobster, Crab Masala, and Coastal Fruit Chats.",
        "map": "https://www.google.com/maps/search/?api=1&query=Andaman+Islands",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Green Valley Resort Havelock, Local Beach Cabins (~₹1,000 - ₹2,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Symphony Palms Beach Resort (~₹4,500 - ₹8,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Taj Exotica Resort & Spa Havelock, Barefoot at Havelock (~₹20,000+ /night)"
        }
    },
    {
        "name": "Gokarna (Karnataka)", "type": "Beaches / Coastal Areas", "budget": 12000, 
        "highlight": "Om Beach, peaceful Mahabaleshwar temple, and beach trekking.",
        "food": "🍕 Seafood Pizza at Namaste Cafe, Gadbad Ice Cream, and South Indian Thali.",
        "map": "https://www.google.com/maps/search/?api=1&query=Gokarna+Karnataka",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Gokarna, Trippr Gokarna Beach Hostel (~₹600 - ₹1,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Namaste Sanjeevini, Kahani Paradise (~₹2,500 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "CGH Earth - SwaSwara (~₹15,000+ /night)"
        }
    },
    {
        "name": "Puducherry", "type": "Beaches / Coastal Areas", "budget": 15000, 
        "highlight": "French colony streets, Promenade beach, and Auroville spiritual center.",
        "food": "🥐 French Croissants, Ratatouille, and wood-fired Pizzas.",
        "map": "https://www.google.com/maps/search/?api=1&query=Puducherry",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Ostello Bangalore Puducherry, Nomad House (~₹500 - ₹1,300/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Shenbaga Hotel, Atithi TGI Grand (~₹3,000 - ₹5,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Palais de Mahé - CGH Earth (~₹10,000+ /night)"
        }
    },
    # NEW 4: Varkala
    {
        "name": "Varkala (Kerala)", "type": "Beaches / Coastal Areas", "budget": 14000, 
        "highlight": "Dramatic cliffside beach view, Janardanaswamy Temple, and surfing.",
        "food": "🐟 Fresh Seafood Barbecue, Kerala Parotta, and Avial.",
        "map": "https://www.google.com/maps/search/?api=1&query=Varkala+Kerala",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Varkala, HosteLaVie (~₹600 - ₹1,400/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Clafouti Beach Resort, Krishnatheeram (~₹2,500 - ₹4,500/night)",
            "👑 Premium Luxury Resort / Hotel": "The Gateway Hotel Varkala (~₹8,000+ /night)"
        }
    },
    # NEW 5: Puri
    {
        "name": "Puri (Odisha)", "type": "Beaches / Coastal Areas", "budget": 9000, 
        "highlight": "Jagannath Temple, Golden Beach sunset, and Chilika Lake day trip.",
        "food": "🍛 Mahaprasad at Temple, Chhena Poda (cheese dessert), and Prawn Curry.",
        "map": "https://www.google.com/maps/search/?api=1&query=Puri+Odisha",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Puri, Beachside Lodges (~₹500 - ₹1,200/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Sonar Bangla, Mayfair Heritage (~₹2,200 - ₹4,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Mayfair Waves Puri (~₹9,000+ /night)"
        }
    },
    # NEW 6: Daman
    {
        "name": "Daman (Daman & Diu)", "type": "Beaches / Coastal Areas", "budget": 11000, 
        "highlight": "Devka Beach, Moti Daman Fort, and colonial Portuguese architecture.",
        "food": "🦐 Portuguese Style Fish Fry, Chicken Bullet, and Local Seafood.",
        "map": "https://www.google.com/maps/search/?api=1&query=Daman+India",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Sea View Guest House, Local Homestays (~₹600 - ₹1,300/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Miramar, Gold Beach Resort (~₹2,500 - ₹4,500/night)",
            "👑 Premium Luxury Resort / Hotel": "The Deltin Daman (~₹8,500+ /night)"
        }
    },

    # --- HISTORICAL / CULTURAL SITES ---
    {
        "name": "Jaipur (Rajasthan)", "type": "Historical / Cultural Sites", "budget": 12000, 
        "highlight": "Hawa Mahal, Amer Fort, City Palace, and shopping for traditional crafts.",
        "food": "🫓 Dal Baati Churma, Pyaaz Kachori, and Mawa Kachori.",
        "map": "https://www.google.com/maps/search/?api=1&query=Jaipur+Rajasthan",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "The Moustache Hostel, Zostel Jaipur (~₹500 - ₹1,200/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Umaid Bhawan Hotel, Hotel Pearl Palace (~₹2,000 - ₹4,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Rambagh Palace, The Oberoi Rajvilas (~₹22,000+ /night)"
        }
    },
    {
        "name": "Agra (Uttar Pradesh)", "type": "Historical / Cultural Sites", "budget": 7000, 
        "highlight": "The iconic Taj Mahal, Agra Fort, and Fatehpur Sikri ruins.",
        "food": "🍯 World-famous Agra Petha (Angoori & Kesar), and Bedai-Kachori.",
        "map": "https://www.google.com/maps/search/?api=1&query=Taj+Mahal+Agra",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Agra, Friends Home Stay (~₹400 - ₹1,000/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Taj Resorts, Howard Plaza The Fern (~₹2,000 - ₹3,500/night)",
            "👑 Premium Luxury Resort / Hotel": "The Oberoi Amarvilas, ITC Mughal (~₹12,000+ /night)"
        }
    },
    {
        "name": "Udaipur (Rajasthan)", "type": "Historical / Cultural Sites", "budget": 22000, 
        "highlight": "Lake Pichola boating, grand City Palace, and Jag Mandir.",
        "food": "🍲 Lal Maas (spicy mutton), Mewari Khichdi, and Mirchi Bada.",
        "map": "https://www.google.com/maps/search/?api=1&query=Udaipur+Rajasthan",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Udaipur, Bunkyard Hostel (~₹500 - ₹1,300/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Mewar Castle, Lake Pichola Hotel (~₹2,500 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "The Taj Lake Palace, The Leela Palace Udaipur (~₹25,000+ /night)"
        }
    },
    {
        "name": "Varanasi (Uttar Pradesh)", "type": "Historical / Cultural Sites", "budget": 8000, 
        "highlight": "Subah-e-Banaras ghats, famous Ganga Aarti, and Kashi Vishwanath temple.",
        "food": "🍃 Banarasi Paan, Tamatar Chaat, Malaiyo (seasonal sweet), and Kachori Sabzi.",
        "map": "https://www.google.com/maps/search/?api=1&query=Varanasi+Uttar+Pradesh",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "GoStops Varanasi, International Travellers Hostel (~₹450 - ₹1,100/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Alka Hotel (Ghat view), Hotel Ganges View (~₹2,000 - ₹4,000/night)",
            "👑 Premium Luxury Resort / Hotel": "BrijRama Palace Heritage Hotel (~₹12,000+ /night)"
        }
    },
    {
        "name": "Amritsar (Punjab)", "type": "Historical / Cultural Sites", "budget": 9000, 
        "highlight": "The holy Golden Temple, Jallianwala Bagh, and Wagah Border ceremony.",
        "food": "🫓 Amritsari Kulcha with lots of butter, Guru ka Langar, and tall glass of Lassi.",
        "map": "https://www.google.com/maps/search/?api=1&query=Golden+Temple+Amritsar",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "InSights Hostel, Local Serai Stay near Temple (~₹400 - ₹1,000/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel HK Clarks Inn, Ramada by Wyndham (~₹2,500 - ₹4,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Taj Swarna, Welcomhotel by ITC Hotels (~₹7,500+ /night)"
        }
    },
    # NEW 7: Hampi
    {
        "name": "Hampi (Karnataka)", "type": "Historical / Cultural Sites", "budget": 10000, 
        "highlight": "UNESCO Heritage ruins, Virupaksha Temple, Stone Chariot, and boulder landscape.",
        "food": "🍌 Banana Flower Curry, South Indian Thali, and Herbal Teas.",
        "map": "https://www.google.com/maps/search/?api=1&query=Hampi+Karnataka",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Gobi Guest House, Hippie Island Cottages (~₹400 - ₹1,200/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Heritage Resort Hampi, Hotel Malligi (~₹2,500 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Evolve Back Hampi (~₹20,000+ /night)"
        }
    },
    # NEW 8: Jaisalmer
    {
        "name": "Jaisalmer (Rajasthan)", "type": "Historical / Cultural Sites", "budget": 18000, 
        "highlight": "Golden Fort, Thar Desert safari, Sam Sand Dunes night camping.",
        "food": "🍲 Ker Sangri, Gatte ki Sabzi, and Makhania Lassi.",
        "map": "https://www.google.com/maps/search/?api=1&query=Jaisalmer+Rajasthan",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Jaisalmer, Desert Backpackers (~₹500 - ₹1,300/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Pleasant Haveli, Royal Desert Camp (~₹2,500 - ₹5,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Suryagarh Jaisalmer (~₹18,000+ /night)"
        }
    },
    # NEW 9: Mysuru
    {
        "name": "Mysuru (Karnataka)", "type": "Historical / Cultural Sites", "budget": 11000, 
        "highlight": "Grand Mysore Palace, Chamundi Hill, Brindavan Gardens, and Silk markets.",
        "food": "🧈 Mysore Pak (ghee sweet), Mysore Masala Dosa, and Filter Coffee.",
        "map": "https://www.google.com/maps/search/?api=1&query=Mysuru+Karnataka",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Morpheus Hostel, Local Heritage Homestays (~₹500 - ₹1,200/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Royal Orchid Metropole, Roopa (~₹2,200 - ₹4,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Grand Mercure Mysore, Lalitha Mahal Palace (~₹8,000+ /night)"
        }
    },

    # --- ADVENTURE / WILDLIFE ---
    {
        "name": "Rishikesh (Uttarakhand)", "type": "Adventure / Wildlife", "budget": 8000, 
        "highlight": "White-water river rafting, bungee jumping, and riverside camping.",
        "food": "🥤 Organic Smoothies, Ayurvedic Food in Cafes, and Chole Bhature.",
        "map": "https://www.google.com/maps/search/?api=1&query=Rishikesh+Uttarakhand",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Zostel Rishikesh, Skyard Hostel, Riverside Camps (~₹600 - ₹1,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Hotel Grand Ganga, Aloha On The Ganges (~₹3,000 - ₹6,000/night)",
            "👑 Premium Luxury Resort / Hotel": "Ananda In The Himalayas, Taj Rishikesh (~₹20,000+ /night)"
        }
    },
    {
        "name": "Jim Corbett (Uttarakhand)", "type": "Adventure / Wildlife", "budget": 15000, 
        "highlight": "Jungle safari, riverside camping, and rich wildlife viewing.",
        "food": "🍲 Kumaoni Raita, Bal Mithai, and local Pahadi Saag (Kapaa).",
        "map": "https://www.google.com/maps/search/?api=1&query=Jim+Corbett+National+Park",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "Local Eco Wildlife Lodges / Tents (~₹1,200 - ₹2,500/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Corbett Trekker Camp, Tiger Camp Resort (~₹3,500 - ₹5,500/night)",
            "👑 Premium Luxury Resort / Hotel": "The Taj Corbett Resort & Spa (~₹10,000+ /night)"
        }
    },
    # NEW 10: Ranthambore
    {
        "name": "Ranthambore (Rajasthan)", "type": "Adventure / Wildlife", "budget": 17000, 
        "highlight": "Royal Bengal Tiger Safaris, ancient Ranthambore Fort, and Padam Talao.",
        "food": "🫓 Rajasthani Thali, Churma Ladoo, and Bajra Roti.",
        "map": "https://www.google.com/maps/search/?api=1&query=Ranthambore+National+Park",
        "hotels": {
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay": "The Backpacker Nest, Wildlife Homestays (~₹800 - ₹1,800/night)",
            "🏨 Comfort Standard Hotel (2-3 Star)": "Tiger Moon Resort, Ranthambore Regency (~₹3,000 - ₹5,500/night)",
            "👑 Premium Luxury Resort / Hotel": "Aman-i-Khas, The Oberoi Vanyavilas (~₹35,000+ /night)"
        }
    }
]

default_food = "🍱 Try local traditional Thali and famous street food stalls nearby!"
default_hotel = "🏨 Great budget stays and guest houses are available near the city center starting from ₹1,200/night."

# Dashboard Layout (Left & Right Split)
col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.subheader("🔍 Set Your Travel Profile")
    
    user_name = st.text_input("What is your name?", key="user_name")
    
    travel_mode = st.selectbox(
        "Preferred Mode of Transport:",
        ["🚂 Train", "✈️ Flight", "🚗 Road Trip / Car"],
        key="travel_mode"
    )
    
    trip_duration = st.slider("Trip Duration (in Days):", min_value=1, max_value=15, value=5, key="trip_duration")
    st.write("---")
    
    budget = st.slider("Select Max Budget (per person in ₹):", min_value=5000, max_value=100000, value=25000, step=5000, key="budget")
    st.metric(label="Your Budget Limit", value=f"₹{budget:,}")
    
    destination_type = st.selectbox(
        "Type of Destination:",
        ["Mountains / Hill Stations", "Beaches / Coastal Areas", "Historical / Cultural Sites", "Adventure / Wildlife"],
        key="destination_type"
    )
    
    hotel_preference = st.selectbox(
        "🏨 Choose Hotel Preference:",
        [
            "🎒 Pocket-Friendly Backpackers Hostel / Homestay", 
            "🏨 Comfort Standard Hotel (2-3 Star)", 
            "👑 Premium Luxury Resort / Hotel"
        ],
        key="hotel_pref"
    )
    
    companion = st.radio(
        "Traveling With:",
        ["Solo", "Friends", "Family", "Couple / Partner"],
        horizontal=True,
        key="companion"
    )
    
    st.write("---")
    
    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
    with btn_col1:
        search_clicked = st.button("🔍 Search", use_container_width=True)
    with btn_col2:
        surprise_clicked = st.button("🎲 Surprise", use_container_width=True)
    with btn_col3:
        st.button("🔄 Reset", on_click=reset_app, use_container_width=True)

with col2:
    display_name = user_name if user_name else "Traveler"
    st.subheader(f"🎯 Recommendations for {display_name}")
    st.caption(f"🎒 Planning a {trip_duration}-day trip via {travel_mode}")
    
    matching_places = [place for place in destinations if place["type"] == destination_type and place["budget"] <= budget]
    
    if search_clicked:
        st.session_state['active_mode'] = 'search'
    elif surprise_clicked:
        st.session_state['active_mode'] = 'surprise'

    current_mode = st.session_state.get('active_mode', None)

    if current_mode == 'search':
        if matching_places:
            st.success(f"Hey {display_name}, we found {len(matching_places)} incredible places for your {companion} trip!")
            
            for place in matching_places:
                with st.expander(f"📍 {place['name']} — (~₹{place['budget']:,})"):
                    st.write(f"**Best Suited For:** {companion} Trip")
                    st.write(f"**Key Highlights:** {place['highlight']}")
                    
                    st.markdown("### 🛏️ Stay & Accommodation Suggestion")
                    destination_hotels = place.get("hotels", {})
                    chosen_hotel_info = destination_hotels.get(hotel_preference, default_hotel)
                    st.info(f"👉 **Option for {hotel_preference}:**\n\n{chosen_hotel_info}")
                    
                    st.markdown("### 🍱 Local Food Specialities")
                    st.write(place.get("food", default_food))
                    
                    st.markdown("### 🗺️ Interactive Route Map")
                    st.link_button("🌐 View Live Location on Google Maps 📍", place.get("map", f"https://www.google.com/maps/search/?api=1&query={place['name']}"))
        else:
            st.warning(f"Sorry {display_name}! No destinations found in this budget. Try adjusting the slider! 💰")
            
    elif current_mode == 'surprise':
        all_budget_friendly = [place for place in destinations if place["budget"] <= budget]
        if all_budget_friendly:
            lucky_place = random.choice(all_budget_friendly)
            st.balloons()
            st.info(f"🎲 {display_name}, here is a perfect spot for your next adventure:")
            
            st.subheader(f"📍 {lucky_place['name']}")
            st.write(f"**Category:** {lucky_place['type']}")
            st.write(f"**Estimated Cost:** ~₹{lucky_place['budget']:,} per person")
            st.write(f"**Highlights:** {lucky_place['highlight']}")
            
            st.markdown("### 🛏️ Stay & Accommodation Suggestion")
            lucky_destination_hotels = lucky_place.get("hotels", {})
            lucky_hotel_info = lucky_destination_hotels.get(hotel_preference, default_hotel)
            st.info(f"👉 **Option for {hotel_preference}:**\n\n{lucky_hotel_info}")
            
            st.markdown("### 🍱 Local Food Specialities")
            st.write(lucky_place.get("food", default_food))
            
            st.markdown("### 🗺️ Interactive Route Map")
            st.link_button("🌐 View Live Location on Google Maps 📍", lucky_place.get("map", f"https://www.google.com/maps/search/?api=1&query={lucky_place['name']}"))
        else:
            st.warning("Even a surprise trip needs a bit more budget! Please increase the slider limit. 💰")
            
    else:
        st.info("👋 Welcome! Fill your travel details on the left and click **Search** or **Surprise** to see fresh recommendations.")