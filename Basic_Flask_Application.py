#######################################################################################################################################################
# What you need to build: A Python fi le that runs a local web server with two working endpoints.
# Endpoint Expected Response / Welcome to app
# Endpoint Expected Response /health App is running 
# How to verify your work: Visit http://localhost:5000/ and http://localhost:5000/health in your browser. Both should show the correct text.
# Ensure: The application runs successfully on localhost , 
# All endpoints return the correct response and are accessible via browser or Postman
# #####################################################################################################################################################

from flask import Flask # Import the Flask Binaries
app = Flask(__name__)
@app.route("/") # Base Page
def home():
    return "Welcome to Flask Application!" 

@app.route("/health")
def health():
    return "Health App is running!" 
if __name__ == "__main__":
    app.run(debug=True)
    
