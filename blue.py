from  bluepy.btle import Scanner
from kalman import KalmanFilter
scanner = Scanner()
devices=scanner.scan(5.0)
kalmanFilter = KalmanFilter(0.01,3)
for device in devices:
    print ("DEV={} RSSI ={}".format(device.addr,kalmanFilter.filter(device.rssi)))