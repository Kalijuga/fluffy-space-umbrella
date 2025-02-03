import turtle 
  
pen = turtle.Turtle() 
  

def curve(): 
    for i in range(200): 
  
        pen.right(1) 
        pen.forward(1) 
  

def heart(): 
 
    pen.fillcolor('red') 
  
   
    pen.begin_fill() 
  
    pen.left(141) 
    pen.forward(113) 
  
    
    curve() 
    pen.left(120) 
  
    # Draw the right curve 
    curve() 
  
 
    pen.forward(112) 
  
    # Ending the filling of the color 
    pen.end_fill() 
  

def txt(): 
  

    pen.up() 
  

    pen.setpos(-68, 95) 
  
 
    pen.down() 
  

    pen.color('black') 
  

    pen.write(" I love you !", font=( 
      "Verdana", 12, "bold")) 
  
  

heart() 
  

txt() 
  

pen.ht() 
Print ("Fröhlichen Valentienstag 2025")
