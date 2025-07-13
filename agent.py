from transformers import pipeline

class KissyMissyAgent:
    def __init__(self):
        self.chatbot = pipeline("text-generation", model="gpt2")

    def respond(self, user_input):
        response = self.chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
        return response

if __name__ == "__main__":
    agent = KissyMissyAgent()
    while True:
        user_input = input("You: ")
        print("Kissy Missy:", agent.respond(user_input))
