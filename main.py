from fastapi import FastAPI, HTTPException, Query
import json
#uvicorn main:app --reload
app=FastAPI()

# http methods
# get-cannot write only displays the msg
# post- can write and creates new data
# put - can update
# delete- can delete

@app.get('/')     #ENDPOINT-whtever written in inverted comma 'll be displayed on tht particular page
def greet():
    return{"hello world"}

@app.get('/hello')
def hello():
    return{"welcome to hello page"}

#helper function
def load_data():
    with open("student-data.json","r") as f:
        return json.load(f)

@app.get('/student')
def student_data():
    return load_data()

#student_id=>path parameter
@app.get("/student/{students_id}")
def get_id(students_id:str):
    data=load_data()
    return data[students_id]

"""
amazon.in/s?k=sneakers+for+woman&s=price-asc-rank&crid=2NKLLARMAGM13&qid=1793699598&sprefix=sne%2Caps%2C314&ref=sr_st_price-asc-rank&ds=v1%3Awpdj%2FlNJx6BttEvU2L63RK
we hv sorted it in from low to high i.e. after ? our query starts and we hv given the parameter s=price-asc-rank which means sort by price in ascending order 
"""

#http://127.0.0.1:8000/sort?sort_by=age,grades&order=asc,desc
SORT_FIELDS=["grades","age"]
SORT_ORDER=["asc","desc"]
@app.get("/sort")
def sort_students(
    sort_by: str,
    order: str
):
    #if the given sort_by input does not belong to the SORT_FIELDS list then we will raise an exception
    if sort_by not in SORT_FIELDS:
        raise HTTPException(status_code=404, detail=f"Invalid sort field. Valid fields are: {', '.join(SORT_FIELDS)}")
    
    #if the given order input does not belong to the SORT_ORDER list then we will raise an exception
    if order not in SORT_ORDER:
        raise HTTPException(status_code=404, detail=f"Invalid sort order. Valid orders are: {', '.join(SORT_ORDER)}")

    data = load_data()
    student=[]
    for student_id, student_info in data.items():
        student_info["id"] = student_id
        student.append(student_info)
    #step2 -sort the list by asc/desc order
    reverse=(order=="asc")
    sorted_students=sorted(student,key=lambda s:s[sort_by],reverse=reverse)
    return sorted_students

"""
pagination
http://127.0.0.1:8000/pagination?page=1&limit=2
page->which page we want to see
limit->how many records we want to see in that page
start=(page-1)*limit
end=start+limit
"""
@app.get("/paginate")
def paginate_students(page:int=Query(1,ge=1,description="which page u want starting from 1?"),
                      limit:int=Query(2,ge=1,description="how many records u want to see in that page?")):
    data=load_data()
    student=[]
    for student_id, student_info in data.items():
        student_info["id"] = student_id
        student.append(student_info)
    start=(page-1)*limit
    end=start+limit
    return student[start:end]

"""
pydantic-we use it for validation"""