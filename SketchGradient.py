import c4d
from c4d import gui
def main():    
    BaseDraw = doc.GetActiveBaseDraw()
    #Add Sketch And Toon if it's not there and required and set up the defaults

    if c4d.modules.CheckSketch(): #if Sketch and Toon is installed && it is wanted. set it up and use it (Do the check)
        rd = doc.GetActiveRenderData() # Get the current renderdata
        vp = rd.GetFirstVideoPost() # Get the first Video Post in the Renderdata object
        if vp == None:
            SketchEffect = c4d.BaseList2D(1011015) # set a baseList2D with the ID of Sketch and Toon
            rd.InsertVideoPost(SketchEffect) #insert the S&T video post
            vp = rd.GetFirstVideoPost()

        BrowseRD(vp, True) #Run the Function

        if vp.GetName() == "Sketch and Toon": #if S&T was found, the rdata name var should be "Sketch and Toon"...
            SketchEffect = vp #Set the "SketchEffect" variable to the current S&T

        else: #if not, set the "SketchEffect" to a NEW S&T videopost
            SketchEffect = c4d.BaseList2D(1011015) # set a baseList2D with the ID of Sketch and Toon
            rd.InsertVideoPost(SketchEffect) #insert the S&T video post

        SketchEffect[c4d.OUTLINEMAT_SHADING_BACK] = 0
        SketchEffect[c4d.OUTLINEMAT_SHADING_OBJECT_MODEL] = 1
        gradient=SketchEffect[c4d.OUTLINEMAT_SHADING_GRADQUANT]
        print gradient.GetData(c4d.GRADIENT_INTERPOLATION),"ID"
        count = 5 #larger than 1!!!!
        offset = 1 / float(count)
        posOff = 1 / float(count + 1)
        gradient.FlushKnots()
        for i in range(0,count + 1):
            print offset * i
            gradient.InsertKnot(c4d.Vector(i * offset), 1.0, posOff * i)
            #gradient.InsertKnot()#Vector(i * 10),i * 10,i * 10,0,i)
        print gradient.GetKnotCount()
        gradient.SetData(c4d.GRADIENT_INTERPOLATION,5)
        SketchEffect[c4d.OUTLINEMAT_SHADING_GRADQUANT]=gradient

    #Remove Sketch Tags and Replace?
    #Make Sketch Mat?
    c4d.EventAdd()
    
def BrowseRD(rd, children): #function that scrolls through the video post effects to find S&T
    if not rd: return
    
    if rd.GetName() == "Sketch and Toon":
        print("S&T in Video Post is Present...")
        return
    
    BrowseRD(rd.GetNext(), children)
    if children:
      BrowseRD(rd.GetDown(), children)

if __name__=='__main__':
    main()
