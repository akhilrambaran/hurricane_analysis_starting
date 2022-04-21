from collections import defaultdict

# names of hurricanes
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# months of hurricanes
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# years of hurricanes
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# areas affected by each hurricane
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["Lesser Antilles", "The Bahamas", "United States East Coast", "Atlantic Canada"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["Southeastern United States", "Northeastern United States", "Southwestern Quebec"],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    ["Central America", "United States Gulf Coast (especially Florida Panhandle)"],
]

# damages (USD($)) of hurricanes
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# deaths for each hurricane
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]

## 1 - Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}

# Filter and Convert Amounts from list
updated_list = []


def damages_convert(lst):
    for amount in lst:
        if "M" in amount:
            updated_list.append(float(amount.strip("M")) * conversion["M"])
        elif "B" in amount:
            updated_list.append(float(amount.strip("B")) * conversion["B"])
        else:
            updated_list.append(amount)
    return updated_list


# Update damages
damages = damages_convert(damages)

# 2 - Create Hurricane Summary
hurricane_summary = {}


def hurricanes_dict(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths
):
    generate_hurricanes_dict(
        names, months, years, max_sustained_winds, areas_affected, damages, deaths
    )
    # print(f'Hurricane Summary: {hurricane_summary}\n')


def generate_hurricanes_dict(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths
):
    for i in range(len(names)):
        hurricane_summary[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": damages[i],
            "Deaths": deaths[i],
        }
    return hurricane_summary


# Construct Hurricane Dictionary Function
hurricanes_dict(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths
)

## 3 - Organizing Dictionary by Year
hurricanes_by_year = []


def hurricanes_sorted_by_year(year):
    sorted_by_year(year)
    print(f"Hurricanes sorted by year:{hurricanes_by_year} \n")


def sorted_by_year(year):
    for name in hurricane_summary:
        if hurricane_summary[name]["Year"] == year:
            hurricanes_by_year.append(hurricane_summary[name])
    return hurricanes_by_year


# create a new dictionary of hurricanes with year and key
hurricanes_sorted_by_year(1932)

# 4 - Counting Damaged Areas
areas_affected_count = defaultdict(int)


def areas_affected_counter(areas):
    areas_affected_check(areas)
    print(f"Count of Areas affected by Hurricanes: {areas_affected_count}\n")


def areas_affected_check(areas):
    for name in hurricane_summary:
        for areas in hurricane_summary[name]["Areas Affected"]:
            areas_affected_count[areas] += 1
    return areas_affected_count


# create dictionary of areas to store the number of hurricanes involved in
areas_affected_counter(areas_affected)

# 5
# Calculating Maximum Hurricane Count
def frequent_affected_area(arr):
    # Finding the most affected area using max function with count of each element as comparison
    max_area = max(list(arr), key=list(arr).count)
    max_area_count = arr[max_area]

    return max_area, max_area_count


# find most frequently affected area and the number of hurricanes involved in
print(
    f"Most affected area and amount of hurricanes exprienced: {frequent_affected_area(areas_affected_count)} \n"
)

## 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(dead, hurr_dict):
    max_deaths = max(dead)
    # Retrieving hurricane info using max_deaths as criteria
    deadliest_cane = [
        hurr_dict[cane] for cane in hurr_dict if hurr_dict[cane]["Deaths"] == max_deaths
    ]

    return deadliest_cane


# find highest mortality hurricane and the number of deaths
deadliest_cane = deadliest_hurricane(deaths, hurricane_summary)
print(f"Deadliest Hurricane: {deadliest_cane}\n")

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

mortality_category = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}


def mortality_sort(hurricane):
    # range used to filter hurricanes by death for new dictionary
    for cane in hurricane:
        if hurricane[cane]["Deaths"] == mortality_category[0]:
            mortality_category[0].append(hurricane[cane])
        elif hurricane[cane]["Deaths"] in range(0, 101):
            mortality_category[1].append(hurricane[cane])
        elif hurricane[cane]["Deaths"] in range(101, 501):
            mortality_category[2].append(hurricane[cane])
        elif hurricane[cane]["Deaths"] in range(501, 1001):
            mortality_category[3].append(hurricane[cane])
        elif hurricane[cane]["Deaths"] in range(1001, 10001):
            mortality_category[4].append(hurricane[cane])
        elif hurricane[cane]["Deaths"] > 10000:
            mortality_category[5].append(hurricane[cane])

    return mortality_category


# categorize hurricanes in new dictionary with mortality severity as key
mort_cat = mortality_sort(hurricane_summary)
print(f"Hurricane with highest morality rating: {mort_cat[5]}\n")

# 8 Calculating Hurricane Maximum Damage
def max_damage_and_cost(cost, hurr_dict):
    # filtering updated damages for numbers only
    costs = [x for x in cost if isinstance(x, float)]
    max_cost = max(costs)
    # Retrieving hurricane info using max_cost as criteria
    most_damage_cane = [
        hurr_dict[cane] for cane in hurr_dict if hurr_dict[cane]["Damage"] == max_cost
    ]
    return most_damage_cane


# find highest mortality hurricane and the number of deaths
most_damage_cane = max_damage_and_cost(damages, hurricane_summary)
print(f"Costliest Hurricane: {most_damage_cane}\n")

# find highest damage inducing hurricane and its total cost
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
damage_category = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}


def damage_sort(hurricane):
    for cane in hurricane:
        damage_amt = hurricane[cane]["Damage"]
        # isinstance function used to check for "Damages not recorded"
        if isinstance(damage_amt, str):
            damage_category[0].append(hurricane[cane])
        elif damage_amt > damage_scale[0] and damage_amt <= damage_scale[1]:
            damage_category[1].append(hurricane[cane])
        elif damage_amt > damage_scale[1] and damage_amt <= damage_scale[2]:
            damage_category[2].append(hurricane[cane])
        elif damage_amt > damage_scale[2] and damage_amt <= damage_scale[3]:
            damage_category[3].append(hurricane[cane])
        elif damage_amt > damage_scale[3] and damage_amt <= damage_scale[4]:
            damage_category[4].append(hurricane[cane])
        elif damage_amt > damage_scale[4]:
            damage_category[5].append(hurricane[cane])
    return damage_category


# categorize hurricanes in new dictionary with damage severity as key
dmge_cat = damage_sort(hurricane_summary)
print(f"Hurricanes with highest damage rating: {dmge_cat[5]}")
