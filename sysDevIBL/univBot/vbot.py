from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    message = request.form.get("message")

    # Process the chatbot message and generate a response
    response = generate_response(message)

    return jsonify(response)

def generate_response(message):
    if "fee collection" in message:
        response = {
            "message": "To make fee payments, you can use the following channels:\n\n"
                       "1. Online banking: Log in to your bank's online portal and make a transfer to the university's account.\n"
                       "2. Mobile banking: Use your bank's mobile app to transfer funds to the university.\n"
                       "3. Cash payment: Visit the university's finance office to make cash payments."
        }
    elif "signing of nominal roll" in message:
        response = {
            "message": "To sign the nominal roll, please visit the academic affairs office during the designated sign-up period."
        }
    elif "elearning portal" in message:
        response = {
            "message": "Access the eLearning portal using the following link:\n\n"
                       "https://elearning.university.edu"
        }
    elif "library" in message:
        response = {
            "message": "The university library offers various resources and services. You can find more information on their website:\n\n"
                       "https://library.university.edu"
        }
    else:
        response = {
            "message": "I'm sorry, but I couldn't understand your query. Could you please rephrase or ask a different question?"
        }

    return response

if __name__ == "__main__":
    app.run()
