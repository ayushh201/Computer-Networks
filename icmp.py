import os
import time
import subprocess

host = "8.8.8.8"
num_pings = 5
rtts = []
lost_packets = 0

print(f"Pinging {host} with {num_pings} packets ")

for i in range(num_pings):
    start_time = time.time()
    result = subprocess.run(["ping","-c","1",host],capture_output=True,text=True)
    end_time=time.time()
    rtt = (end_time - start_time)*1000
    if "time=" in result.stdout or "TTL=" in result.stdout:
        print(f"Ping {i+1}: RTT = {rtt:.2f}ms")
        rtts.append(rtt)
    else:
        print(f"Ping {i+1}: Packet lost")
        lost_packets += 1
if rtts:
    min_rtt = min(rtts)
    max_rtt = max(rtts)
    avg_rtt = sum(rtts)/len(rtts)
    packet_loss_rate = (lost_packets/num_pings)*100
    print(f"Min RTT : {min_rtt:.2f}")
    print(f"Max RTT : {max_rtt:.2f}")
    print(f"Avg RTT : {avg_rtt:.2f}")
    print(f"packet_loss_rate RTT : {packet_loss_rate:.2f}")
else:
    print("All packets lost")
