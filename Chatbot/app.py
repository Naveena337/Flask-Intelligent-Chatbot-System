code: 
from flask import Flask, request, jsonify, render_template_string 
app = Flask(__name__) 
HTML_TEMPLATE = """ 
<!DOCTYPE html> 
<html lang="en"> 
<head> 
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Chatbot</title> 
    <style> 
        body { 
            font-family: Arial, sans-serif; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            margin: 0; 
            background: #000080; /* Navy Blue Background */ 
        } 
        #chat-container { 
            width: 400px; 
            height: 600px; 
            border: 1px solid #ccc; 
            background: white; 
            border-radius: 8px; 
            display: flex; 
            flex-direction: column; 
        } 
        #chat-window { 
            flex: 1; 
            padding: 10px; 
            overflow-y: auto; 
            border-bottom: 1px solid #ccc; 
        } 
        input, button { 
            padding: 10px; 
            margin: 5px; 
            border: 1px solid #ccc; 
            border-radius: 4px; 
            font-size: 14px; 
        } 
        button { 
            background-color: red; 
            color: white; 
            cursor: pointer; 
        } 
        button:hover { 
            background-color: #0056b3; 
        } 
        /* Button outline turns red when clicked */ 
        button:focus { 
            outline: 2px solid red; 
        } 
    </style> 
</head> 
<body> 
    <div id="chat-container"> 
        <div id="chat-window"></div> 
        <input type="text" id="user-input" placeholder="Type your message..."> 
        <button id="send-btn">Send</button> 
    </div> 
    <script> 
        const sendBtn = document.getElementById("send-btn"); 
        const userInput = document.getElementById("user-input"); 
        const chatWindow = document.getElementById("chat-window"); 
 
        sendBtn.addEventListener("click", async () => { 
            const message = userInput.value.trim(); 
            if (!message) return; 
 
            const response = await fetch("/chat", { 
                method: "POST", 
                headers: { "Content-Type": "application/json" }, 
                body: JSON.stringify({ message }), 
            }); 
            const data = await response.json(); 
            chatWindow.innerHTML += `<p><strong>You:</strong> ${message}</p>`; 
            chatWindow.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`; 
            userInput.value = ""; 
            chatWindow.scrollTop = chatWindow.scrollHeight; // Auto-scroll 
        }); 
    </script> 
</body> 
</html> 
""" 
def get_bot_response(user_input): 
    """ 
    Generate a response based on the user's input. 
    """ 
    normalized_input = user_input.strip().lower() 
    responses = { 
        "hello": "Hi there! How can I assist you today?", 
        "hi": "Hi there! How can I assist you today?", 
        "how are you": 
        "I'm just a bot, but I'm functioning perfectly. How about you?", 
        "what is your name": 
        "I'm your friendly chatbot. You can call me ChatGPT!", 
        "bye": "Goodbye! Have a great day!", 
        "what can you do": 
        "I can assist you with general questions, provide information, and keep you company!", 
        "tell me a joke": 
        "Why don't scientists trust atoms? Because they make up everything!", 
        "what is python": 
        "Python is a popular programming language known for its simplicity and versatility.", 
        "how old are you": 
        "I'm as old as the code that runs me, which is timeless!", 
        "what is your favorite color": 
        "I like all colors equally, but blue feels calming.", 
        "tell me a fun fact": "Did you know? Octopuses have three hearts!", 
        "what is the weather": 
        "I can't check the weather right now, but you can try a weather app!", 
        "how do computers work": 
        "Computers process data using instructions given by software. They're essentially super
fast calculators!", 
        "what is artificial intelligence": 
        "Artificial Intelligence refers to machines designed to perform tasks that usually require 
human intelligence.", 
        "can you help me": 
        "Of course! Let me know what you need help with, and I'll do my best.", 
        "i am sad": 
        "I'm sorry to hear that. Remember, tough times don't last forever. You’re stronger than you 
think!", 
        "tell me a lame joke": 
        "Why don't skeletons fight each other? They don't have the guts!", 
    } 
    return responses.get( 
        normalized_input, 
        "I'm sorry, I didn't understand that. Can you rephrase?") 
@app.route("/") 
def index(): 
    return render_template_string(HTML_TEMPLATE) 
@app.route("/chat", methods=["POST"]) 
def chat(): 
    user_input = request.json.get("message") 
    if not user_input: 
        return jsonify({"response": "Please provide a valid input."}), 400 
    bot_response = get_bot_response(user_input) 
    return jsonify({"response": bot_response}) 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080) 
  
