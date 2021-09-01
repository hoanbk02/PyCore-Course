"""
Bước Chuẩn bị
    - Cài đặt module speedtest: pip install speedtest-cli
"""


from speedtest import Speedtest

st = Speedtest()

MBps_2_bps = 1024*1024

print(f"Your connection's DOWNLOAD: {st.download()/MBps_2_bps} Megabit/s")
print(f"Your connection's UPLOAD: {st.upload()/MBps_2_bps} Megabit/s")
