from flask import Flask,request,render_template
from analyzer import studentAnalyzer
import os
app=Flask(__name__)
upload_folder="uploads"
os.makedirs(upload_folder,exist_ok=True)
@app.route("/")
def home():
 return render_template("index.html")

@app.route("/analyze" ,methods=["POST"])
def analyze():
 file=request.files["file"]
 if not file.filename.endswith(".csv"):
   return render_template("index.html" ,error=" only CSV files are accepted")
 filepath=os.path.join(upload_folder,file.filename)
 file.save(filepath)
 max_marks=int(request.form["max_marks"])
 try:
   
  analyzer=studentAnalyzer(filepath,max_marks)
  analyzer.loadData()
  results=analyzer.analyzeStudent()
  summary=analyzer.class_summary(results)
  return render_template("result.html" ,results=results, summary=summary)
 except Exception as e:
   return render_template("index.html" ,error=str(e))
   
if __name__ == "__main__":
    app.run(debug=True)

  
  

  
 

