# Mapping allowing different names for teams to be converted to be conform to database naming for team names
NAME_MAPPING = {
    'as roma': 'roma',
    'west brom': 'west bromwich albion',
    'verona': 'hellas verona',
    'chievo': 'chievoverona',
    'deportivo': 'deportivo la coruna',
    'betis': 'real betis',
    'psg': 'paris saint germain',
    'paris': 'paris saint germain',
    'as monaco': 'monaco',
    'fc köln': 'fc cologne',
    'fc koln': 'fc cologne',
    'rb leipzig': 'leipzig',
    'stuttgart': 'vfb stuttgart',
    'psv': 'psv eindhoven',
    'sm caen': 'caen',
    'pordenone': 'pordenone calcio',
    'frankfurt': 'eintracht frankfurt',
    'afc bournemouth': 'bournemouth',
    'west ham united': 'west ham',
    'tottenham hotspur': 'tottenham',
    'ssc napoli': 'napoli',
    'brighton & hove albion': 'brighton',
    'huddersfield town': 'huddersfield',
    'inter': 'inter milan',
    'borussia dortmund': 'dortmund',
    "borussia m'gladbach": 'borussia monchengladbach',
    'monchengladbach': 'borussia monchengladbach',
    'rasenballsport leipzig': 'leipzig',
    'saint-etienne': 'saint etienne',
    'swansea city': 'swansea',
    'al-jazira': 'al jazira',
    'fc groningen': 'groningen',
    'akhisar belediye genclik ve spor': 'akhisar genclik spor',
    'leeds': 'leeds united',
    'waregem': 'zulte waregem',
    'zulte-waregem': 'zulte waregem',
    'zenit st. petersburg': 'zenit st petersburg',
    'zenit': 'zenit st petersburg',
    'appolon fc': 'apollon limassol',
    'hnk rijeka': 'rijeka',
    'fc twente': 'twente',
    'real murcia': 'murcia',
    'roda jc kerkrade': 'roda',
    'roda jc': 'roda',
    'hamburg': 'hamburger sv',
    'qarabag': 'qarabag fk',
    'sporting': 'sporting cp',
    'formentera': 'sd formentera',
    'celta': 'celta vigo',
    'olympique marseille': 'marseille',
    'olympique lyonnais': 'lyon',
    'om': 'marseille',
    'ol': 'lyon',
    'aca': 'ajaccio',
    'asm': 'monaco',
    'aja': 'auxerre',
    'bor': 'bordeaux',
    'lil': 'lille',
    'fcn': 'nantes',
    'nic': 'nice',
    'rcl': 'lens',
    'str': 'rennes',
    'stade rennais': 'rennes',
    'se': 'saint etienne',
    'soc': 'sochaux',
    'tfc': 'toulouse',
    'est': 'troyes',
    'wolverhampton wanderers': 'wolverhampton',
    'wolves': 'wolverhampton',
    'sc freiburg': 'freiburg',
    'fc barcelona': 'barcelona',
    'cardiff city': 'cardiff',
    'newport county': 'newport',
    'peterborough united': 'peterborough',
    'yeovil town': 'yeovil',
    'barca': 'barcelona',
    'leicester': 'leicester city',
    'ogc nice': 'nice',
    'equipe de france': 'france',
    'man u': 'manchester united',
    'man city': 'manchester city',
    'spurs': 'tottenham',
    'gunners': 'arsenal',
    'liverpool fc': 'liverpool',
    'lille osc': 'lille',
    'losc': 'lille',
    'fc nantes': 'nantes',
    'bourg-peronnas': 'bourg peronnas',
    'porto': 'fc porto',
    'man united': 'manchester united',
    'clarets': 'burnley',
    'blues': 'chelsea',
    'pensioners': 'chelsea',
    'eagles': 'crystal palace',
    'toffees': 'everton',
    'tigers': 'hull city',
    'foxes': 'leicester city',
    'reds': 'liverpool',
    'red devils': 'manchester united',
    'citizens': 'manchester city',
    'magpies': 'newcastle united',
    'saints': 'southampton',
    'potters': 'stoke city',
    'swans': 'swansea',
    'baggies': 'west bromwich albion',
    'hammers': 'west ham',
    'copenhagen': 'fc copenhagen',
    'ostersunds': 'ostersund',
    'ludogorets razgrad': 'ludogorets',
    'kardemir karabuk': 'karabukspor',
    'zwolle': 'pec zwolle'
}


# Return the name form the mapping if in it, otherwise return the same team name
def get_exact_name(team_name):
    name = NAME_MAPPING.get(team_name)

    if not name:
        name = team_name

    return name