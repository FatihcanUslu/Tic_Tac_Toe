# Tic_Tac_Toe
In order to work in program all you need pygame . You can pip install pygame on cmd or pip install  or you can pip install -r requirements.txt inside the file path.while its done i can explain the code .

## --BUTTON.PY--

I created this class for call our images and to actively move . It takes the width height image and scale size . 

## --INSIDE OUR Tic_Tac_Toe.py--

game_grid() function is creates our 3x3 game outline .
  
draw_blocks() function created for shape of our x and o blocks . I used pygame.draw.line method for that

Adding and using images: In order to do that i used pygame.image.load method to load our image (line 61). For adding to surface i used button class (line 71) but as you can see some images like x_button and winner1_button created 2000x2000 far from game . Because i wanted that game doesnt start it immediately .First it asks to start and than character selection screen and finally the game area . So as you can see i cant show all the images at the same time . So they far from the game but when i made the decision their location changes on that situration . For example ;

game loop (line 152): after the filling screen with #00ffff  , start_button.draw(line 157) draws our image of start . But its not end for his job it also waits for clicking on start image .When it takes it makes the position moves . This draw method is called from Button class . By reading it you can understand . It continues to the line 199 . So basically clicking images changes it their location . After that our event handler starts(line 199). Its responsible on taking mouse clickes and turns into actions and most importantly creates the areas reserved for the characters we will draw(i mean X and O) on our playground.But due to the brevity of the designated area code gave arror at first time . Thats why i put it in try catch its tries and while noticing no problem to touching outside the range gives no problem. 
 
 ending_game() function is responsible to choose who is winner . In order to do that i created 2 of them . For X and for O . Its basically takes our game surface that created as a 2 dimensional array so checks it that array and change stops to game in order to decide winner . For understand you can activate the 28th line, which is the comment line.

winner1_button and winner2_button  (lines 187 ,190)takes the winner parameter from ending_game and shows the image of winner on the screen . 

All of the images in icons file and the sounds files used in order to background and common game sounds . mixer.music.load method used for that and mixer.music.play(-1) i made it -1 because while making it -1 , it will work in a loop so its wont end until program closed .


# Photos from in game
![foto1](https://user-images.githubusercontent.com/72496488/141329718-f8fc436d-e594-4bcb-9965-09d5c2957b42.PNG)



![foto2](https://user-images.githubusercontent.com/72496488/141329728-49b774c0-9314-4463-bfb5-193a14c89898.PNG)



![foto3](https://user-images.githubusercontent.com/72496488/141329736-e58ddbb3-9810-4b46-90c3-adb2567c5a43.PNG)



![foto4](https://user-images.githubusercontent.com/72496488/141329741-0545e82e-e33c-4263-b7e0-46b63058fa58.PNG)










