import time

epoch_time = time.time()
print('Seconds since epoch:' + str(epoch_time // 1))
print('Minutes since epoch:' + str(epoch_time // 60))
print('Hours since epoch:' + str(epoch_time // (60*60)))
print('Days since epoch:' + str(epoch_time // (60*60*24)))
