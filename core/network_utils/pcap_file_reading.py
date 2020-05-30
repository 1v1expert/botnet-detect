import pyshark
import datetime
import sqlite3


def contains_line(word,search_word):
    word = word.split("\n")
    for i in word:
        if i.__contains__(search_word) and not i.__contains__("0:") and not i.__contains__("Port"):
            return i


#con = sqlite3.connect("connection.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS pre(id INTEGER, value text)")
#print(datetime.datetime.now().time())
cap = pyshark.FileCapture("core/network_utils/capture20110818-2.truncated.pcap", keep_packets=True)
cap.set_debug()
sess_index = []
sum = 1
pcaps = []
pcap_dic = dict()
for ic, pkt in enumerate(cap):
    print(pkt)
    if ic > 10:
        break
#     try:
#         sess_index.append(pkt.tcp.stream)
#         packet = len(pkt)
#         source = contains_line(str(pkt),"Source")
#         source = source.replace("\tSource: ","").replace("\r","")
#         destination = contains_line(str(pkt),"Destination")
#         destination = destination.replace("\tDestination: ", "").replace("\r", "")
# #         #cur.execute("INSERT INTO pre VALUES(?,?)", (sum, str(pkt.tcp.stream)))
#         pcaps.append((source,packet,destination))
#         pcap_dic[source+" to "+destination] = [0, 0]
#         sum+=1
#         if sum==10:
#             break
#     except:
#         pass
print(pcaps)
# #con.commit()
# #cur.close()
# #con.close()
# for i in range(len(pcaps)):
#         pcap_dic[pcaps[i][0]+" to "+pcaps[i][2]][0] += pcaps[i][1]
#
# for i in pcap_dic:
#     print(i," ",pcap_dic[i])
# print("___________________________")
# s = 0
# for i in list(pcap_dic):
#     for y in list(pcap_dic):
#         if y == i.split(" to ")[1]+" to " + i.split(" to ")[0] and pcap_dic[i][1]!=0:
#             pcap_dic[i][1]+=pcap_dic[y][0]
#             break
# for i in pcap_dic:
#     print(i, "\t", pcap_dic[i])
# print(sess_index)
# print(datetime.datetime.now().time())