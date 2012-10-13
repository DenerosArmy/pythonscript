drawTimeout = None
vidData = [1,1,1,1]

def lambda_function1():
    def lambda_function2():
        global cw, ch
        cw = v.clientWidth
        ch = v.clientHeight
        canvas.width = cw
        canvas.height = ch 
        back.width = cw
        back.height = ch
        draw(v,context,backcontext,cw,ch,1) 

    v = js.document.getElementById('v')
    canvas = js.document.getElementById('c')
    context = js.canvas.getContext('2d') 
    back = js.document.createElement('canvas')
    backcontext = js.back.getContext('2d')
    cw = None
    ch = None
    js.v.addEventListener('play',lambda_function2,False)

js.document.addEventListener('DOMContentLoaded',lambda_function1,False)

def draw(v,c,bc,w,h,value):
    if (v.paused or v.ended):return False 
    js.bc.drawImage(v,0,0,w,h)
    idata = js.bc.getImageData(0,0,w,h)
    data = idata.data 
    for i in range(0,data.length,4):
        r = data[i]
        g = data[i+1]
        b = data[i+2]
        data[i] = r * vidData[0] * vidData[1] 
        data[i+1] = g * vidData[0] * vidData[2] 
        data[i+2] = b * vidData[0] * vidData[3]
    idata.data = data

    js.c.putImageData(idata,0,0)
    js.c.putImageData(idata,0,0) 
    def lambda_function3():
        draw(v,c,bc,w,h,value) 
    drawTimeout = js.setTimeout(lambda_function3, 0)


def changeVideo(attribute,direction):
    vidData[attribute] += direction * .5
