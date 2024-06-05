import json
import re
import urllib.request


def expand_asset(as_set):
    pass


class AsExpander:
    def __init__(self, as_set):
        self.asns = {}
        self.expanded = {}

        self.expand(as_set)

    def expand(self, as_set):
        """ Expand an AS-SET
            Works recursively until all member AS-SETs have been expanded.
            Avoids infinite recursion by saving the name of the expanded
            AS-SETs, thus avoiding loops.
        """
        #print(self.get_members(as_set))
        for member in self.get_members(as_set):
            if member in self.expanded:
                continue
            self.expanded[member] = 2
            if re.match('^[0-9]+$', re.sub('AS', '', member)):
                self.asns[int(re.sub('AS', '', member))] = {as_set}
            else:
                self.expand(member)

    def get_members(self, as_set):
        """ Get members from RIPE DB
        """
        url = "http://rest.db.ripe.net/RIPE/AS-SET/%s" % as_set
        req = urllib.request.Request(url, headers={'Accept': 'application/json'})
        try:
            response = urllib.request.urlopen(req)
        except urllib.error.HTTPError:
            return {}
        data = json.loads(response.read().decode())
        members = []
        for obj in data['objects']['object']:
            for attr in obj['attributes']['attribute']:
                if attr['name'] == 'members':
                    members.append(attr['value'])
        return members


def get_prefixes(origin):
    url = "http://rest.db.ripe.net/search.json?query-string=AS%s&inverse-attribute=origin" % str(origin)
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return {}
    data = json.loads(response.read().decode())
    res = {}
    for obj in data['objects']['object']:
        if obj['type'] == 'route':
            route = {}
            for attr in obj['attributes']['attribute']:
                route[attr['name']] = attr['value']
            res[route['route']] = route

    return res


# if __name__ == '__main__':
#     import argparse
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument(nargs="+", dest="asns")
#     args = parser.parse_args()
#
#     for asn in args.asns:
#         ase = AsExpander(asn)
#         print(set(ase.asns))

