from flask import Flask
app = Flask ( __name__ )
API_KEY = " sk_test_51Mx82uFJg ... etc "

@app . route ( " / " )
def home () :
    return " Bonjour , SSII from Caplogy!"

if __name__ == " __main__ " :
    app . run ( debug = True )