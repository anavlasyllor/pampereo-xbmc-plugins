from scraper import (get_rtmp_params, get_channels)

NETWORKS = {
    'Rotana': [],
    'Abu Dhabi': [],
    'Alarabiya': [],
    'Alhayat': [],
    'Aljazeera': ['JSC','Jsc8'],
    'CBC': [],
    'Dubai': [],
    'Dream': [],
    'MBC': [],
    'Panorama': [],
    'Persian': [],
    'Rotana': [],
    'Sama ': [],
    'Nile': [],
    'Melody': [],
    'Al Nahar': ['Al-Nahar', 'Nahar'],
    'Tunisia':['Tuni', 'Nessma', 'Hanib', 'Touni']
}

CATEGORIES = {
    'Movies': ['Cinema', 'Aflam', 'Film', 'Cima'],
    'Drama': ['Series', 'Hekayat'],
    'Comedy': [],
    'Cooking': ['Fatafeat'],
    'Children': ['Ajyal', 'Baraem', 'Cartoon', 'Founon', 'Cocuk', 'Spacepower', 'Toyor'],
    'General': ['Alhayat', 'Dream', 'CBC', 'Faraeen', 'MBC Masr', 'MBC 1', 'MBC 3', 'MBC 4',
                'Masria', 'Masriya', 'Mehwar', 'Misr 25', 'Life', 'On TV', 'Ontv', 'Qatar', 'Dubai', 'Syria', 'Sharjah'],
    'News': ['Alarabiya', 'Aljazeera', 'France', 'Geographic'],
    'Sport': ['riadia', 'Gladiator', 'JSC', 'Mosar3'],
    'Music': ['Aghanina', 'Hits', 'Zaman', 'Khaliji', 'Clip', 'Arabica', 'Ghinwa', 'Mawal', 'Mazzika', 'Mtv', 'Zaman'],
    'Religion': ['Rahma', 'Anwar', 'Kawthar', 'Resala', 'Alnas', 'Coran', 'Iqra'],
    'English': ['Dubai One', 'Top Movies', 'MBC 2', 'Fx', 'MBC Action', 'MBC Drama', 'MBC Max', 'MBC Maghreb']
}

'''The main API object. Useful as a starting point to get available subjects. '''
class TeledunetAPI(object):

    def __init__(self, cache):
        self.cache = cache

    def get_rtmp_params(self, channel_name):
        return get_rtmp_params(channel_name)

    def get_channels(self):
        return get_channels()

    def get_channels_grouped_by_network(self):
        items = []
        channels = self.get_channels()

        for network in NETWORKS:
            children = self.get_channels_for_network(channels, network)
            items.append({
                'network_name': network,
                'label': '%(channel)s ([COLOR blue]%(count)s[/COLOR])' % {'channel': network, 'count': len(children)}
            })

        return items

    def get_channels_grouped_by_category(self):
        items = []
        channels = self.get_channels()

        for category in CATEGORIES:
            children = self.get_channels_for_category(channels, category)
            items.append({
                'category_name': category,
                'label': '%(channel)s ([COLOR blue]%(count)s[/COLOR])' % {'channel': category, 'count': len(children)}
            })

        return items

    def get_channels_for_category(self, channels, channel_name):
        def belongsToNetwork(channel):
            for prefix in CATEGORIES[channel_name]:
                if prefix in channel['label']:
                    return True
            return channel_name in channel['label']

        return filter(belongsToNetwork, channels)

    def get_channels_for_network(self, channels, network_name):

        def belongsToNetwork(channel):
            for prefix in NETWORKS[network_name]:
                 if prefix in channel['label']:
                    return True
                
            return network_name in channel['label']
            	
    	 
        return filter(belongsToNetwork, channels)