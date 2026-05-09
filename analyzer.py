import pandas as pd
import numpy as np
class studentAnalyzer():
    def __init__(self,filepath,max_marks_per_subject):
        self.filepath=filepath
        self.data=None
        self.max_marks=max_marks_per_subject
    def loadData(self):
        try:
           self.data=pd.read_csv(self.filepath)
           if self.data.empty:
            raise ValueError("this file is empty")
           
        except FileNotFoundError:
            raise FileNotFoundError("no such file exist")
            
        except Exception as e:
            raise Exception(f"something went wrong : {e}")
            
    def analyzeStudent(self):
       results=[]
       subject_columns=self.data.columns[3:]
       for index,row in self.data.iterrows():
          total=np.sum(row[subject_columns])
          average=np.mean(row[subject_columns])
          max_marks=self.max_marks*len(subject_columns)
          percentage=(total/max_marks)*100
          grade=self.get_grade(percentage)
          status='PASS' if percentage>=35 else 'FAIL'

          results.append({
             "enroll_no" : row["enroll_no"],
             "name" : row["name"],
             "total" : total,
             "average_marks" : average,
             "percentage": percentage,
             "grade" : grade,
             "status" : status

          })
       return results
    def get_grade(self,percentage):
       if percentage>=75:
          return 'A'
       elif percentage>=60:
          return 'B'
       elif percentage>=50:
          return 'C'
       elif percentage>=35:
          return 'D'
       else:
          return 'F'
    def class_summary(self,results):
       topper=max(results , key=lambda x: x['percentage'])
       topper_name=topper['name']
       pass_count=sum(1 for r in results if r["status"]=='PASS')
       fail_count=sum(1 for r in results if r["status"]=='FAIL')
       
       count_A=sum(1 for r in results if r["grade"]=='A')
       count_B=sum(1 for r in results if r["grade"]=='B')
       count_C=sum(1 for r in results if r["grade"]=='C')
       count_D=sum(1 for r in results if r["grade"]=='D')
       count_F=sum(1 for r in results if r["grade"]=='F')
       grade_count={
          "no_of_A_grade" : count_A,
           "no_of_B_grade" : count_B,
            "no_of_C_grade" : count_C,
             "no_of_D_grade" : count_D,
             "no_of_fail_student": count_F
       }
       return {
          "topper": topper_name,
          "pass_count":pass_count,
          "fail_count" : fail_count,
          "grade_count" : grade_count
       }

     
             


          

