from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Natascha",
        "message": "You got this, guuuurl!", 
        "hobbies": ["Reading", "Playing Video Games","Hiking", "Traveling"]
    }

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Natascha",
        "message": "You got this, guuuurl!", 
        "hobbies": ["Reading", "Playing Video Games","Hiking", "Traveling"]
    }
    new_hobby = ["Eating"]
    response_body["hobbies"] = response_body["hobbies"] + new_hobby
    return response_body