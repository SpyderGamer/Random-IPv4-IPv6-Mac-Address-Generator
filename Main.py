# Importing Libraries.
import random, time, secrets, sys

# Variable(s)
valid = False

# Intro Thingy.
print("Welcome to the IPv4-v6-Mac-Address Generator!")

time.sleep(3)

# Function for Generating the IPv4 Address.
def ipv4():
    # Create 4 Different Variables (Each String has a Random Number Between 1 and 255).
    st1_v4 = random.randint(0, 255)
    st2_v4 = random.randint(0, 255)
    st3_v4 = random.randint(0, 255)
    st4_v4 = random.randint(0, 255)

    # Join the Variables and Seperate them by Dots (.)
    ipv4_address = "{}.{}.{}.{}".format(st1_v4, st2_v4, st3_v4, st4_v4)

    print("\nYour Randomly Generated IPv4 Address is:", ipv4_address)

    # Ask the User for Another Prompt.
    time.sleep(2)
    main()

# Function for Generating the IPv6 Address.    
def ipv6():
    # Create 8 Different Variables (Each String has a Random 4 Digit Hex Value).
    st1_v6 = f"{secrets.token_hex(2)}".upper()
    st2_v6 = f"{secrets.token_hex(2)}".upper()
    st3_v6 = f"{secrets.token_hex(2)}".upper()
    st4_v6 = f"{secrets.token_hex(2)}".upper()
    st5_v6 = f"{secrets.token_hex(2)}".upper()
    st6_v6 = f"{secrets.token_hex(2)}".upper()
    st7_v6 = f"{secrets.token_hex(2)}".upper()
    st8_v6 = f"{secrets.token_hex(2)}".upper()

    # Join the Variables and Seperate them by Colons (:)
    ipv6_address = "{}:{}:{}:{}:{}:{}:{}:{}".format(st1_v6, st2_v6, st3_v6, st4_v6, st5_v6, st6_v6, st7_v6, st8_v6)

    print("\nYour Randomly Generated IPv6 Address is:", ipv6_address)

    # Ask the User for Another Prompt.
    time.sleep(2)
    main()

# Function for Generating the Mac Address.
def mac():
    # Create 6 Different Variables (Each String has a Random 2 Digit Hex Value).
    st1_mac = f"{secrets.token_hex(1)}".upper()
    st2_mac = f"{secrets.token_hex(1)}".upper()
    st3_mac = f"{secrets.token_hex(1)}".upper()
    st4_mac = f"{secrets.token_hex(1)}".upper()
    st5_mac = f"{secrets.token_hex(1)}".upper()
    st6_mac = f"{secrets.token_hex(1)}".upper()

    # Join the Variables and Seperate them by Colons (:)
    mac_address = "{}:{}:{}:{}:{}:{}".format(st1_mac, st2_mac, st3_mac, st4_mac, st5_mac, st6_mac)

    print("\nYour Randomly Generated Mac Address is:", mac_address)

    # Ask the User for Another Prompt.
    time.sleep(2)
    main()

# Main Function for User Prompt.
def main():
    global valid

    while not valid:

        print("\nWhich Option Do You Want This Program to Generate?")
        print("[1] IPv4 Address")
        print("[2] IPv6 Address")
        print("[3] Mac Address")
        print("[4] Exit.")
        choice = input("[Option]: ")

        if choice == "1":
            time.sleep(2)
            ipv4()
            valid = True
        
        elif choice == "2":
            time.sleep(2)
            ipv6()
            valid = True
        
        elif choice == "3":
            time.sleep(2)
            mac()
            valid = True
        
        elif choice == "4":
            time.sleep(1)
            print("\nAbort.")
            time.sleep(2)
            sys.exit()
        
        else:
            time.sleep(2)
            print("\nInvalid Choice, Please Provide a Valid Number.")
            time.sleep(2)

# Run The Prompt.
main()