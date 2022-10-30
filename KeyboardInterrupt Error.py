#Dominic Oladapo-Tonade - 6469
#handling the keyboard interrupt error

try:
    dIn = input()
    print('Hit Ctrl+C or interrupt Kernel')

except KeyboardInterrupt:
    print("Caught Interrupt")

else:
    print("No exception occured")
