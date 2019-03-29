def setup():
    size(500,500)
    textSize (70)
def draw ():
    text ("K",150, 250)
    text ("W", 250,250)
    
    print (mouseX, mouseY)
    print (hex(get(mouseX,mouseY)))
    if keyPressed:
        print(keyCode)
        if key == "w":
            fill(255,20,147,100)
            text ("W", 250, 250)
            fill(255,240,245)
            text ("K", 150, 250)
            pass
        if key == CODED:
                if keyCode == LEFT:
                    fill (0,250, 154)
                    text ("K", 150,250)
                    fill(255,240,245)
                    text("W", 250, 250)
                    pass
        else:
            fill(255,240,245)
        if key == "k":
            fill (0,250, 154)
            text ("K", 150,250)
            fill(255,240,245)
            text("W", 250, 250)
        if key == CODED:
            if keyCode == RIGHT:
                    fill(255,20,147,100)
                    text ("W", 250, 250)
                    fill(255,240,245)
                    text ("K", 150, 250)
                    pass
        pass
    s= createShape ()
    s.beginShape ()
    s.fill(147,122,219)
    s.noStroke()
    s.vertex (250,300)
    s.vertex (10,250)
    s.vertex (300,400)
    s.vertex (450, 400)
    s.endShape(CLOSE)
    shape (s, 25, 25)
                
