dictCountries = {'Afghanistan': 'Kabul', 'Albania': 'Tirana',
                 'Algeria': 'Algiers', 'Andorra': 'Andorra la Vella',
                 'Angola': 'Luanda', 'Antigua and Barbuda': "St. John's",
                 'Argentina': 'Buenos Aires', 'Armenia': 'Yerevan',
                 'Australia': 'Canberra', 'Austria': 'Vienna',
                 'Azerbaijan': 'Baku',
                 'The Bahamas': 'Nassau', 'Bahrain': 'Manama',
                 'Bangladesh': 'Dhaka', 'Barbados': 'Bridgetown',
                 'Belarus': 'Minsk', 'Belgium': 'Brussels',
                 'Belize': 'Belmopan', 'Benin (official)': 'Porto Novo',
                 'Bhutan': 'Thimpu', 'Bolivia (administrative)': 'La Paz',
                 'Bolivia (constitutional)': 'Sucre',
                 'Bosnia and Herzegovina': 'Sarajevo',
                 'Botswana': 'Gaborone', 'Brazil': 'Brasilia',
                 'Brunei': 'Bandar Seri Begawan',
                 'Bulgaria': 'Sofia', 'Burkina Faso': 'Ouagadougou',
                 'Burundi': 'Bujumbura', 'Cambodia': 'Phnom Penh',
                 'Cameroon': 'Yaounde', 'Canada': 'Ottawa',
                 'Central African Republic': 'Bangui',
                 'Chad': "N'Djamena", 'Chile': 'Santiago', 'China': 'Beijing',
                 'Colombia': 'Bogota', 'Comoros': 'Moroni',
                 'Democratic Republic of the Congo': 'Kinshasa',
                 'Republic of the Congo': 'Brazzaville',
                 'Costa Rica': 'San Jose', 'Croatia': 'Zagreb',
                 'Cuba': 'Havana', 'Cyprus': 'Nicosia',
                 'Czech Republic': 'Prague', 'Denmark': 'Copenhagen',
                 'Djibouti': 'Djibouti', 'Dominica': 'Roseau',
                 'Dominican Republic': 'Santo Dominigo',
                 'East Timor': 'Dili', 'Ecuador': 'Quito',
                 'Egypt': 'Cairo', 'El Salvador': 'San Salvador',
                 'Equatorial Guinea': 'Malabo',
                 'Eritrea': 'Asmara', 'Estonia': 'Tallinn',
                 'Ethiopia': 'Addis Ababa', 'Fiji': 'Suva',
                 'Finland': 'Helsinki', 'France': 'Paris',
                 'Gabon': 'Libreville', 'Gambia': 'Banjul',
                 'Georgia': 'Tbilisi',
                 'Germany': 'Berlin', 'Ghana': 'Accra', 'Greece': 'Athens',
                 'Grenada': "St. George's", 'Guatemala': 'Guatemala City',
                 'Guinea': 'Conakry', 'Guinea-Bissau': 'Bissau',
                 'Guyana': 'Georgetown', 'Haiti': 'Port-au-Prince',
                 'Honduras': 'Tegucigalpa', 'Hungary': 'Budapest',
                 'Iceland': 'Rejkyavik', 'India': 'New Delhi',
                 'Indonesia': 'Jakarta', 'Iran': 'Tehran', 'Iraq': 'Baghdad',
                 'Ireland': 'Dublin', 'Israel': 'Jerusalem', 'Italy': 'Rome',
                 'Ivory Coast': 'Yamoussoukro', 'Jamaica': 'Kingston',
                 'Japan': 'Tokyo', 'Jordan': 'Amman',
                 'Kazakhstan': 'Astana', 'Kenya': 'Nairobi',
                 'Kiribati': 'Tarawa', 'Kosovo': 'Pristina',
                 'Kuwait': 'Kuwait City', 'Kyrgyzstan': 'Bishkek',
                 'Laos': 'Vientiane', 'Latvia': 'Riga',
                 'Lebanon': 'Beirut', 'Lesotho': 'Maseru',
                 'Liberia': 'Monrovia', 'Libya': 'Tripoli',
                 'Liechtenstein': 'Vaduz', 'Lithuania': 'Vilnius',
                 'Luxembourg': 'Luxembourg', 'Macedonia': 'Skopje',
                 'Madagascar': 'Antananarivo', 'Malawi': 'Lilongwe',
                 'Malaysia': 'Kuala Lumpur', 'Maldives': 'Male',
                 'Mali': 'Bamako', 'Malta': 'Valletta',
                 'Marshall Islands': 'Majuro',
                 'Mauritania': 'Nouakchott', 'Mauritus': 'Port Louis',
                 'Mexico': 'Mexico City',
                 'Federal States of Micronesia': 'Palikir',
                 'Moldova': 'Chisinau', 'Monaco': 'Monaco',
                 'Mongolia': 'Ulaanbaatar', 'Montenegro': 'Podgorica',
                 'Morocco': 'Rabat', 'Mozambique': 'Maputo',
                 'Myanmar': 'Naypyidaw', 'Namibia': 'Windhoek',
                 'Nauru': 'Yaren', 'Nepal': 'Kathmandu',
                 'Kingdom of the Netherlands': 'Amsterdam',
                 'New Zealand': 'Wellington', 'Nicaragua': 'Managua',
                 'Niger': 'Niamey', 'Nigeria': 'Abuja',
                 'North Korea': 'Pyongyang',
                 'Norway': 'Oslo', 'Oman': 'Muscat', 'Pakistan': 'Islamabad',
                 'Palau': 'Ngerulmud', 'Palestine': 'East Jerusalem',
                 'Panama': 'Panama City', 'Papua New Guinea': 'Port Moresby',
                 'Paraguay': 'Asuncion', 'Peru': 'Lima',
                 'Philippines': 'Manila', 'Poland': 'Warsaw',
                 'Portugal': 'Lisbon', 'Qatar': 'Doha', 'South Korea': 'Seoul',
                 'Romania': 'Bucharest', 'Russia': 'Moscow',
                 'Rwanda': 'Kigali', 'Saint Kitts and Nevis': 'Basseterre',
                 'Saint Lucia': 'Castries',
                 'Saint Vincent and the Grenadines': 'Kingstown',
                 'Samoa': 'Apia', 'San Marino': 'San Marino',
                 'Sao Tome and Principe': 'Sao Tome',
                 'Saudi Arabia': 'Riyadh', 'Senegal': 'Dakar',
                 'Serbia': 'Belgrade', 'Seychelles': 'Victoria',
                 'Sierra Leone': 'Freetown', 'Singapore': 'Singapore',
                 'Slovakia': 'Bratislava', 'Slovenia': 'Llubjana',
                 'Solomon Islands': 'Honiara', 'Somalia': 'Mogadishu',
                 'South Africa (Executive)': 'Pretoria',
                 'South Africa (Juidical)': 'Bloemfontein',
                 'South Africa (Legislative)': 'Cape Town',
                 'South Sudan': 'Juba', 'Spain': 'Madrid',
                 'Sri Lanka': 'Sri Jayawardenepura Kotte',
                 'Sudan': 'Khartoum', 'Suriname': 'Paramaribo',
                 'Swaziland (Administrative)': 'Mbabane',
                 'Swaziland (Legislative)': 'Lobamba',
                 'Sweden': 'Stockholm', 'Switzerland': 'Bern',
                 'Syria': 'Damascus', 'Taiwan': 'Taipei',
                 'Tajikistan': 'Dushanbe', 'Tanzania': 'Dodoma',
                 'Thailand': 'Bangkok', 'Togo': 'Lome',
                 'Tonga': "Nuku'alofa", 'Transnistria': 'Tiraspol',
                 'Trinidad and Tobago': 'Port of Spain',
                 'Tunisia': 'Tunis', 'Turkey': 'Ankara',
                 'Turkmenistan': 'Ashgabat',
                 'Tuvalu': 'Funafuti', 'Uganda': 'Kampala', 'Ukraine': 'Kiev',
                 'United Arab Emirates': 'Abu Dhabi',
                 'United Kingdom': 'London',
                 'United States': 'Washington, D.C.',
                 'Uruguay': 'Montevideo', 'Uzbekistan': 'Tashkent',
                 'Vanuatu': 'Port Vila', 'Vatican City': 'Vatican City',
                 'Venezuela': 'Caracas', 'Vietnam': 'Hanoi',
                 'Yemen': "Sana'a", 'Zambia': 'Lusaka',
                 'Zimbabwe': 'Harare'}


def write_dict(dictCountries):
    return dictCountries


if __name__ == "__main__":
    write_dict(dictCountries)
