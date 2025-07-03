boat_side="Right"
missionaries_right=3
cannibals_right=3
missionaries_left=0
cannibals_left=0

print('M=',missionaries_left,'C=',cannibals_left,'|------B|' 'M=',missionaries_right ,'C=',cannibals_right)

while True:
 missionaries=int(input("Enter the number of missionaries or enter 10 to quit :"))
 if missionaries==10:
    print("You Quit, Game Over!")
    break
 cannibals=int(input("Enter the number of cannibals :"))

 if (missionaries+cannibals) !=1 and (missionaries+cannibals) !=2:
    print("Invalid Move")
    continue
 if boat_side=="Right":
    if missionaries_right<missionaries or cannibals_right<cannibals:
       print("Invalid Move")
    missionaries_right=missionaries_right-missionaries
    cannibals_right=cannibals_right-cannibals

    missionaries_left=missionaries_left+missionaries
    cannibals_left=cannibals_left+cannibals
    
    print('M=',missionaries_left,'C=',cannibals_left,'|B------|' 'M=',missionaries_right ,'C=',cannibals_right)

    boat_side="Left"
 else:
    if missionaries_left<missionaries or cannibals_left<cannibals_left:
       print("Invalid Move")

    missionaries_left=missionaries_left-missionaries
    cannibals_left=cannibals_left-cannibals

    missionaries_right=missionaries_right+missionaries
    cannibals_right=cannibals_right+cannibals   

    print('M=',missionaries_left,'C=',cannibals_left,'|------B|' 'M=',missionaries_right ,'C=',cannibals_right)

    boat_side="Right"
 if (missionaries_right<cannibals_right and missionaries_right>0) or (missionaries_left<cannibals_left and cannibals_left<0):
    print("You Loose!")
    break
 if (missionaries_left==3 and cannibals_left==3):
    print("You Win!")
    break 

            