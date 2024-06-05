from test import *

tracked_asn = [31133,3216,3267,3320,5459,5580,8359,8402,8732,12389,13238,15169,
               16265,16276,20485,20860,21011,21219,22822,24940,28917,29076,
               29329,31500,35320,35662,39832,42610,46489,47541,47542,47764,48268,56630,58073,211157,212236]

has_tracked_asn = ['AS-ROSTELECOM']

dct_tracked = {}

for as_set in has_tracked_asn:
    as_set_obj = AsExpander(as_set)
    for asn in tracked_asn:
        if as_set_obj.asns.get(asn) != None:
            if dct_tracked.get(as_set) == None:
                dct_tracked[as_set] = {as_set_obj.asns.get(asn).copy().pop(): [asn]}
            else:
                #значения для одного и того же ассет не плюсуются , они перезаписываются надо исправлять
                #dct_tracked[as_set][as_set_obj.asns.get(asn).copy().pop()] += f',{str(asn)}'
                dct_tracked[as_set][as_set_obj.asns.get(asn).copy().pop()].append(asn)

#опытка установить соединение была безуспешной,
# т.к. от другого компьютера за требуемое время не получен нужный отклик, или
# было разорвано уже установленное соединение из-за неверного отклика уже подключенного компьютера>

for asn in tracked_asn:
    if as_set_obj.asns.get(asn) != None:
        if dct_tracked.get(as_set) == None:
            dct_tracked[as_set] = {as_set_obj.asns.get(asn).copy().pop():[asn]}
        else:
            #значения для одного и того же ассет не плюсуются , они перезаписываются надо исправлять
            #dct_tracked[as_set][as_set_obj.asns.get(asn).copy().pop()] += f',{str(asn)}'
            dct_tracked[as_set] = {as_set_obj.asns.get(asn).copy().pop(): [asn]}
            dct_tracked[as_set][as_set_obj.asns.get(asn).copy().pop()].append(asn)