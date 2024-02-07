from flask import Blueprint, request, jsonify, Response
import os
from .extensions import mongo
import bcrypt
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

main = Blueprint('main', __name__)

@main.route('/test', methods=['POST'])
def ai_endpoint():
    open_api_key = os.getenv("OPENAI_API_KEY")
    input_data = request.json.get('input', '')
    user_id = request.json.get('user_id', '')  # placeholder for future use

    # validation and processing of the input_data
    if not isinstance(input_data, str) or not input_data.strip():
        return jsonify({'output': "Invalid or empty input"})

    if len(input_data.strip()) < 5:
        return jsonify({'output': "Message too short"})

    # extract client IP
    ipv4 = request.headers.getlist("X-Forwarded-For")[0] if request.headers.getlist("X-Forwarded-For") else request.remote_addr

# login user
@main.route('/api/login_user', methods=['POST'])
 
def login_user():
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    # validate input
    if not email or not password:
        return jsonify({'success': '0', 'message': 'Invalid input'})

    # find the user in the database
    user_collection = mongo.db.users
    user = user_collection.find_one({'email': email})

    # if user does not exist
    if not user:
        return jsonify({'success': '0', 'message': 'User not found'})

    # verify the password
    hashed_password = user['password']
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return jsonify({'success': '1', 'message': 'Login successful'})
    else:
        return jsonify({'success': '0', 'message': 'Invalid credentials'})

# create user
@main.route('/api/create_user', methods=['POST'])
def create_user():
    email = request.json.get('email', '') 
    password = request.json.get('password', '') 

    if not email or not password:
        return jsonify({'success': '0', 'message': 'Invalid input'})
    
    user_collection = mongo.db.users
    
    if user_collection.find_one({'email': email}):
        return jsonify({'success': '0', 'message': 'Email already exists'})

    # hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # store the hashed password, not the plain one
        user_collection.insert_one({'email': email, 'password': hashed_password})
        
    except Exception as e:
        return jsonify({}), 500

    return jsonify({'success': '1', 'message': 'User created successfully'})

# submit question and AI returns response
@main.route('/api/submit_question', methods=['POST'])
def submit_question():
    input_text  = request.json.get('input', '') 
    email = request.json.get('email', '') 
    open_api_key = os.getenv("OPENAI_API_KEY")
    
    # initialize llm
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, max_tokens=150, openai_api_key = open_api_key )    
    
    # create template
    chat_template  = ChatPromptTemplate.from_messages([
        ("system", "Given product description, respond with a compelling sales pitch for that product."),
        ("user", input_text)
    ])
    
    output_parser = StrOutputParser()
    
    chain = chat_template | llm | output_parser
    
    try:
        response = chain.invoke({"input": input_text})
    except Exception as e:
        return jsonify({'success': '0', 'message': f"Error generating response: {str(e)}"}), 500

    
    return jsonify({'success': '1', 'message': response})

# get product by ID
@main.route('/api/product/<int:id>', methods=['GET'])
def get_product(id):
    
    return jsonify({'message': f'Product {id} details'})

# list products
@main.route('/api/list_product', methods=['GET'])
def list_products():
    
    return jsonify({'message': 'List of products'})

# delete product by ID
@main.route('/api/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    
    return jsonify({'message': f'Product {id} deleted successfully'})

@main.route('/health', methods=['GET'])
def health_check():
    return Response("Healthy", status=200, mimetype='text/plain')

