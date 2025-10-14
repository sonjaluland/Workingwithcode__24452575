#set background size and ask for 3D canvas
size(1206, 789)
    
#base background colour
fill(255,253,245)
rect(0,0,1206,789)

#Blocking out the background
#blue rect 1
fill(154,189,211)
noStroke()
rect(157,82,515,130)

#blue rect 2
fill(100,127,193)
noStroke()
rect(196,206,700,300)

#Blue sqaure 3
fill(190,212,227)
rect(0,258,200,285)

#bottom left yellow sqaure
fill(250,216,129)
rect(0,540,296,250)

#grey rects
fill(105,112,116)
rect(70,368,136,186)

fill(105,112,116)
rect(124,501,123,145)

fill(187,200,206)
quad(0,0,167,82,220,278,0,265)

#yellow top
fill(255,251,206)
quad(0,0,167,82,800,100,700,0)

# grey sqaure
fill(115,116,121)
rect(654,73,160,139)

#Navy Quad
fill(73,76,85)
quad(815,90,900,160,900,225,800,205)

#navy square
fill(62,64,85)
rect(718,190,50,20)

#gray square
fill(97,98,103)
rect(900,581,330,210)

#blue quad
fill(192,215,229)
quad(1022,210,1200,110,1021,0,809,0)

#blue triangle RIGHT
fill(154,175,188)
triangle(1015,0,1206,0,1206,123)

fill(127,159,178)
triangle(900,500,1206,400,1206,200)


#teal square bottome base
fill(21,92,98)
rect(200,500,1045,395)

#brown sqaure bottom right
fill(100,77,53)
quad(886,510,1070,453,1093,630,900,581)

#grey purple quad bottome right 
fill(90,82,103)
quad(1007,455,1206,415,1206,673,1087,650)


#Creating the Crane 
fill(134,9,9)
quad(900,166,1011,170,1048,430,880,507)

fill(134,9,9)
quad(900,167,1011,171,850,0,670,0)

fill(134,9,9)
quad(880,472,888,517,1206,418,1206,382)

fill(78,87,93)
quad(1015,200,1206,102,1206,200,1043,400)


#Changing opacity for painting look 
fill(250,208,141,80)
quad(885,480,890,520,1206,420,1206,388)
#Creating boathouse base
fill(247,241,217)
noStroke()
rect(310,415,550,100)

#Creating windows 1
fill(118,111,79)
noStroke()
rect(317,420,30,80)

#Creating window 2
fill(129,127,120)
noStroke()
rect(395,420,60,95)

#Creating beam 
fill(129,127,120)
noStroke()
rect(495,420,30,95)

#window 3
fill(90,75,66)
noStroke()
rect(560,430,44,44,8)

#window 4
fill(206,172,117)
noStroke()
rect(645,420,90,93)

#window 5
fill(124,102,66)
noStroke()
rect(765,420,70,95)

# Quad for the roof
fill(232)
noStroke()
quad(241,420,1000,420,870,365,444,363)

#secondary roof
fill(211)
noStroke()
rect(711,345,150,21)

#triangle for roof
fill(193)
noStroke()
triangle(679,345,777,315,893,345)
