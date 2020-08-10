i = "HELP"
n = "START"
k = "STOP"
m = "QUIT"
engine = 0
print ("Car game")
x = input().upper()
while x != m:
    if engine == 1 and x == n:
        print ("The car is already started")
    if engine == 0 and x == k:
        print ("The car is already stopped")
    if x == i:
        print(n.lower() + " - to start the car")
        print(k.lower() + " - to stop the car")
        print(m.lower() + " - to exit")
    if x == n and engine == 0:
        engine = 1
        print ("Car started... Ready to go!")
    if x == k and engine == 1:
        engine = 0
        print ("Car stopped.")

    if x != n and x != k and x != i:
        print ("I don't understand that...")
    x = input().upper()