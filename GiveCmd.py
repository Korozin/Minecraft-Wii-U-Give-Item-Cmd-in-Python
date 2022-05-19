import math
import socket
import os

# Conversion table of remainders to
# hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}
  
  
# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
    if(decimal <= 0):
        return ''
    remainder = decimal % 16
    return decimalToHexadecimal(decimal//16) + conversion_table[remainder]
  
  
Item_ID = int(input("Item ID: ")) # Item ID Conversion
print("Item ID set", Item_ID,
      "to:", decimalToHexadecimal(Item_ID))
print('Formatted Item_ID String:', decimalToHexadecimal(Item_ID).rjust(8,'0'))

Item_ID_code='000200002FFFFFF0'+decimalToHexadecimal(Item_ID).rjust(8,'0')+'00000000'

print('Formatted Item_ID Code:', Item_ID_code)

Item_Amount = int(input("\nItem Amount: ")) # Item Amount Conversion
print("Item Amount set", Item_Amount,
      "to:", decimalToHexadecimal(Item_Amount))
print('Formatted Item_Amount String:', decimalToHexadecimal(Item_Amount).rjust(8,'0'))

Item_Amount_code='000200002FFFFFF4'+decimalToHexadecimal(Item_Amount).rjust(8,'0')+'00000000'

print('Formatted Item_Amount Code:', Item_Amount_code)

Item_Value = int(input("\nEnter 0 if you're not sure\nItem Damage/Value: ")) # Item Value Conversion
print("Item Damage/Value set", Item_Value,
      "to:", decimalToHexadecimal(Item_Value))
print('Formatted Item_Value String:', decimalToHexadecimal(Item_Value).rjust(8,'0'))

Item_Value_code='000200002FFFFFF8'+decimalToHexadecimal(Item_Value).rjust(8,'0')+'00000000'

print('Formatted Item_Value Code:', Item_Value_code)
print('')

print('Player Slot ID List:\n'+'0 = Player 1 (self)\n'+'8 = Player 2\n10 = player 3\n18 = player 4\n20 = player 5\n28 = player 6\n30 = player 7\n38 = player 8')
Item_Player = int(input("\nWhich Player: ")) # Player Slot Conversion
print("Player Slot Set to:", Item_Player)
print('Formatted Player Slot String:', decimalToHexadecimal(Item_Player).rjust(8,'0'))

Item_Player_code='000200002FFFFFFC'+decimalToHexadecimal(Item_Player).rjust(8,'0')+'00000000D0000000DEADCAFE'

print('Formatted Player Slot Code:', Item_Player_code)

Full_Code = Item_ID_code+Item_Amount_code+Item_Value_code+Item_Player_code+'09020000102EFA640000040000000000C0000038600000009421FF887C0802A63D40109C3D202FFF9001007C614AD8E43D002FFF6129FFFC80CA00006108FFF080E900003D402FFF80C600343D202FFF93C10070614AFFF480C600F86129FFF883C80000810600C893E100743BE00000936100649381006883690000838A000093A1006C7FA8382E93E1005093E10054480000110067006900760065000000007C8802A63D20020B38610008612908D47D2903A64E8004213D20024661290E54808100087D2903A6812100108061000C7F67DB78818100147F86E378800100187FC5F3788161001C3901002881410020912100308121002490810028388100489061002C386100509121004493A1004893E1004C91810034900100389161003C914100404E8004218121004028090007408100183D2003828061003C6129ABB47D2903A64E8004218121002028090007408100183D2003828061001C6129ABB47D2903A64E8004213D40109C3D200304614AD8E46129A5D8814A00007D2903A680C1005038810058812A003480E100548069087890C1005890E1005C4E8004218001007C83610064838100687C0803A683A1006C83C1007083E10074382100784E800020600000003C40010F60426AE07C4903A64E800420D0000000DEADCAFE'

print('\nFull code format:\n'+Full_Code)

IP_Addr=input('\nWii U IP: ')
ip=IP_Addr # IP Address
print('\n ** Sending Command.. **\n')
print('  Connecting to: '+ip)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,7331))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10014CFC00000000'))

cafe=Full_Code # Cafe Code
for x in range(math.floor(len(cafe)/8)):
    s.send(bytes.fromhex('03'))
    s.send(bytes.fromhex('0'+format(0x01133000+x*4,'X')+cafe[x*8:x*8+8]))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10014CFC00000001'))
s.close()
print('\nItem Give Code Sent!')
print('\nPress D-Pad Right to Execute Command')
