# import flask 
import re
from unittest import result
from flask import Flask, render_template,request

# Create the Object 
app = Flask(__name__)

# Define the Routes and bind it with a Function
@app.route('/',methods=['GET','POST'])
def regex101():
    if request.method=='POST':
        xprsn = request.form['xpn']
        tststrng = request.form['tst']
        cnt=0
        if (len(xprsn) ==0 or len(tststrng) == 0):
            cnt=-1
            return render_template("index.html",result="Please provide input",count=cnt)
        else:
            lst=[]
            for match in re.finditer(r'{}'.format(xprsn),tststrng):
                stn=''
                cnt+=1
                stn=stn+"Match {} \"{}\" at start and end indices [{} , {}]".format(cnt,match.group(),match.start(),match.end())
                lst.append(stn)
            return render_template("index.html",result ="Matches found", xpn=xprsn, tst=tststrng, lsts=lst, count=cnt)

    return render_template("index.html",count=-1)

    
# Run the App
if __name__=='__main__':
    app.run(debug=True)